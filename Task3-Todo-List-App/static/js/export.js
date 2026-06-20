// ============================
// TOAST NOTIFICATION SYSTEM
// ============================

function showToast(message) {
    const note = document.createElement("div");

    note.className = "alert alert-success fade-in";
    note.style.position = "fixed";
    note.style.right = "16px";
    note.style.bottom = "16px";
    note.style.zIndex = "9999";
    note.style.minWidth = "220px";

    note.textContent = message;

    document.body.appendChild(note);

    setTimeout(() => {
        note.remove();
    }, 2500);
}


// ============================
// PDF EXPORT TOAST
// ============================

document.addEventListener("DOMContentLoaded", () => {

    const pdfBtn = document.querySelector('a[href="/export/pdf"]');

    if (pdfBtn) {

        pdfBtn.addEventListener("click", () => {

            showToast("📄 Preparing your PDF report...");

        });

    }

    console.log("✅ PDF Export system loaded");

});