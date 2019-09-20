To excute the project> instead of runserver here,
we have to manage.py runsslserver 127.0.0.1:8000

Admin login details:-
username:- admin
password :- admintest
Used additional library's
django-allauth > for the api auth and  model and templates for social login's,
django-sslserver > for the https access of the local host for the fb app access.

To access the login in the browser the url is > " https://localhost:8000/ "
you can't loging with 127.0.0.1:8000 u will get below error
Can't load URL: The domain of this URL isn't included in the app's domains. To be able to load this URL, add all domains and sub-domains of your app to the App Domains field in your app settings.
because facebook app doesnt allow to give ip address in App domain.

Right now only default user data will be display
id,first_name,last_name,name,picture

remaining information can be display only app was reviewed, take approximately 5 days for the approval from the date of submission.

