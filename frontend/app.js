const questionInput = document.getElementById("questionInput");
const responseBox = document.getElementById("responseBox");
const satisfactionSlider = document.getElementById("satisfactionSlider");
const satisfactionValue = document.getElementById("satisfactionValue");
const departmentDropdown = document.getElementById("departmentDropdown");
const themeToggle = document.getElementById("themeToggle");

// Update satisfaction value display
satisfactionSlider.addEventListener("input", () => {
  satisfactionValue.textContent = satisfactionSlider.value;
});

themeToggle.addEventListener("change", () => {
  document.body.classList.toggle("dark-theme");
});

// Ask question and get response from backend
async function askQuestion() {
  const question = questionInput.value.trim();
  const department = departmentDropdown.value;
  const satisfaction = satisfactionSlider.value;

  let enhancedQuery = question;
  if (department && department !== "-- Select Department --") {
    enhancedQuery += ` in the ${department} department`;
  }
  if (satisfaction) {
    enhancedQuery += ` with job satisfaction of ${satisfaction}`;
  }

  if (!question) {
    responseBox.innerHTML = `<span style="color:red;">Please enter a question.</span>`;
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: enhancedQuery }),
    });

    const data = await response.json();

    responseBox.innerHTML = `
      <div><strong>📂 Answer:</strong><br>${data.answer}</div>
      <br>
      <div><strong>📄 Sources:</strong><ul>${data.sources.map(s => `<li>${s}</li>`).join("")}</ul></div>
    `;
  } catch (err) {
    console.error("Error:", err);
    responseBox.innerHTML = `<span style="color:red;">Error fetching response from backend.</span>`;
  }
}

// Load charts
async function loadAnalytics() {
  try {
    const response = await fetch("http://127.0.0.1:8000/employee-stats");
    const stats = await response.json();

    const attritionCtx = document.getElementById("attritionChart")?.getContext("2d");
    const departmentCtx = document.getElementById("departmentChart")?.getContext("2d");

    if (attritionCtx) {
      new Chart(attritionCtx, {
        type: "doughnut",
        data: {
          labels: ["At Risk", "Not at Risk"],
          datasets: [{
            data: [stats.at_risk_count, stats.not_at_risk_count],
            backgroundColor: ["#ef4444", "#10b981"],
          }]
        },
        options: {
          plugins: {
            legend: { position: "bottom" }
          }
        }
      });
    }

    if (departmentCtx) {
      new Chart(departmentCtx, {
        type: "bar",
        data: {
          labels: Object.keys(stats.departments),
          datasets: [{
            label: "Employees per Department",
            data: Object.values(stats.departments),
            backgroundColor: "#3b82f6",
          }]
        },
        options: {
          scales: {
            y: { beginAtZero: true }
          }
        }
      });
    }

  } catch (err) {
    console.error("Failed to load analytics:", err);
  }
}

window.onload = loadAnalytics;
