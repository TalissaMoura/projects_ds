# NewsApp <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/regular/newspaper.svg" width="50" height="50">

<p align="left">
    <img src="https://img.shields.io/static/v1?label=Project Status&message=complete&color=green"/>
   
</p>

# About
NewsApp is a simple website that load the news  stored in a database. I made this because I wanted to learn how ML models are applied in web applications (or, better, how ML models are *deployed*). 

The news is shown in cards with the title, description, date and category. The goal of our model is to predict the category of news from their title. 
 

## Technologies used
<p align="left">
<a href="">
<img src="https://img.shields.io/static/v1?label=Languages&message=Python and JavaScript&color=blue"/>
</a> 
<a>
<img src="https://img.shields.io/static/v1?label=Database&message=MongoDB&color=blue&logo="/>
</a>
</p>

# Project Overview

As this project is a simple web application, the following steps were taken:
<ol>
<li><strong>About the frontend</strong>:</li>

To keep this page simple, it has a CardView design built with HTML, JS, and Bootstrap.

JS is used to control the number of items loaded on the page and what information to put in the tags in the HTML file. This is done by the loadItems function. If we receive an empty response, no more items are loaded.

Another thing to add is that this page has infinite scrolling. New news is loaded every time the user hits the end of the page. For this, we're using the IntersectionObserver class, and you can find the implementation in the templates folder at the index.html file.
    
 <li><strong>About the backend:</strong></li>

To create the routes, comunicate to database and deploy the model we are using the Flask library from Python. Here, we have some definitions:
    
* **Database used**: We're using the MongoDB database as it's free and more flexible to save the news informations.
 
* **The [routes.py](\news\routes.py) file**: In this file, we have two functions the first is `home_page` that loads our `index.html` file and the other is the `more_page` function that grabs more news that are stored in our database. All the news is returned as JSON object and their information is treated by the `loadItems` function defined at `index.html`. Here, also, is where we apply our ML pipeline to predict the category of a news from their title. First, we need to encode our title by using the `NewsTitleEncoder` class, then, we load our model to predict the category from this vector.
    
* **The [models.py](\news\models.py) file**: Here we define the class `NewsTitleEncoder` which has methods to convert the text into vector. They are the same functions used at the data preprocessing step explained below. 

    
<li><strong>About the model:</strong></li>

* **Dataset used**: The dataset used is the <a href="https://www.kaggle.com/datasets/rmisra/news-category-dataset">News Category Dataset</a> which contains around 210k news headlines from 2012 to 2022 from HuffPost.

* **Data preprocessing**: To use text for ML algorithms we need to convert our text into vectors. But, before this the data is prepared by following this steps: first, we clean the text by removing punctuations, repetitions and contractions, after this, our text is convert to tokens (and every token is stemming by SnowballStemmer), then, we apply the tf-idf vectorizer,finally, to reduce the dimensionality of our vectors we use PCA

* **Model definition and training**: Our dataset have for about 20k news, divide by 5 categories: business, art, education, science and sports. The training data contains 80% of all data, the rest is test data. As we have a good amount of data and small categories a simple logistic regression gives good results. So our model estimates what category is more likely to occur based on probabilities. 

* **Results:**  For training data or best model has 85% of accuracy, 84% of f1-score macro avg and 84% of f1-score weighted avg. At test data, it achieved 80% of accuracy, 78% of f1-score macro avg and 80% of f1-score weighted avg. 
</li>

</ul>


    
    
   
</ol>



# Results

Here is the final result!

![Final Result!](https://github.com/TalissaMoura/projects_ds/blob/main/newsApp/images/newsapp.gif)

## If you want to execute this project:
- You need to create a virtual environment and download the libraries listed in the `requirements.txt` file. The python version used is `3.10.2`
- Run the notebook `news_category_analysis.ipynb` to get the model files to be used and the `selected_news.csv` file
to be used in the `newsdatabase.ipynb`.
- Run the notebook `newsdatabase.ipynb` to add the selected news to your [mongodb cluster](https://www.mongodb.com/basics/clusters/mongodb-cluster-setup). Remember to change the dir to point where the `selected_news.csv` is saved. 
- To run the dockerfile correctly you"ll need to change the dir of your [secrets](https://docs.docker.com/compose/use-secrets/) in the `compose.yaml` file.
- With all the previous steps complete you can run `docker compose up -d` and access `localhost:5000` to see the application.
As everything is setup, for now, you only need to execute this command to run the application.  