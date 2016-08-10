from flask import jsonify,Blueprint,render_template
from flask.views import MethodView
from survaider.models import Hotels,Relation,Reviews

api = Blueprint("api",__name__,template_folder='static')

class ListView(MethodView):

    def get(self):
        return render_template('index.html')

class DetailView(MethodView):

    def get(self):
        reviews_list = []
        pipeline = [{'$unwind':'$units'},{'$project':{'units':1,'parent':1}},{'$lookup':{'from':"reviews",'localField':"units.property_id",'foreignField':"property_id",'as':"result"}},{'$unwind':"$result"},{'$group':{'_id':{'unit':"$units.name",'chain':"$parent.name"},'reviews':{'$push':"$result.review"},'positive':{'$sum':{'$cond':{'if':{'$eq':["$result.sentiment","Positive"]},'then':1,'else':0 }}},'negative':{'$sum':{'$cond':{'if':{'$eq':["$result.sentiment","Negative"]},'then':1,'else':0 }}},'neutral':{'$sum':{'$cond':{'if':{'$eq':["$result.sentiment","Neutral"]},'then':1,'else':0 }}}}},{'$project':{'_id':1,'positive':1,'negative':1,'neutral':1,'reviews':{'$slice':["$reviews",5]}}}]
        all_hotel_reviews = Relation._get_collection().aggregate(pipeline)
        for review in all_hotel_reviews:
            reviews_list.append(review)

        return jsonify({'data':reviews_list})

# Register the urls
api.add_url_rule('/', view_func=ListView.as_view('list'))
api.add_url_rule('/hotel/', view_func=DetailView.as_view('detail'))
