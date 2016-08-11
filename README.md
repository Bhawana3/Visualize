A Flask Application for Hotel Reviews
=====================================
An application to visualize hotel review data's sentiments in pie chart format.

The source code for the Hotel Reviews Application with Flask and MongoEngine.

Installation
------------

You need to have python-3.5 and mongodb-3.2.4 installed on your machine.

1.Install python  pip <br />
2.Install the required dependencies: <br />
3.pip install -r requirements.txt <br />

Import data into mongodb:

```
sudo mongoimport --db survaider_task --collection relation --drop --file /survaider_task/survaider/relation.json --jsonArray
sudo mongoimport --db survaider_task --collection reviews --drop --file /survaider_task/survaider/reviews.json --jsonArray
```

Running the app:
Inside the survaider directory

```python
python manage.py runserver
```

Goto: [http://localhost:5000](http://localhost:5000)
