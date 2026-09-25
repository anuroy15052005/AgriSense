const form = document.getElementById('cropForm');
const resultBox = document.getElementById('result');
const cropName = document.getElementById('cropName');
const confidence = document.getElementById('confidence');

const API_URL = 'http://127.0.0.1:8000/predict';

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const payload = {
    N: Number(document.getElementById('N').value),
    P: Number(document.getElementById('P').value),
    K: Number(document.getElementById('K').value),
    temperature: Number(document.getElementById('temperature').value),
    humidity: Number(document.getElementById('humidity').value),
    ph: Number(document.getElementById('ph').value),
    rainfall: Number(document.getElementById('rainfall').value),
  };

  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || 'Prediction failed');
    }

    cropName.textContent = data.crop;
    confidence.textContent = data.confidence;
    resultBox.classList.remove('hidden');
  } catch (error) {
    cropName.textContent = 'Unavailable';
    confidence.textContent = error.message;
    resultBox.classList.remove('hidden');
  }
});
