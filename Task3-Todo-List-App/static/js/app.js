// TaskNest — global UX enhancements
// Auto-dismiss flash messages
setTimeout(() => {
  document.querySelectorAll(".alert").forEach(a => {
    a.style.transition = "opacity .4s ease";
    a.style.opacity = "0";
    setTimeout(() => a.remove(), 450);
  });
}, 3500);
// Keyboard shortcut: press "n" to jump to "Add task"
document.addEventListener("keydown", (e) => {
  const tag = (e.target.tagName || "").toLowerCase();
  if (tag === "input" || tag === "textarea" || e.metaKey || e.ctrlKey) return;
  if (e.key === "n") {
    const link = document.querySelector('a[href*="/tasks/add"]');
    if (link) { e.preventDefault(); window.location.href = link.href; }
  }
});
// Theme toggle (persisted)
(function () {
  const saved = localStorage.getItem("tn-theme");
  if (saved) document.documentElement.setAttribute("data-theme", saved);
  const btn = document.getElementById("themeToggle");
  if (btn) btn.addEventListener("click", () => {
    const cur = document.documentElement.getAttribute("data-theme") === "light" ? "" : "light";
    if (cur) document.documentElement.setAttribute("data-theme", cur);
    else document.documentElement.removeAttribute("data-theme");
    localStorage.setItem("tn-theme", cur);
  });
})();
