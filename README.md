# AgriSense

## Run locally

```powershell
python -m pip install -r requirements.txt
python train_model.py
python app.py
```

Open `http://127.0.0.1:5000` in a browser.

The API accepts a JSON `POST` request at `/predict` with `N`, `P`, `K`,
`temperature`, `humidity`, `ph`, and `rainfall` fields.