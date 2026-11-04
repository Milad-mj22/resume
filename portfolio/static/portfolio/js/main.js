(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Navbar ---------- */
  const nav = $("#nav");
  const onScroll = () => nav.classList.toggle("scrolled", scrollY > 30);
  onScroll(); addEventListener("scroll", onScroll, { passive: true });

  const burger = $("#burger"), links = $("#navLinks");
  burger.addEventListener("click", () => {
    const open = links.classList.toggle("open");
    burger.setAttribute("aria-expanded", open);
  });
  $$("a", links).forEach(a => a.addEventListener("click", () => {
    links.classList.remove("open"); burger.setAttribute("aria-expanded", "false");
  }));

$$(".lang, .theme-switcher").forEach(box => {
  const btn = $(".lang-btn", box);
  if (!btn) return;
  btn.addEventListener("click", e => {
    e.stopPropagation();
    $$(".lang, .theme-switcher").forEach(b => b !== box && b.classList.remove("open"));
    const open = box.classList.toggle("open");
    btn.setAttribute("aria-expanded", open);
  });
});

  /* ---------- Count-up (supports Persian digits) ---------- */
  const fa = "۰۱۲۳۴۵۶۷۸۹";
  const toEn = s => s.replace(/[۰-۹]/g, d => fa.indexOf(d));
  const toFa = s => s.replace(/\d/g, d => fa[d]);
  const isFa = document.documentElement.dataset.lang === "fa";

  const countObs = new IntersectionObserver(entries => entries.forEach(en => {
    if (!en.isIntersecting) return;
    const el = en.target, target = +toEn(el.dataset.to), sup = $("sup", el);
    countObs.unobserve(el);
    if (reduce) return;
    const t0 = performance.now(), dur = 1400;
    const tick = now => {
      const p = Math.min((now - t0) / dur, 1), v = Math.round(target * (1 - Math.pow(1 - p, 3)));
      el.firstChild.nodeValue = isFa ? toFa(String(v)) : String(v);
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }), { threshold: .6 });
  $$(".count").forEach(el => countObs.observe(el));

  /* ---------- Skill bars ---------- */
  const barObs = new IntersectionObserver(entries => entries.forEach(en => {
    if (en.isIntersecting) { en.target.classList.add("in"); barObs.unobserve(en.target); }
  }), { threshold: .3 });
  $$(".skills").forEach(el => barObs.observe(el));


  /* ---------- Scroll-driven background (crossfade between layers) ---------- */
  const layers = $$(".bg-layer"), secs = $$("[data-bg]");
  if (layers.length && secs.length) {
    const map = new Map(layers.map(l => [l.dataset.key, l]));
    const fallback = $(".bg-layer img").getAttribute("src");           // profile.png
    layers.forEach(l => {
      const im = $("img", l);
      const fail = () => {
        if (im.dataset.tried || im.getAttribute("src") === fallback) im.classList.add("hide");
        else { im.dataset.tried = 1; im.src = fallback; }              // اگر عکس آن بخش نبود، عکس اصلی
      };
      im.addEventListener("error", fail);
      if (im.complete && im.naturalWidth === 0) fail();
    });

    let cur = null, ticking = false;
    const pick = () => {
      ticking = false;
      const mid = innerHeight * .5;
      let key = secs[0].dataset.bg;
      for (const s of secs) if (s.getBoundingClientRect().top <= mid) key = s.dataset.bg;
      if (key === cur) return;
      cur = key;
      map.forEach((l, k) => l.classList.toggle("active", k === key));
      document.body.dataset.bg = key;
    };
    addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(pick); } }, { passive: true });
    addEventListener("resize", pick);
    pick();
  }

  /* ---------- Background parallax + cursor glow (desktop) ---------- */
  if (!reduce && matchMedia("(hover:hover)").matches) {
    const cur = document.createElement("div"); cur.className = "cursor"; document.body.appendChild(cur);
    const imgs = $$(".bg-layer img");
    addEventListener("mousemove", e => {
      cur.classList.add("on");
      cur.style.left = e.clientX + "px"; cur.style.top = e.clientY + "px";
      const x = (e.clientX / innerWidth - .5) * 14, y = (e.clientY / innerHeight - .5) * 8;
      imgs.forEach(im => im.style.transform = `translate(${x}px,${y}px)`);
    });
    $$("a,button,input,select,textarea").forEach(el => {
      el.addEventListener("mouseenter", () => cur.classList.add("big"));
      el.addEventListener("mouseleave", () => cur.classList.remove("big"));
    });
  }

  /* ---------- Contact form (AJAX) ---------- */
  const form = $("#contactForm"), msg = $("#formMsg");
  form.addEventListener("submit", async e => {
    e.preventDefault();
    $$(".invalid", form).forEach(i => i.classList.remove("invalid"));
    const bad = $$("[required]", form).filter(i => !i.value.trim() || (i.type === "email" && !i.validity.valid));
    if (bad.length) {
      bad.forEach(i => i.classList.add("invalid")); bad[0].focus();
      msg.className = "form-msg err"; msg.textContent = form.dataset.error; return;
    }
    const btn = $("button[type=submit] span", form), label = btn.textContent;
    btn.textContent = form.dataset.sending;
    try {
      const res = await fetch(form.action, {
        method: "POST", body: new FormData(form),
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]", form).value }
      });
      if (!res.ok) throw 0;
      form.reset(); msg.className = "form-msg ok"; msg.textContent = form.dataset.success;
    } catch {
      msg.className = "form-msg err"; msg.textContent = form.dataset.error;
    } finally { btn.textContent = label; }
  });

  /* ---------- Sync favicon & browser theme-color with the CSS theme ---------- */
  const resolve = prop => {                       // تبدیل متغیر CSS به رنگ نهایی (rgb)
    const t = document.createElement("i");
    t.style.cssText = `position:absolute;visibility:hidden;color:var(${prop})`;
    document.body.appendChild(t);
    const v = getComputedStyle(t).color; t.remove(); return v;
  };
  const accent = resolve("--accent"), bgc = resolve("--bg");
  const metaTheme = $('meta[name="theme-color"]'); if (metaTheme) metaTheme.content = bgc;
  const icon = $('link[rel="icon"]');
  if (icon) icon.href = "data:image/svg+xml," + encodeURIComponent(
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" stroke="${accent}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4 4 27h6l6-12 6 12h6L16 4Z"/><path d="M12.5 21h7"/></svg>`);
})();
