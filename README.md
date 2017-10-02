# app*o*site
PlayStore app explorer

## Setup

### Pre-requisites

- Python 3.6.x
- virtualenv

### Installation

```
pip install -r requirements.txt
```
```
python manage.py migrate
```
```
python manage.py runserver
```
Then goto http://localhost:8000/

### Style compilation

Make sure you have `node-sass` (`npm i -g node-sass`)

```
node-sass --watch --output-style compressed  appsearch/static/style/appsearch.scss -o appsearch/static/style
```
