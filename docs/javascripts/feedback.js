document.addEventListener("DOMContentLoaded", function () {
  const params = new URLSearchParams(window.location.search);
  const editUrl = params.get("from");
  const btn = document.getElementById("quick-edit-btn");

  if (btn && editUrl) {
    btn.href = editUrl;
  }
});