// static/eas/vendor_autocomplete.js
(() => {
  const API_URL = "/eas/api/vendor-suggest/";
  const LIMIT = 10;
  const DEBOUNCE_MS = 120;

  // a_1 ~ j_1 만 대상
  const VENDOR_INPUT_ID_RE = /^[a-j]_1$/;

  function debounce(fn, ms) {
    let t = null;
    return (...args) => {
      clearTimeout(t);
      t = setTimeout(() => fn(...args), ms);
    };
  }

  function formatNumber(n) {
  if (n === null || n === undefined || n === "") return "";
  const num = Number(n);
  if (Number.isNaN(num)) return "";
  return num.toLocaleString("ko-KR");
}


  function ensureDropdown(input) {
    let dd = input._vendorDropdown;
    if (dd) return dd;

    dd = document.createElement("div");
    dd.className = "vendor-suggest";
    dd.style.position = "absolute";
    dd.style.zIndex = "9999";
    dd.style.display = "none";
    dd.style.background = "white";
    dd.style.border = "1px solid #ddd";
    dd.style.borderRadius = "8px";
    dd.style.boxShadow = "0 6px 18px rgba(0,0,0,0.08)";
    dd.style.maxHeight = "320px";
    dd.style.overflowY = "auto";
    dd.style.minWidth = "900px";

    document.body.appendChild(dd);
    input._vendorDropdown = dd;
    input._vendorActiveIndex = -1;
    input._vendorItems = [];

    return dd;
  }

  function positionDropdown(input, dd) {
    const r = input.getBoundingClientRect();
    dd.style.left = `${window.scrollX + r.left}px`;
    dd.style.top = `${window.scrollY + r.bottom + 6}px`;
    dd.style.width = `${Math.max(r.width, 900)}px`;
  }

  function closeDropdown(input) {
    const dd = input._vendorDropdown;
    if (!dd) return;
    dd.style.display = "none";
    dd.innerHTML = "";
    input._vendorActiveIndex = -1;
    input._vendorItems = [];
  }

  function closeAllDropdowns() {
    document.querySelectorAll("input[id]").forEach((el) => {
      if (!el._vendorDropdown) return;
      if (el._vendorDropdown.style.display !== "block") return;
      closeDropdown(el);
    });
  }

  function escapeHtml(s) {
    return String(s ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  // ✅ used_at (ISO 문자열) -> "YYYY-MM-DD" 표시
  function formatUsedAt(iso) {
    if (!iso) return "";
    const d = new Date(iso);
    if (Number.isNaN(d.getTime())) return "";
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, "0");
    const day = String(d.getDate()).padStart(2, "0");
    return `${y}-${m}-${day}`;
  }

  function renderDropdown(input, items) {
    const dd = ensureDropdown(input);
    positionDropdown(input, dd);

    const prevIdx =
      typeof input._vendorActiveIndex === "number" ? input._vendorActiveIndex : 0;

    input._vendorItems = items || [];

    if (!input._vendorItems.length) {
      input._vendorActiveIndex = -1;
    } else {
      input._vendorActiveIndex = Math.min(
        Math.max(prevIdx, 0),
        input._vendorItems.length - 1
      );
    }

    dd.innerHTML = "";

    if (!input._vendorItems.length) {
      dd.style.display = "none";
      return;
    }

    input._vendorItems.forEach((it, idx) => {
      const row = document.createElement("div");
      row.className = "vendor-suggest-row";
      row.dataset.index = String(idx);
      row.style.padding = "10px 12px";
      row.style.cursor = "pointer";
      row.style.borderBottom = "1px solid #f1f1f1";
      row.style.whiteSpace = "nowrap";
      row.style.overflow = "hidden";
      row.style.textOverflow = "ellipsis";

      // ✅ 레이아웃: 좌/우 간격 줄이고 금액을 왼쪽으로 당김
      const top = document.createElement("div");
      top.style.display = "grid";
      top.style.gridTemplateColumns = "auto 480px"; // ✅ 우측은 내용만큼
      top.style.columnGap = "14px";
      top.style.justifyContent = "space-between"; // ✅ 양쪽을 끝으로 밀착

      const left = document.createElement("div");
      left.style.minWidth = "0";
      left.style.whiteSpace = "nowrap";
      left.style.maxWidth = "620px";        // ✅ 추가
      left.style.overflow = "hidden";        // ✅ 추가
      left.style.textOverflow = "ellipsis";  // ✅ 추가
      left.innerHTML = `
        <strong>${escapeHtml(it.vendor)}</strong>
        <span style="margin-left:10px;color:#666;font-size:12px;">
          ${escapeHtml(it.account_no)} / ${escapeHtml(it.bank)} / ${escapeHtml(it.account_name)}
        </span>
      `;
      const right = document.createElement("div");
      right.style.display = "grid";
      right.style.gridTemplateColumns = "110px 90px 1fr"; // 날짜 / 금액 / 비고
      right.style.alignItems = "center";
      right.style.gap = "10px";
      right.style.fontSize = "12px";
      right.style.whiteSpace = "nowrap";

      const amountText = formatNumber(it.amount);

        const dateText = formatUsedAt(it.used_at);

        right.innerHTML = `
          <span style="color:#666;text-align:center;">
            ${escapeHtml(dateText)}
          </span>

          <span style="color:#0f766e;text-align:right;font-weight:600;">
            ${escapeHtml(amountText)}
          </span>

          <span style="color:#666;overflow:hidden;text-overflow:ellipsis;">
            ${escapeHtml(it.note || "")}
          </span>
        `;


      top.appendChild(left);
      top.appendChild(right);
      row.appendChild(top);

      row.addEventListener("mouseenter", () => {
        input._vendorActiveIndex = idx;
        paintActive(input);
      });

      row.addEventListener("mousedown", (e) => {
        e.preventDefault(); // blur보다 먼저
        applySelection(input, idx);
      });

      dd.appendChild(row);
    });

    dd.style.display = "block";
    paintActive(input);
  }

  function paintActive(input) {
    const dd = input._vendorDropdown;
    if (!dd) return;

    const rows = dd.querySelectorAll(".vendor-suggest-row");
    rows.forEach((r) => (r.style.background = "white"));

    const idx = input._vendorActiveIndex;
    if (idx >= 0 && rows[idx]) {
      rows[idx].style.background = "#f5f5f5";
      rows[idx].scrollIntoView({ block: "nearest" });
    }
  }

  function applySelection(input, idx) {
    const items = input._vendorItems || [];
    const it = items[idx];
    if (!it) return;

    // ✅ 잔상 방지: 선택 즉시 닫기
    closeDropdown(input);
    closeAllDropdowns();

    const prefix = input.id.split("_")[0]; // a,b,c...
    const elVendor = document.getElementById(`${prefix}_1`);
    const elAccNo = document.getElementById(`${prefix}_2`);
    const elBank = document.getElementById(`${prefix}_3`);
    const elAccName = document.getElementById(`${prefix}_4`);
    const elAmount = document.getElementById(`${prefix}_5`);
    const elType = document.getElementById(`${prefix}_6`); // 구분

    if (elVendor) elVendor.value = it.vendor || "";
    if (elAccNo) elAccNo.value = it.account_no || "";
    if (elBank) elBank.value = it.bank || "";
    if (elAccName) elAccName.value = it.account_name || "";

    // ✅ 매입처가 한국3M(자체)면 구분 자동 입력
    if (elType && (it.vendor || "").trim() === "한국3M(자체)") {
      elType.value = "대진상사";
    }

    if (elAmount) elAmount.focus();
  }

  async function fetchSuggest(q) {
    const url = new URL(API_URL, window.location.origin);
    url.searchParams.set("q", q);
    url.searchParams.set("limit", String(LIMIT));

    const res = await fetch(url.toString(), {
      headers: { "X-Requested-With": "XMLHttpRequest" },
    });
    if (!res.ok) return [];
    const data = await res.json();
    return data.items || [];
  }

  const onInput = debounce(async (e) => {
    const input = e.target;
    const q = (input.value || "").trim();

    if (!q) {
      closeDropdown(input);
      return;
    }

    try {
      const items = await fetchSuggest(q);
      renderDropdown(input, items);
    } catch (err) {
      closeDropdown(input);
    }
  }, DEBOUNCE_MS);

  function onKeyDown(e) {
    const input = e.target;
    const dd = input._vendorDropdown;
    const open = dd && dd.style.display === "block";
    if (!open) return;

    const items = input._vendorItems || [];
    if (!items.length) return;

    // 메뉴 열려있을 때는 기존 페이지 엔터/이동 로직 막기
    if (["ArrowDown", "ArrowUp", "Enter", "Escape", "Tab"].includes(e.key)) {
      e.preventDefault();
      e.stopPropagation();
    }

    if (typeof input._vendorActiveIndex !== "number" || input._vendorActiveIndex < 0) {
      input._vendorActiveIndex = 0;
      paintActive(input);
    }

    if (e.key === "ArrowDown") {
      input._vendorActiveIndex = Math.min(items.length - 1, input._vendorActiveIndex + 1);
      paintActive(input);
      return;
    }

    if (e.key === "ArrowUp") {
      input._vendorActiveIndex = Math.max(0, input._vendorActiveIndex - 1);
      paintActive(input);
      return;
    }

    if (e.key === "Enter") {
      applySelection(input, input._vendorActiveIndex);
      return;
    }

    if (e.key === "Escape") {
      closeDropdown(input);
      return;
    }

    // Tab은 “선택 안 하고 이동”
    if (e.key === "Tab") {
      closeDropdown(input);
      return;
    }
  }

  function onFocus(e) {
    const input = e.target;
    const dd = ensureDropdown(input);
    positionDropdown(input, dd);
  }

  function onBlur(e) {
    const input = e.target;
    setTimeout(() => closeDropdown(input), 120);
  }

  function bind(input) {
    ensureDropdown(input);
    input.addEventListener("input", onInput);

    // 캡처 단계에서 키다운 먼저 가로채기
    input.addEventListener("keydown", onKeyDown, true);

    input.addEventListener("focus", onFocus);
    input.addEventListener("blur", onBlur);
  }

  document.addEventListener("DOMContentLoaded", () => {
    const inputs = document.querySelectorAll("input[id]");
    inputs.forEach((el) => {
      if (VENDOR_INPUT_ID_RE.test(el.id)) bind(el);
    });

    // vendor input 밖으로 포커스 이동하면 닫기
    document.addEventListener("focusin", (ev) => {
      const target = ev.target;

      const isVendorInput =
        target && target.id && VENDOR_INPUT_ID_RE.test(target.id);

      let isInsideAnyDropdown = false;
      document.querySelectorAll("input[id]").forEach((el) => {
        if (!el._vendorDropdown) return;
        if (el._vendorDropdown.contains(target)) isInsideAnyDropdown = true;
      });

      if (!isVendorInput && !isInsideAnyDropdown) {
        closeAllDropdowns();
      }
    });

    window.addEventListener(
      "scroll",
      () => {
        document.querySelectorAll("input[id]").forEach((el) => {
          if (!el._vendorDropdown) return;
          if (el._vendorDropdown.style.display !== "block") return;
          positionDropdown(el, el._vendorDropdown);
        });
      },
      { passive: true }
    );

    window.addEventListener("resize", () => {
      document.querySelectorAll("input[id]").forEach((el) => {
        if (!el._vendorDropdown) return;
        if (el._vendorDropdown.style.display !== "block") return;
        positionDropdown(el, el._vendorDropdown);
      });
    });
  });
})();
