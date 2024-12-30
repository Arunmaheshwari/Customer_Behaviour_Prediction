## Predicting how a customer will feel about a product before they even ordered it






------------------------------------About Dataset------------------------------------
Customers Dataset
This dataset has information about the customer and its location. Use it to identify unique customers in the orders dataset and to find the orders delivery location.

At our system each order is assigned to a unique customer_id. This means that the same customer will get different ids for different orders. The purpose of having a customer_unique_id on the dataset is to allow you to identify customers that made repurchases at the store. Otherwise you would find that each order had a different customer associated with.






Problem statement: For a given customer's historical data, we are tasked to predict the review score for the next order or purchase. We will be using the Brazilian E-Commerce Public Dataset by Olist. This dataset has information on 100,000 orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allow viewing charges from various dimensions: from order status, price, payment, freight performance to customer location, product attributes and finally, reviews written by customers. The objective here is to predict the customer satisfaction score for a given order based on features like order status, price, payment, etc. In order to achieve this in a real-world scenario, we will be using ZenML to build a production-ready pipeline to predict the customer satisfaction score for the next order or purchase.





I am using Zenml for visualizing my all steps.
if i want to run use zenml so i need...

   pip install "zenml[server]" 

and then
   
   zenml init  

after installing, now i want to run my pipeline, i will use this....
   
   python run_pipeline.py      

and then i also need to run this command as well...
   
   zenml login --local --blocking

this command will ensure that zenml will also run in my system as well.
typically zenml does not run on window system, that's why we are using blocking.



If i want to see my model and everything in mlflow, so i have to use these command...
'''bash
           python run_pipeline.py

from this command i will be getting url and then i need to run this command with this url
           
            mlflow ui --backend-store-uri "file:C:\Users\Hare Krishna\AppData\Roaming\zenml\local_stores\941ab80c-7c9b-408b-beb3-d0132f0adaf2\mlruns"

whatever i have inside this "" is the url.