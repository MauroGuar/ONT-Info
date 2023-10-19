const waitMsg = document.getElementById('wait-msg');
const form = document.getElementById('ip-sn-form');

form.addEventListener('submit', function () {
    waitMsg.style.display = "flex";
    localStorage.setItem("submittedForm", "true")
});

if (localStorage.getItem("submittedForm") === "true") {
    waitMsg.style.display = "none"
}