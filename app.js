document.addEventListener('DOMContentLoaded', function() {
    // Navigation smooth scroll
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
                document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
                this.classList.add('active');
            }
        });
    });

    // Modal elements
    const modal = document.getElementById('result-modal');
    const closeBtn = document.getElementById('close-modal');
    const paramsList = document.getElementById('input-params-list');
    const modalOutput = document.getElementById('modal-prediction-output');

    // Show modal
    function showModal(inputs, prediction) {
        // List all input parameters
        paramsList.innerHTML = '';
        for (const [key, value] of Object.entries(inputs)) {
            // Format key nicely
            const label = key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
            paramsList.innerHTML += `<li><strong>${label}:</strong> ${value}</li>`;
        }
        // Show prediction
        modalOutput.innerHTML = `
            <div class="result-field"><strong>Accident:</strong> ${prediction.accident}</div>
            <div class="result-field"><strong>Severity:</strong> ${prediction.severity}</div>
            <div class="result-field"><strong>Chance of Accident:</strong> ${prediction.probability}</div>
        `;
        modal.style.display = 'block';
    }

    // Close modal
    closeBtn.onclick = function() {
        modal.style.display = 'none';
    };
    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };

    // Prediction form
    const form = document.getElementById('predict-form');
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const data = {};
        form.querySelectorAll('input, select').forEach(el => {
            data[el.name] = el.value;
        });
        fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(resp => resp.json())
        .then(res => {
            showModal(data, res);
        })
        .catch(() => {
            showModal({}, {
                accident: "<span style='color:red;'>Prediction failed.</span>",
                severity: "",
                probability: ""
            });
        });
    });
});
