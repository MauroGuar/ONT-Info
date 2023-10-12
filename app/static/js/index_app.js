const waitMsg = document.getElementById('wait-msg');
const form = document.getElementById('ip-sn-form');

form.addEventListener('submit', function () {
    waitMsg.style.display = 'flex';
});

form.addEventListener('load', function () {
    waitMsg.style.display = 'none';
});
