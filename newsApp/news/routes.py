from news.models import NewsTitleEncoder
from flask import render_template,request,jsonify,make_response
from news import app,db
import time,pickle,os


posts = db.get_collection("posts")
all_posts = posts.count()
#loading model from pickle
model = pickle.load(open(os.path.join(".","news","model","save","my_model.sav"),"rb"))
quantity = 20


@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/more")
def more_news(): 
    time.sleep(0.2)
    if request.args:
        counter = int(request.args.get("c"))
        #return most recent news
        docs = list(posts.aggregate(pipeline=[{"$sort":{"date":-1}}]))

        ##loading news
        if counter == 0:
          for doc in docs[0:quantity]:
             doc_tokens = NewsTitleEncoder(doc["title"]).process_text()
             new_vec = NewsTitleEncoder.text_to_vec(doc_tokens)
             #return category
             category = model.predict(new_vec)[0]
             if category == 0:
                name_category = "Arts"
                doc["category"]=name_category
             elif category == 1:
                name_category = "Bussiness"
                doc["category"]=name_category
             elif category == 2:
                name_category = "Education"
                doc["category"]=name_category
             elif category == 3:
                name_category = "Science"
                doc["category"]=name_category
             else:
                name_category = "Sports"
                doc["category"]=name_category
          #retuning docs to 0 to quantity
          res = make_response(jsonify(docs[0:quantity]),200)


        elif counter >= all_posts:
            #no more posts to list
            res = make_response(jsonify({}),200)
        else:
            for doc in docs[counter:counter+quantity]:
              doc_tokens = NewsTitleEncoder(doc["title"]).process_text()
              new_vec = NewsTitleEncoder.text_to_vec(doc_tokens)
              #return category
              category = model.predict(new_vec)[0]
              if category == 0:
                 name_category = "Arts"
                 doc["category"]=name_category
              elif category == 1:
                 name_category = "Bussiness"
                 doc["category"]=name_category
              elif category == 2:
                 name_category = "Education"
                 doc["category"]=name_category
              elif category == 3:
                 name_category = "Science"
                 doc["category"]=name_category
              else:
                 name_category = "Sports"
                 doc["category"]=name_category
            #retuning docs from counter to counter+quantity
            res = make_response(jsonify(docs[counter:counter+quantity]),200)
    return res