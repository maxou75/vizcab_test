# Vizcab backend challenge

## Requirements
- Python >= 3.12.2
- Django >= 5.0.4

## Installation
Clone the source code project from the Git repository:
```
git clone https://github.com/maxou75/vizcab_test
```

Create a Python environment first:
```
python3 -m venv myenv
```

Then activate the environment:
```
source myenv/bin/activate
```

Then install all the module requirements:
```
pip install -r requirements.txt
```

Start the local server:
```
python manage.py runserver
```

By default, you could access the app thought the Django Rest Framework Admin panel:
http://localhost:8000/total_surface?building_id=0

The API is public, so you don't need any authorization. There are 3 endpoints for this API:
- Total surface: Retrieve the total surface for a building id specified in parameters (ex: http://localhost:8000/total_surface?building_id=0)
- Building usage: Retrieve the usage label for a building id specified in parameters (ex: http://localhost:8000/building_usage?building_id=0)
- Carbon impact: Retrieve the carbon impact value building id specified in parameters (ex: http://localhost:8000/carbon_impact?building_id=0)

In addition, you can manually regenerate API documentation with
```
python ./manage.py spectacular --file schema.yaml --validate
```

Finally, you can run the tests localized in **challenge/tests.py** with:
```
python manage.py test
```