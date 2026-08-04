# Pandas Playground

A very small learning project with:

- a Python backend using pandas;
- a frontend made with plain HTML, CSS, and JavaScript;
- a sample CSV and five beginner-friendly pandas operations.

## Run it

Create a virtual environment and install pandas:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If Ubuntu/Debian reports that `ensurepip` is unavailable, install virtual
environment support first:

```bash
sudo apt install python3-venv
```

Then run the virtual-environment commands above again.

Start the app:

```bash
python app.py
```

Then open <http://127.0.0.1:8000>.

## Practice ideas

1. Add a row or a column to `data/sales.csv`.
2. Change a filter in `try_pandas.py`.
3. Add a new option to the HTML and a matching operation in Python.
4. Try `df.head()`, `df.describe()`, or `df.dropna()`.

The browser calls `/api/data`. Python reads the CSV with pandas, performs the
selected operation, and sends JSON back to JavaScript, which creates the table.
The pandas exercises live in `try_pandas.py`; `app.py` contains the web server
and everything needed to run the app.
