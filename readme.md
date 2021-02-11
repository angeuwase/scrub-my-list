# Project Name: Scrub My List

## **Problem**
Email marketing is the best digital marketing tool for engaging with prospective customers and selling things online. However, building and maintaining an email list takes a lot of time and effort. Some companies build their email lists over time while others simply buy it. Regardless of the source of their email lists, email marketers all share the same  quality issues associated with them, such as incomplete or missing data, invalid email addresses, inactive email addresses, to name a few. There are several companies that provide email validation services, but few offer email marketers analytics regarding the health of their email lists.  

## **Solution and Impact**
Scrub My List utilises the Mailboxvalidator API to not only provide email validation services, but also provide actionable insight into the health of the email lists. By building this application, we will be able to ensure that email marketers have email lists that contain valid, active email addresses that are guaranteed not to bounce back, which will reduce their bounce rates and improve their client engagement rates. Email marketers will also be able to determine the reliability of their email list sources, among other things, from the actionable insight we provide.   

## **App architecture**
-This application will consist of a python flask back-end and html/css front-end.  
-The backend will utilise the core flask functionality of routes, jinja templates and blueprints. 
-It will also implement flask features such as sessions, logging, flash messaging. 
-The relational database management system used will be SQLite during development and postgreSQL during production.    
-The email validation service will be built to utilize the MailBoxValidator API.  
-The app is designed for web only, so it is not optimised for mobile. Future improvements will include mobile responsiveness.  
-The app will be developed using a test-driven development approach.  

## **Key User Stories**
1. As an email marketer, I want to be able to register to use the app, and be able to sign in to my account.   
2. As an email marketer, I want to be able to submit a csv or text file of email addresses that I want cleaned and analysed.   
3. As an email marketer, I want to be able to view all the email lists I have uploaded, and also be able to delete ones I no longer want to see on my account.   
4. As an email marketer, I want to be able to view the analytical data regarding the health and makeup of my mailing list.   
5. As an email marketer, I want to be able to download a sanitized copy of any of my mailing lists as a csv or text file.   