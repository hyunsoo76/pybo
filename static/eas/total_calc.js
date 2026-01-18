// static/eas/total_calc.js
(() => {
  // 금액 칸: a_5 ~ j_5
  const AMOUNT_IDS = ["a_5","b_5","c_5","d_5","e_5","f_5","g_5","h_5","i_5","j_5"];

  function parseNumber(v) {
    if (v === null || v === undefined) return 0;
    const s = String(v).trim();
    if (!s) return 0;
    // 콤마/공백 제거
    const cleaned = s.replace(/[,\s]/g, "");
    const n = Number(cleaned);
    return Number.isFinite(n) ? n : 0;
  }

  function formatNumber(n) {
    try {
      return n.toLocaleString("ko-KR");
    } catch {
      return String(n);
    }
  }

  function calcAndRender() {
    let sum = 0;

    for (const id of AMOUNT_IDS) {
      const el = document.getElementById(id);
      if (!el) continue;
      sum += parseNumber(el.value);
    }

    // detail.html / detail_modify.html에 이미 있는 합계 표시 영역
    const totalEl = document.getElementById("total");
    if (totalEl) totalEl.textContent = formatNumber(sum);

    // (선택) hidden total input이 있다면 같이 업데이트 (없으면 그냥 무시됨)
    const totalInput = document.querySelector('input[name="total"], input#total_input');
    if (totalInput) totalInput.value = sum;
  }

  function bind() {
    // 입력할 때마다 합계 갱신
    for (const id of AMOUNT_IDS) {
      const el = document.getElementById(id);
      if (!el) continue;

      el.addEventListener("input", calcAndRender);
      el.addEventListener("change", calcAndRender);
      el.addEventListener("blur", calcAndRender);
    }

    // 페이지 최초 진입 시에도 1번 계산(수정 페이지에서 기존 값 합계 표시)
    calcAndRender();
  }

  document.addEventListener("DOMContentLoaded", bind);
})();
