**Topic 1- Media Monitor**: \
This is a **Machine Learning Based Model** that is used to detect the public sentiment by using **Natural Language Processing** about any product or brand we may find on the web.
The software works by first calling a Google search API when we search an item in our website and it searches and collects data of first indexed page in google search engine.
After the website is gathered from google, we input it into the Machine Learning Model.
By using Beautiful Soup, a library in python, we first scrap out the Website into HTML raw file and we then seperate out review section to put it in a sentence and further perform sentiment analysis on it.
Based on the analysis, the ML model predicts if the product or brand has Positive, Negative or Neutral reviews alongwith the trustworthiness of the brand.
We have integrated our model into a simple website using Django API, HTML, CSS and Javascript.
![image](https://user-images.githubusercontent.com/89735261/189471566-df7069ac-a538-46b2-9868-1e34a0570ecc.png)
This is our Front-end interface where you need to input a product name or a brand name.
![image](https://user-images.githubusercontent.com/89735261/189471625-32318ef5-7c86-486c-ad1d-ace2c3d1dfa2.png)
This is our backend interface where the Machine Learning model works and executes the sentiment analysis using **Natural Language Processing**
**INSTRUCTIONS OF USE**\
DOWNLOAD DJANGO BY RUNNING "pip install Django==4.1.1" in terminal. \
TO USE THIS U NEED TO FORK THE CONTENT OR DOWNLOAD IT IN A FOLDER. \
OPEN THE PROJECT FILE AND OPEN TERMINAL IN THAT FILE. \
run the following code to start a server on local host: \
python manage.py runserver\
click on the link generated to view the project.\
The creators of this project are:
1. Adrita Chakrabarti [it2022/b09][ac.adrita2003@gmail.com]
2. Shrayanendra Nath Mandal [cse2020/092] [shrayanmandal21@gmail.com]

Video Link - [https://www.youtube.com/watch?v=OWa9T2wjoXM]
