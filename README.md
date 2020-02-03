# wsd-game-store

Online game store for JavaScript games.

**PROJECT PLAN**
-------------------------------------------------------------------------------------------------------------------------------
 
**MEMBERS**
 
Minna Laitinen 561578<br/>
Minna Seppälä 564177<br/>
Van Chau 585392
 
-------------------------------------------------------------------------------------------------------------------------------
 
**FEATURES**
 
Our plan is to implement all the mandatory features including authentication, basic player/developer functionalities, game/service interaction, etc., in our project. The project will have a RESTful API, save/load features, and possibly our own game, if the schedule allows. 
 
Brief description of each feature (how we plan to implement)

Authentication → Authentication (login, logout, sign up) will be done using Django auth. The role of a player and a developer will not be differentiated, meaning that there won't be separate accounts for the two roles. All users can thus be both player and developer, depending on how they want to use the service. If there is enough time, email feature will be added using Django’s mail module.

Basic player functionalities → Players will only have the rights to play the games that they have purchased -- this will be done via a Purchase model, which instances will tell who have paid for which games. For actual process of purchasing, the mockup payment service offered by the course will be used. Players will be able to find games by scrolling down the games list in the home page, or (if there is time to implement) by searching for specific ones via a search bar.

Basic developer functionalities → Developer functionalities will contain components such as the ability to add games and managing the games in the developer’s inventory. The database will provide sales statistics as well as a list of games developed by the users, and restrict access so that only the developer/publisher of a game can edit, delete, or view sales info.

Game/service interaction → All communication between the game and the service will be handled via the window.postMessage() method, which will enable sending messages between the two platforms.

Save/load feature → The save/load feature can be implemented by saving all the necessary player data in a game into a JSON format, which will then be stored in the database. When the player accesses the game again, a message will pop up to ask whether the player wishes to continue playing from the saved data or start a new game. 

RESTful API → RESTful API will be used for accessing the database, be it for the purpose of purchasing games, retrieving saved game data, logging in to the service, etc.

-----------------------------------------------------------------------------------------------------
--------------------------
 
**GENERAL ARCHITECTURE**

Django project: gameproject
Core of the entire system. Contains essential files such as settings.py and urls.py.

Django applications: gamestore and accounts. "Accounts" contains views and templates relevant to the authentication process. Gamestore is the meat and potatoes of the entire game service - this is where all the central models, views, and templates, are defined.


-------------------------------------------------------------------------------------------------------------------------------
 
**MODELS AND VIEWS**
 
The project will have three custom models in addition to the User model provided by Django: Game, Purchase, and Score models. Since Django’s User model provides all the necessary fields such as  username, password, and email, we concluded it not necessary to create an augmented User model for the purpose of this game service, although that was the original plan. The Purchase model will contain all information relevant to the context of game purchasing: price, game id, player id, pid (pk), purchased time, and purchased status. Score model will contain fields such as player id, game id, score, etc.
 
As for views, there will be home, game_view, my_games, statistics, and login, to begin with. Home view will serve as the home page of the service, displaying popular games and high scores. In game_view, a player can view game details or play depending on whether they have purchased the game or not. my_games will display a list of games that a player has purchased. Statistics view will display sales statistics of the games to the developers. Finally, there will also need to be some form of a login view to handle user registration, login, and logout features. 
 
-------------------------------------------------------------------------------------------------------------------------------
 
**TECHNOLOGIES**
 
The project will be implemented using Django framework, JavaScript libraries, and possibly jQuery. Django will be used for the development of both the client side and the server side. For styling, Bootstrap seems like a logical choice for the time being. The final product will be deployed to Heroku. 
 
-------------------------------------------------------------------------------------------------------------------------------
 
**SCHEDULE**
 
All communication will for the most part take place in Telegram, but we will also try to arrange a meeting every one to two weeks. Version management will be done via Version Aalto.

Below is a brief estimation of the overall schedule:

7.1 Discussing and dividing tasks between the team members

8.1-17.1 Authentication and basic developer/player functionalities

18.1-25.1 Continuing to work on the basic functionalities as well as game/service interaction

26.1-7.2 RESTful API and save/load features

8.2-14.2 Updating project plan and documentation for submission

-------------------------------------------------------------------------------------------------------------------------------
 
**IMPLEMENTED FEATURES**

X = completed
O = under implementation
_ = pending

AUTHENTICATION (mandatory)

X login, logout, and sign up
_ email validation

BASIC PLAYER FUNCTIONALITIES (mandatory)

X purchase games with mockup payment service
X users can play games
X players are only allowed to play games they have purchased
_ search functionality (how users can find games)

BASIC DEVELOPER FUNCTIONALITIES (mandatory)

X Add game URL, set price, and manage game (remove, modify)
X Basic game inventory and sales statistics 
X Developers are only allowed to modify/add/etc. their own games 

GAME/SERVICE INTERACTION (mandatory)

_ Save player's scores and display global high scores 
_ Messages from service to the game

QUALITY OF WORK (mandatory)

O Comments, architecture
_ Purposeful use of framework (DRY principle, Model-View-Template separation)
O User experience (styling, interaction)
_ Testing

NON-FUNCTIONAL REQUIREMENTS (mandatory)

O Project plan
O Overall documentation, demo, teamwork, project management

SAVE/LOAD AND RESOLUTION FEATURE (optional)

_ The game supports saving/loading of the games with simple message protocol

3RD PARTY LOGIN (optional)

_ Support for OpenID, gmail, or Facebook login

RESTFUL API (optional)

_ Design and implementation of RESTful API to the service

OWN GAME (optional)

_ Simple game in JavaScript that communicated with the service

MOBILE FRIENDLY (optional)

U Usability on both traditional computers and mobile devices

SOCIAL MEDIA SHARING (optional)

_ Enable sharing games in social media site (Facebook, Twitter, Google+, etc.)

-------------------------------------------------------------------------------------------------------------------------------

DEVELOPER NOTES

How to get rid of "Class has no objects member" error caused by pylint
1. pip install pylint-django
2. In VSC go to settings (File > Preferences > Settings > Extensions > Django configuration and open json file)
3. Insert {"python.linting.pylintArgs": ["--load-plugins=pylint_django"],}


