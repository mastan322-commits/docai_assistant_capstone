Start-Process powershell -ArgumentList "uvicorn app.api.main:app --reload --port 8080"
Start-Sleep -Seconds 3
streamlit run frontend/ui.py --server.port 8502
