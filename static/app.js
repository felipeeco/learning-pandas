const status = document.querySelector("#status");
const tableHead = document.querySelector("#table-head");
const tableBody = document.querySelector("#table-body");

async function loadData() {
  try {
    const response = await fetch("/api/data", { cache: "no-store" });
    const data = await response.json();

    if (!response.ok) throw new Error(data.error || "The request failed");

    renderTable(data.columns, data.rows);
    status.textContent = "";
  } catch (error) {
    status.textContent = `Error: ${error.message}`;
    tableHead.replaceChildren();
    tableBody.replaceChildren();
  }
}

function renderTable(columns, rows) {
  const headingRow = document.createElement("tr");
  columns.forEach((column) => {
    const cell = document.createElement("th");
    cell.scope = "col";
    cell.textContent = column.replaceAll("_", " ");
    headingRow.append(cell);
  });
  tableHead.replaceChildren(headingRow);

  const rowElements = rows.map((row) => {
    const tableRow = document.createElement("tr");
    columns.forEach((column) => {
      const cell = document.createElement("td");
      cell.textContent = row[column];
      tableRow.append(cell);
    });
    return tableRow;
  });
  tableBody.replaceChildren(...rowElements);
}

loadData();
