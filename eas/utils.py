from datetime import date, time
from django.db import connections
from datetime import time


def is_director_absent(now_dt):
    today = now_dt.date()
    now_time = now_dt.time()

    with connections['leave'].cursor() as cursor:
        cursor.execute("""
            SELECT leave_type, half_day
            FROM leaves_leaverequest lr
            JOIN leaves_employee e ON lr.employee_id = e.id
            WHERE e.name = %s
            AND lr.start_date <= %s
            AND lr.end_date >= %s
            LIMIT 1
        """, ["정현수", today, today])

        row = cursor.fetchone()

        print("DEBUG today:", today)
        print("DEBUG row:", row)

    if not row:
        return False

    leave_type, half_day = row

    # 연차
    if leave_type == "ANNUAL":
        return True

    # 반차
    if leave_type == "HALF":
        if half_day == "AM":
            return now_time < time(12, 0)
        elif half_day == "PM":
            return now_time >= time(12, 0)

    return False