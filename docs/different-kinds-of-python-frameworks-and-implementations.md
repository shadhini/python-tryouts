---
icon: list-tree
---

# Different Kinds of Python Frameworks and Implementations

## Python Based Implementations

Python is the <mark style="background-color:blue;">**"Swiss Army Knife"**</mark> of programming because it doesn't just do one thing—it adapts to the shape of the problem you're trying to solve.

<table><thead><tr><th width="118.48046875">Type</th><th width="247.36328125">Best For</th><th width="103.28125">Complexity</th><th>Key Feature</th></tr></thead><tbody><tr><td><strong>Script</strong></td><td>Simple Automation, Utilities</td><td>Very Low</td><td>Single file execution.</td></tr><tr><td><strong>Library</strong></td><td>Shared Logic, Code reuse, Distribution</td><td>Medium</td><td>Versioning and <code>pip</code> installable.</td></tr><tr><td><strong>Flask</strong></td><td>Custom Control, Small-Medium apps, APIs</td><td>Medium</td><td>Minimalist, "un-opinionated."</td></tr><tr><td><strong>FastAPI</strong></td><td>APIs / Performance, Microservices</td><td>Medium</td><td>Auto-documentation and <code>async</code>.</td></tr><tr><td><strong>Django</strong></td><td>Enterprise Web, Large apps, CMS</td><td>High</td><td>Built-in Admin and Security.</td></tr><tr><td><strong>Pipeline</strong></td><td>Data Engineering, Data processing, ETL</td><td>High</td><td>Focus on reliability and retries.</td></tr></tbody></table>

### 1. Standalone Scripts

**Nature**: single-purpose, usually a single `.py` file program, self-contained functionality, linear execution, executed directly (`python script.py`)&#x20;

**Use Cases**: small tasks, quick automation, one-off utilities, data processing, automation tasks

* automating file backups
* scraping a single website
* "one-and-done" data migrations
* quick data munging
* sysadmin tasks
* small prototypes

**Project Structure:**

```
...
├── .env                # Environment variables (API keys)
├── requirements.txt    # Minimal dependencies
└── script.py           # The single file program
```

**Sample Code:**

{% code title="script.py" %}
```py
#!/usr/bin/env python3
"""
script.py - simple file lister
Usage: python script.py /path/to/dir
"""
import sys
from pathlib import Path

def main(path_str: str):
    p = Path(path_str)
    if not p.exists():
        print("Path does not exist:", p)
        return
    for child in p.iterdir():
        print(child.name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <path>")
    else:
        main(sys.argv[1])
```
{% endcode %}



### 2. Python Library / Package

**Nature**: reusable code packaged for distribution, distributed via pip (`wheel`/`sdist`), published to PyPI (Python Package Index), exposes an API for other code, imported by other Python programs

**Use cases**: utility libraries, domain-specific packages, shared code across projects, code reusability, sharing functionality, open-source contributions, internal company tools

**Project Structure:**

```
my_library/
├── src/
│   └── my_library/             # Actual package source code
│       ├── __init__.py         # Makes the directory a package
│       ├── core.py
│       ├── utils.py
│       └── models.py
├── tests/                      # Test suite
│   ├── __init__.py
│   ├── test_core.py
│   └── test_utils.py
├── docs/                       # Documentation (Sphinx or MkDocs)
│   └── index.md
├── .github/                    # CI/CD workflows (GitHub Actions)
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── LICENSE
├── pyproject.toml / setup.py   # Build system & metadata (The heart of the project)
├── requirements.txt
├──  MANIFEST.in
├── README.md
└── setup.cfg                   # Optional (if not using pyproject.toml fully)
```

**Sample Code:**

{% embed url="https://github.com/shadhini/python-tryouts/tree/main/python-library-skeleton" %}



### 3. The Web Trinity: Flask, FastAPI, & Django

These three represent a spectrum from <kbd>"DIY"</kbd> to <kbd>"Everything is provided"</kbd>.

#### A. Flask (The "Micro" Framework)

**Nature**:  minimalist, flexible & extensible (minimal core with many extensions), lightweight WSGI web framework, synchronous by default, template rendering with `Jinja2`, you choose your own database, auth, and validation tools,&#x20;

**Use Cases**: small to medium apps, prototypes, simple APIs, web UIs, when you want total control over the stack

**Project Structure**:

```
flask-app/
├── app/
│   ├── __init__.py
│   ├── routes.py         # URL routes
│   ├── models.py         # Database models
│   ├── forms.py          # WTForms
│   ├── templates/        # HTML templates
│   │   ├── base.html
│   │   └── index.html
│   └── static/           # CSS, JS, images
│       ├── css/
│       └── js/
├── config.py
├── requirements.txt
└── run.py
```

**Sample Code:**

