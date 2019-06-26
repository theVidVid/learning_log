# learning_log
Django web app that allows users to log the topics they're interested in and make journal entries as they learn about each topic.

The app allows users to create new topics, followed by a new entry related to that topic, and the ability to edit an existing entry.

All topics and posts are protected by the django @login_required decorator. Clicking on the topics link on the navbar while not logged in or register will direct the user to the login page.

The app has an admin-panel powered by Django, where the created superuser can add, modify, or delete users, topics and entries.

The app was styled using Bootstrap4. 

# Index page
![index_page](https://user-images.githubusercontent.com/35820755/60214138-c5b3a580-9819-11e9-89c3-1bc2309b4b14.png)
