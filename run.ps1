Start-Process powershell -ArgumentList "uvicorn app.main:app --reload"
Start-Sleep -Seconds 3
streamlit run frontend/ui.py --server.port 8502
