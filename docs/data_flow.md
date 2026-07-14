# Data Flow

1. Driver information is sent from Postman.

2. n8n receives the request through a Webhook.

3. n8n forwards the request to FastAPI.

4. FastAPI loads the machine learning model.

5. The model predicts whether the driver is risky or safe.

6. FastAPI calculates a risk score.

7. The prediction and score are stored in SQLite.

8. Streamlit reads the database and displays the dashboard.