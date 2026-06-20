// Live search debounce — submits search form 400ms after typing stops
(function () {
  const input = document.querySelector('input[name="q"]');
  if (!input) return;
  let t;
  input.addEventListener("input", () => {
    clearTimeout(t);
    t = setTimeout(() => input.form && input.form.submit(), 400);
  });
})();