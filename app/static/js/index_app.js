/**
 * @fileoverview This script handles displaying the wait message when the form is submitted.
 */

/**
 * @type {HTMLElement}
 * @description The element that displays the waiting message.
 */
const waitMsg = document.getElementById('wait-msg');

/**
 * @type {HTMLFormElement}
 * @description The form element.
 */
const form = document.getElementById('ip-sn-form');

/**
 * An event listener that displays the waiting message when the form is submitted.
 */
form.addEventListener('submit', function () {
    /**
     * Changes the display style of waitMsg to "flex" when the form is submitted.
     */
    waitMsg.style.display = "flex";
});

/**
 * An event listener that handles the unloading of the window.
 * This is used so that the waiting message is hidden again in case the user returns to the page.
 */
window.onunload = function (e) {
}