```python
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/api/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        data = request.get_json()
        user = User(username=data['username'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201
    
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/api/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user(user_id):
    user = User.query.get_or_404(user_id)
    
    if request.method == 'GET':
        return jsonify(user.to_dict())
    
    elif request.method == 'PUT':
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        db.session.commit()
        return jsonify(user.to_dict())
    
    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return '', 204

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Notes: in production, run under `Gunicorn` + `workers`.



#### B. FastAPI (The Modern Speedster)

**Nature**: high performance, asynchronous (async/await support — ASGI), web framework for building JSON APIs, built on Python type hints, validation with `Pydantic`, automatically generated OpenAPI docs, modern Python 3.7+ features

**Use Cases**: high-performance backends, RESTful APIs, microservices, ML model serving, Real-time applications

**Project Structure:**

```
fastapi-app/
├── app/
│   ├── __init__.py
│   ├── main.py           # Application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes/       # API routes/endpoints
│   │   │   ├── auth.py
│   │   │   └── users.py
│   ├── models/           # Pydantic models
│   ├── services/         # Business logic
│   ├── core/             # Config, security
│   └── db/               # Database connections
├── tests/
├── requirements.txt
├── .env
└── run.py
```

**Sample Code:**

Run: `uvicorn app.main:app --reload`

```python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="My API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for validation
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

# In-memory database
items_db = []

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# CRUD endpoints
@app.get("/items", response_model=List[Item])
async def get_items():
    return items_db

@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: Item):
    item.id = len(items_db) + 1
    items_db.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            updated_item.id = item_id
            items_db[idx] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(idx)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Notes: use `uvicorn` + `gunicorn/uvicorn workers` for production



#### C. Django (The "Batteries Included" Giant)

**Nature**: batteries-included full-stack framework, opinionated and massive, built-in Admin panel, ORM (Object-Relational Mapping), Authentication out of the box, forms, templating, sessions, migrations built-in, MTV (Model-Template-View) architecture, WSGI application, conventions and scaffolding via django-admin

**Use Cases**: complex, data-heavy sites (Instagram and Pinterest were built on this), enterprise applications, when you need rapid development, apps requiring integrated auth/DB/convention, makes building monoliths easy

**Project Structure:**

```
django-project/
├── myproject/            # Project folder
│   ├── __init__.py
│   ├── settings.py       # Configuration
│   ├── urls.py           # URL routing
│   ├── wsgi.py
│   └── asgi.py
├── apps/                 # Modular "apps"
│   ├── users/         
│   ├── myapp/                # App folder
│   │   ├── migrations/       # Database migrations
│   │   ├── __init__.py
│   │   ├── admin.py          # Admin interface
│   │   ├── apps.py
│   │   ├── models.py         # Database models
│   │   ├── views.py          # View logic
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── templates/        # HTML templates
│   │   └── tests.py
│   └── blog/
├── static/               # Static files
├── media/                # User uploads
├── manage.py             # CLI tool
└── requirements.txt
```

* Run: `python manage.py runserver`
* Notes:&#x20;
  * Django projects often grow larger; use apps to split functionality
  * use migrations, settings per environment, and a WSGI/ASGI server for deployment



### 4. Data Pipelines (ETL)

**Nature**: focused on the flow of data: <kbd>Extract → Transform → Load</kbd> processes

* directed acyclic graph (DAG) of tasks, scheduled/automated jobs, often orchestrated by a scheduler
* data processing workflows
* usually scheduled via tools/frameworks like **`Apache Airflow`** or **`Prefect`**

**Use Cases**: data warehousing, ETL processes, data integration, batch processing/batch workflows, analytics pipelines, periodic data processing, ML pipelines

* syncing a sales database to a data warehouse,  processing 1TB of logs nightly

**Project Structure:**

```
data-pipeline/
├── pipelines/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── dags/                   # Airflow DAGs: Directed Acyclic Graphs (Workflow logic)
│   └── daily_pipeline.py
├── tasks/                  # Individual processing steps
├── config/
│   └── database.yaml
├── sql/                    # Transformation queries
├── tests/
├── requirements.txt
└── run_pipeline.py
```

Notes: use orchestration system (`Airflow`/`Prefect`/`DBT`), containerize tasks, store metadata in databases



### Other

#### Command-line tool (CLI) — argparse or click

**Nature**: Script or package exposing CLI entry points (console\_scripts). Use `click` or `argparse` for arguments.

**Use cases**: developer tools, automation, CLIs used by humans

**Minimal structure**:

```
cli_app/
├── cli_app/
│   ├── init.py
│   └── cli.py
└── pyproject.toml
```

**Example (`click`):**

```python
import click

@click.command()
@click.option("--name", "-n", default="world", help="Name to greet")
def main(name):
    """Simple CLI"""
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    main()
```

`pyproject` should define an entry point so `pip install .` installs `mycli` command.

#### Serverless function (AWS Lambda / GCP Cloud Function)

**Nature**: small function triggered by events, pay-per-execution, limited runtime

**Use cases**: event-driven tasks, webhook handlers, lightweight APIs, glue code

**Notes**:&#x20;

* use `AWS SAM`, `Serverless Framework`, or `Terraform` for infra
* keep cold-starts and package size in mind

#### Jupyter Notebook / Exploratory Data Analysis

**Nature**: interactive notebooks combining code, visualizations, and prose

**Use cases**: data exploration, analysis, ML experiments, sharing reproducible reports.

**Note:**

* use notebooks for iteration; convert to scripts when productionalizing

#### Desktop app (Tkinter / PyQt)

**Nature**: GUI apps packaged for desktop users

**Use cases**: internal tools, simple GUI utilities, specialized domain apps



***

## Which Python? (Python Implementations)

_how_ Python code runs depends on the implementation:

* **`CPython`**: The standard (what you get from python.org).
* **`PyPy`**: A faster version for CPU-heavy tasks using JIT (Just-In-Time) compilation.
* **`Jython`/`IronPython`**: For running Python on the Java or .NET virtual machines.

