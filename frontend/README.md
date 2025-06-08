to run frontend:
cd frontend
python3.13 -m venv .venv
source .venv/bin/activate             # or venv\Scripts\activate on Windows
# make sure to use python 3.11+
pip install -r requirements.txt      # installing dependencies

python main.py                       # launching gui


deactivate       # deactivates venv