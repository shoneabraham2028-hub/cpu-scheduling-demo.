
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>FCFS Scheduler</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
    }

    h2 {
      text-align: center;
    }

    table {
      margin: 20px auto;
      border-collapse: collapse;
      width: 90%;
    }

    th, td {
      border: 1px solid #333;
      padding: 8px 12px;
      text-align: center;
    }

    th {
      background-color: #eee;
    }

    input {
      width: 60px;
    }

    button {
      display: block;
      margin: 20px auto;
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
    }

    .gantt-chart {
      display: flex;
      margin: 30px auto 10px;
      height: 60px;
      border: 2px solid #333;
      width: fit-content;
    }

    .process {
      display: flex;
      justify-content: center;
      align-items: center;
      color: white;
      font-weight: bold;
      border-right: 1px solid white;
      height: 100%;
    }

    .timeline {
      display: flex;
      font-size: 14px;
      width: fit-content;
      margin: 0 auto;
    }

    .timeline div {
      text-align: left;
    }
  </style>
</head>
<body>

<h2>First Come First Serve (FCFS) Scheduling</h2>

<table id="inputTable">
  <thead>
    <tr>
      <th>Process</th>
      <th>Arrival Time (AT)</th>
      <th>Burst Time (BT)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>P1</td>
      <td><input type="number" value="0"></td>
      <td><input type="number" value="5"></td>
    </tr>
    <tr>
      <td>P2</td>
      <td><input type="number" value="1"></td>
      <td><input type="number" value="3"></td>
    </tr>
    <tr>
      <td>P3</td>
      <td><input type="number" value="2"></td>
      <td><input type="number" value="8"></td>
    </tr>
    <tr>
      <td>P4</td>
      <td><input type="number" value="3"></td>
      <td><input type="number" value="6"></td>
    </tr>
  </tbody>
</table>

<button onclick="runFCFS()">Run FCFS</button>

<div id="result"></div>

<script>
  function runFCFS() {
    const table = document.getElementById("inputTable").getElementsByTagName("tbody")[0];
    const rows = table.getElementsByTagName("tr");

    const processes = [];

    for (let i = 0; i < rows.length; i++) {
      const pname = `P${i + 1}`;
      const at = parseInt(rows[i].cells[1].children[0].value);
      const bt = parseInt(rows[i].cells[2].children[0].value);
      processes.push({ pname, at, bt });
    }

    processes.sort((a, b) => a.at - b.at);

    let time = 0;
    let resultHTML = `
      <table>
        <thead>
          <tr>
            <th>Process</th>
            <th>Burst Time (BT)</th>
            <th>Completion Time (CT)</th>
            <th>Turnaround Time (TAT)</th>
            <th>Waiting Time (WT)</th>
          </tr>
        </thead>
        <tbody>
    `;

    let ganttHTML = `<div class="gantt-chart">`;
    let timelineHTML = `<div class="timeline">`;
    const colors = ["#0074D9", "#2ECC40", "#FF851B", "#B10DC9", "#FF4136", "#FFDC00"];
    let ganttTime = 0;

    processes.forEach((p, i) => {
      if (time < p.at) {
        time = p.at;
      }
      const start = time;
      time += p.bt;
      const ct = time;
      const tat = ct - p.at;
      const wt = tat - p.bt;

      resultHTML += `
        <tr>
          <td>${p.pname}</td>
          <td>${p.bt}</td>
          <td>${ct}</td>
          <td>${tat}</td>
          <td>${wt}</td>
        </tr>
      `;

      const width = p.bt * 20;
      ganttHTML += `<div class="process" style="width:${width}px; background:${colors[i % colors.length]}">${p.pname}</div>`;
      timelineHTML += `<div style="width:${width}px;">${start}</div>`;
      ganttTime = ct;
    });

    timelineHTML += `<div style="width:0px;">${ganttTime}</div>`;
    ganttHTML += `</div>`;
    timelineHTML += `</div>`;

    resultHTML += `</tbody></table>`;
    document.getElementById("result").innerHTML = resultHTML + ganttHTML + timelineHTML;
  }
</script>

</body>
</html>


