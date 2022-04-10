## To Run:

- Install virtualenv
  `pip install virtualenv`
- Create the virtual environment named "env" (Windows):
  `python -m venv env`
- Add the path to the git ignore file (optional):
  `echo env/ >> .gitignore`
- Activate the virtual env:
  `source env/Scripts/activate`
- Install dependencies:
  `pip install pymongo pymongo[srv] fastapi uvicorn python-dotenv`
- Run:
  `uvicorn index:app --reload` or `python -m uvicorn index:app --reload`
