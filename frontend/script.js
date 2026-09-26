const form = document.getElementById("predictionForm");
const button = document.getElementById("predictButton");
const buttonText = document.getElementById("buttonText");
const result = document.getElementById("result");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const data = {
        N: parseFloat(document.getElementById("N").value),
        P: parseFloat(document.getElementById("P").value),
        K: parseFloat(document.getElementById("K").value),
        temperature: parseFloat(document.getElementById("temperature").value),
        humidity: parseFloat(document.getElementById("humidity").value),
        ph: parseFloat(document.getElementById("ph").value),
        rainfall: parseFloat(document.getElementById("rainfall").value)
    };

    button.disabled = true;
    buttonText.textContent = "Predicting...";

    result.classList.add("hidden");

    try {

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const output = await response.json();

        if (!response.ok) {
            throw new Error(output.error || "Prediction failed");
        }

        result.innerHTML = `
            <h2>Recommended Crop</h2>
            <div class="crop-name">${output.crop}</div>
            <p>Based on the soil and environmental conditions provided.</p>
        `;

        result.classList.remove("hidden");

    } catch (error) {

        result.innerHTML = `
            <h2>Something went wrong</h2>
            <p>${error.message}</p>
        `;

        result.classList.remove("hidden");

        console.error("Prediction error:", error);

    } finally {

        button.disabled = false;
        buttonText.textContent = "Recommend Crop";

    }
});