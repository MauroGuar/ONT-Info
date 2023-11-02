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

/**
 * @type {Array}
 * @description Array of IP options for OLT.
 */
const oltIpOptions = ["172.17.254.34", "172.17.254.8", "172.17.254.9", "172.17.254.4", "172.17.254.30", "172.17.254.14", "172.17.254.21", "172.17.254.15", "172.17.254.45"];

/**
 * @type {HTMLSelectElement}
 * @description The select element for OLT IP options.
 */
const selectOltIp = document.getElementById("olt_ip");

/**
 * Populates the selectOltIp element with options from oltIpOptions array.
 */
oltIpOptions.forEach(olt_ip => {
    /**
     * @type {HTMLOptionElement}
     * @description An option element for the selectOltIp element.
     */
    let option = document.createElement("option");
    option.value = olt_ip;
    option.text = olt_ip;
    selectOltIp.appendChild(option);
});








