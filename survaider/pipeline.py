pipeline = [
	{'$unwind':'$units'},
	{'$project':{'units':1,'parent':1}},
	{'$lookup':{'from':"reviews",'localField':"units.property_id",'foreignField':"property_id",'as':"result"}},
	{'$unwind':"$result"},
	{'$group':
		{'_id':{'unit':"$units.name",'chain':"$parent.name"},
		'reviews':{'$push':"$result.review"},
		'positive':{'$sum':{'$cond':{'if':{'$eq':["$result.sentiment","Positive"]},'then':1,'else':0 }}},
		'negative':{'$sum':{'$cond':{'if':{'$eq':["$result.sentiment","Negative"]},'then':1,'else':0 }}},
		'neutral':{'$sum':{'$cond':{'if':{'$eq':["$result.sentiment","Neutral"]},'then':1,'else':0 }}}}},
	{'$project':{'_id':1,'positive':1,'negative':1,'neutral':1,'reviews':{'$slice':["$reviews",5]}}}
]
