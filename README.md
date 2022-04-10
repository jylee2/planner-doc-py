## To Run:

- Install virtualenv
  `pip install virtualenv`
- Create the virtual environment named "env":
  `python -m venv env`
- Add the path to the git ignore file (optional):
  `echo env/ >> .gitignore`
- Activate the virtual env:
  `source env/Scripts/activate`
- Install dependencies:
  `pip install pymongo fastapi uvicorn python-decouple`
- For mongo:
  `pip3 install 'pymongo[srv]'`
- Run:
  `uvicorn index:app --reload`
