const form = document.getElementById("predictionForm");
const result = document.getElementById("result");

const fields = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"];

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const data = Object.fromEntries(fields.map((field) => [
        field,
        Number(document.getElementById(field).value)
    ]));

    if (Object.values(data).some((value) => !Number.isFinite(value))) {
        result.textContent = "Please enter valid numbers in every field.";
        return;
    }

    result.innerHTML = "Predicting...";

    try {

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const output = await response.json();

        if (response.ok) {
            result.replaceChildren();
            const heading = document.createElement("h2");
            heading.textContent = "Recommended Crop";
            const crop = document.createElement("p");
            crop.textContent = output.crop;
            result.append(heading, crop);
        } else {
            result.textContent = `Error: ${output.error || "Prediction failed."}`;
        }

    } catch (error) {

        result.textContent = "Unable to connect to the server.";

        console.error(error);
    }
});