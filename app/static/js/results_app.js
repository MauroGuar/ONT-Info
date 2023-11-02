/**
 * Get the table, rows and moreInfoBtn from the DOM.
 */
const table = document.getElementsByClassName("table");
const rows = document.querySelectorAll("tr");
const moreInfoBtn = document.getElementById("more-info-btn");

/**
 * Define the items to show and a flag to indicate whether more information is being shown.
 */
let itemsToShow = ["run state", "temperature(c)", "description", "last down cause", "last up time", "last down time", "ont online duration", "rx optical power(dbm)", "olt rx ont optical power(dbm)", "ont ip 0 address/mask"];
let isShowingMore = false;

/**
 * Add event listeners for DOMContentLoaded and click events.
 */
document.addEventListener('DOMContentLoaded', () => {
    showRowsByKeyValue(itemsToShow);
});

moreInfoBtn.addEventListener('click', toggleShowMoreOrLessInfo);

/**
 * Show rows in the table based on the provided keys.
 * @param {Array} itemsToShow - The keys of the rows to show.
 */
function showRowsByKeyValue(itemsToShow) {
    rows.forEach(row => {
        let tdKey = row.getElementsByClassName("td-key");
        let tdValue = row.getElementsByClassName("td-value");
        if (tdKey.length > 0 && tdValue.length > 0) {
            let keyText = tdKey[0].innerText.trim().toLowerCase();
            if (itemsToShow.includes(keyText)) {
                row.style.display = "flex";
            } else {
                row.style.display = "none";
            }
        }
    });
    stylizeRow();
}

/**
 * Show all rows in the table.
 */
function showAllRows() {
    rows.forEach(row => {
        row.style.display = "flex";
    });
    stylizeRow();
}

/**
 * Toggle between showing more or less information in the table.
 */
function toggleShowMoreOrLessInfo() {
    if (isShowingMore) {
        showRowsByKeyValue(itemsToShow);
        moreInfoBtn.textContent = "Mostrar Más";
    } else {
        showAllRows();
        moreInfoBtn.textContent = "Mostrar Menos";
    }
    isShowingMore = !isShowingMore;
}

/**
 * Apply styles to the rows in the table.
 */
function stylizeRow() {
    i = 0;
    rows.forEach(row => {
        let tdKey = row.getElementsByClassName("td-key");
        let tdValue = row.getElementsByClassName("td-value");
        if (tdKey.length > 0 && tdValue.length > 0) {
            tdKey = tdKey[0];
            tdValue = tdValue[0];
            if (row.style.display != "none") {
                if (i % 2 == 0) {
                    tdKey.style.backgroundColor = "#e3e3e3";
                    tdValue.style.backgroundColor = "#c4d4ffff";
                } else {
                    tdKey.style.backgroundColor = "#f2f2f2";
                    tdValue.style.backgroundColor = "#e9f1ff";
                }
                i++;
            }
        }
    });
}

