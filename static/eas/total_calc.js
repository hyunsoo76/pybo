// static/eas/total_calc.js
(() => {
  // 금액 칸: a_5 ~ j_5
  const AMOUNT_IDS = ["a_5","b_5","c_5","d_5","e_5","f_5","g_5","h_5","i_5","j_5"];

  function digitsOnly(s) {
    return String(s ?? "").replace(/[^\d]/g, "");
  }

  function parseNumber(v) {
    const d = digitsOnly(v);
    if (!d) return 0;
    const n = Number(d);
    return Number.isFinite(n) ? n : 0;
  }

  function formatCommaFromDigits(d) {
    if (!d) return "";
    // 앞자리에 불필요한 0 제거(원하면 제거하지 않아도 됨)
    d = d.replace(/^0+(?=\d)/, "");
    return d.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }

  // 커서 위치를 최대한 유지하면서 값 포맷팅
  function setFormattedKeepingCaret(el) {
    const oldValue = el.value ?? "";
    const oldCaret = el.selectionStart ?? oldValue.length;

    // "커서 왼쪽에 있던 숫자 개수"를 기준으로 새 caret 계산
    const leftPart = oldValue.slice(0, oldCaret);
    const leftDigitsCount = digitsOnly(leftPart).length;

    const digits = digitsOnly(oldValue);
    const formatted = formatCommaFromDigits(digits);

    el.value = formatted;

    // 새 문자열에서 leftDigitsCount만큼 숫자를 지난 위치로 caret 이동
    if (typeof el.setSelectionRange === "function") {
      if (leftDigitsCount === 0) {
        el.setSelectionRange(0, 0);
        return;
      }
      let seen = 0;
      let pos = 0;
      for (; pos < formatted.length; pos++) {
        if (/\d/.test(formatted[pos])) {
          seen += 1;
          if (seen >= leftDigitsCount) {
            pos += 1; // 해당 숫자 뒤
            break;
          }
        }
      }
      el.setSelectionRange(pos, pos);
    }
  }

  function calcAndRenderTotal() {
    let sum = 0;
    for (const id of AMOUNT_IDS) {
      const el = document.getElementById(id);
      if (!el) continue;
      sum += parseNumber(el.value);
    }

    const totalEl = document.getElementById("total");
    if (totalEl) totalEl.textContent = sum.toLocaleString("ko-KR");

    // (있으면) hidden total도 같이 갱신
    const totalInput = document.querySelector('input[name="total"], input#total_input');
    if (totalInput) totalInput.value = String(sum);
  }

  function onAmountInput(e) {
    const el = e.target;
    setFormattedKeepingCaret(el);
    calcAndRenderTotal();
  }

  function onBlur(e) {
    const el = e.target;
    // blur 시에도 한번 정리(콤마/숫자)
    el.value = formatCommaFromDigits(digitsOnly(el.value));
    calcAndRenderTotal();
  }

  function bind() {
    for (const id of AMOUNT_IDS) {
      const el = document.getElementById(id);
      if (!el) continue;

      // 모바일에서 숫자 키패드 유도
      el.setAttribute("inputmode", "numeric");
      el.setAttribute("autocomplete", "off");

      el.addEventListener("input", onAmountInput);
      el.addEventListener("blur", onBlur);
    }

    // 수정 페이지에서 기존 값도 콤마 포맷 적용 + 합계 1회 계산
    for (const id of AMOUNT_IDS) {
      const el = document.getElementById(id);
      if (!el) continue;
      el.value = formatCommaFromDigits(digitsOnly(el.value));
    }
    calcAndRenderTotal();
  }

  document.addEventListener("DOMContentLoaded", bind);

  // submit 전에 서버로는 콤마 제거된 숫자만 보내기
  document.addEventListener("submit", (e) => {
    const form = e.target;
    if (!(form instanceof HTMLFormElement)) return;

    for (const id of AMOUNT_IDS) {
      const el = document.getElementById(id);
      if (!el) continue;
      el.value = String(parseNumber(el.value));
    }
  });
})();
