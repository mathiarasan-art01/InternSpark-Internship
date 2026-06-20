document.querySelectorAll(".stat-value").forEach(el => {
  const text = el.textContent.trim();
  const m = text.match(/^(\d+)(%?)$/);
  if (!m) return;
  const end = parseInt(m[1], 10);
  const suffix = m[2] || "";
  const dur = 600;
  const start = performance.now();
  function step(now) {
    const p = Math.min(1, (now - start) / dur);
    el.textContent = Math.round(end * p) + suffix;
    if (p < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
});