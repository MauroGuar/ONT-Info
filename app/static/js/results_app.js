const table = document.getElementsByClassName("table");
const rows = document.querySelectorAll("tr");
const moreInfoBtn = document.getElementById("more-info-btn");

let itemsToShow = ["run state", "temperature(c)", "description", "last down cause", "last up time", "last down time", "ont online duration", "rx optical power(dbm)", "olt rx ont optical power(dbm)"];
let isShowingMore = false;

document.addEventListener('DOMContentLoaded', () => {
    showRowsByKeyValue(itemsToShow);
});

moreInfoBtn.addEventListener('click', toggleShowMoreOrLessInfo);

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

function showAllRows() {
    rows.forEach(row => {
        row.style.display = "flex";
    });
    stylizeRow();
}

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
