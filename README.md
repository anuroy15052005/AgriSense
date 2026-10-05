# 🌱 AgriSense

### Smart Crop Recommendation using Machine Learning

AgriSense is a machine learning web application that recommends a suitable crop based on soil and environmental conditions.

Enter the values for **N, P, K, temperature, humidity, pH, and rainfall**, and AgriSense predicts the crop that best matches the given conditions.

---

## ✨ Highlights

- 🌾 **22 crop classes** supported
- 🤖 **Random Forest** based classification
- 🔄 **5-Fold Cross-Validation**
- ⚙️ Hyperparameter tuning
- 📊 Feature importance & ablation analysis
- 🌐 Flask REST API
- 💻 Interactive web interface
- 🐳 Dockerized application
- 🚀 Deployment-ready

---

## 📸 How It Works

```text
        Soil & Weather Data
                │
                ▼
      ┌─────────────────────┐
      │    AgriSense        │
      │   Web Interface     │
      └──────────┬──────────┘
                 │
                 ▼
          Flask REST API
                 │
                 ▼
       Random Forest Model
                 │
                 ▼
        Recommended Crop 🌱