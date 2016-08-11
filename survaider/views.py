from flask import jsonify,Blueprint,render_template
from flask.views import MethodView
from survaider.models import Hotels,Relation,Reviews
from pipeline import pipeline

api = Blueprint("api",__name__,template_folder='static')

class ListView(MethodView):

    def get(self):
        return render_template('index.html')

class DetailView(MethodView):

    def get(self):
        reviews_list = []
        all_hotel_reviews = Relation._get_collection().aggregate(pipeline)
        for review in all_hotel_reviews:
            reviews_list.append(review)

        return jsonify({'data':reviews_list})

# Register the urls
api.add_url_rule('/', view_func=ListView.as_view('list'))
api.add_url_rule('/hotel/', view_func=DetailView.as_view('detail'))
