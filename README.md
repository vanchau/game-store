# wsd-game-store

CS-C3170 Web Software Development: Course Project (2019-2020)   
Online game store for JavaScript games.

**FINAL SUBMISSION REPORT**
-------------------------------------------------------------------------------------------------------------------------------

**MEMBERS**
 
Minna Laitinen 561578<br/>
Minna Seppälä 564177<br/>
Van Chau 585392

-------------------------------------------------------------------------------------------------------------------------------

**IMPLEMENTED FEATURES**

**Minimum functional requirements**

1. Register as a player and developer :heavy_check_mark:
2. As a developer: add games to their inventory, see list of game sales :heavy_check_mark:
3. As a player: buy games, play games, see game high scores and record their score to it :heavy_check_mark:

Non-registered users can only browse the games and view specific game pages with restricted view (Buy button
instead of game, only global high scores). Registered users can both play and add games. If user has 
added games, they will see more functionalities in those game views (managing, statistics).

**Authentication (mandatory, 100-200 points)**
1. Login, logout and register. :heavy_check_mark:
2. Use Django Auth :heavy_check_mark:
3. Email validation :x:

We think we successfully implemented these features with excellent quality and 
purposeful use of the framework (Django auth, forms, etc.), achieving e.g reusability and modularity. As email validation is missing:  
**--> Self-evaluation: 100 points**

**Basic player functionalities (mandatory, 100-300 points)**
1. Buy games, payment is handled by the course’s mockup payment service: https://tilkkutakki.cs.aalto.fi/payments/ :heavy_check_mark:
2. Play games. :heavy_check_mark:
3. Security restrictions, e.g. player is only allowed to play the games they’ve purchased :heavy_check_mark:
4. Also consider how your players will find games (are they in a category, is there a search functionality?) :heavy_check_mark:

(2,3) To play a game, user has to buy it. If user is the developer of the game, it is playable without buying.  
(4) All existing games in the store can be searched from the home page by anyone. Additionally, users can search
their own bought games or published games. The search returns games if the query matches in any way with game title or category.

We think we succeeded in these features too as everything got implemented and work as intended. The framework
was used purposefully here as well (Model-Template-View separation of concern) with good practices, e.g., DRY
was enforced with extending templates and the same search works for categories and game titles. Although we 
had some struggles with template-view communication, we think that in the end we managed to produce a great solution.
**--> Self-evaluation: 300 points**

**Basic developer functionalities (mandatory 100-200 points)**
1. Add a game (URL) and set price for that game and manage that game (remove, modify) :heavy_check_mark:
2. Basic game inventory and sales statistics (how many of the developers' games have been bought and when) :heavy_check_mark:
3. Security restrictions, e.g. developers are only allowed to modify/add/etc. 
   their own games, developer can only add games to their own inventory, etc. :heavy_check_mark:

(1) User can manage (edit, remove) their published games from the game speficic pages. The options are only visible
if the user is the publisher.  
(2) The publisher of a game can see sales statistic from the game page.

We think these features are also successfully implemented, sharing the same explanations as above (purposeful use
of the Django framework through models, views and templates). We like our simple solution how everyone
can be a developer but only users who have actually published a game see the extra features, which are all implemented.
With each game having a foreign key to its publisher, they can only be managed by their publisher. Additionally,
each user has their own inventory of their published game.  
**--> Self-evaluation: 200 points**

**Game/service interaction (mandatory 100-200 points)**

1. When player has finished playing a game (or presses submit score), the game sends a postMessage to the parent window
   containing the current score. This score must be recorded to the player's scores and to the global high score list for that game.
   :heavy_check_mark:
2. Messages from service to the game must be implemented as well :heavy_check_mark:

(1,2) All five message types (SCORE, SAVE, LOAD_REQUEST, LOAD, ERROR and SETTING) are supported, i.e.,
interaction goes both ways.

In the beginning we had some difficulties with data formats in the communication between models, views and templates (and the game
itself) but managed to successfully implement a game-service interaction that goes both ways. We think Django features
were used versatilely and accordingly in these processes.  
**--> Self-evaluation: 200 points**

**Quality of Work (mandatory 0-100 points)**

1. Quality of code (structure of the application, comments) :heavy_check_mark:
2. Purposeful use of framework (Don't-Repeat-Yourself principle, Model-View-Template separation of concerns) :heavy_check_mark:
3. User experience (styling, interaction) :heavy_check_mark:
4. Meaningful testing :heavy_check_mark:

(1,2) Code is commented. Lint is used. Applications and their related files are organized systematically (modularity).
Reusability and DRYness achieved e.g. with extending templates (template blocks) and generic views. Models designed to be as simple as possible with
no unnecessary fields.    
(3) Bootstrap used for clean styling. Straightforward UI for ensuring a nice user experience.  
(4) Only manual testing done to verify that everyting works smoothly without bugs or crashes.  

Overall, Django's features are used versatilely to ensure mainly reusability and modularity. Thorough manual testing was
done throughout the project. However, security flaws were not investigated intensively.  
**--> Self-evaluation: 90 points**

**Non-functional requirements (mandatory 0-200 points)**
1. Project plan (part of final grading, max. 50 points) :heavy_check_mark:
2. Overall documentation, demo, teamwork, and project management as seen from the history of your GitLab project
   (and possible other sources that you submit in your final report). :heavy_check_mark:

(1) [Project plan](#projectplan) is found below in this same README. We think that the plan was very good to get us started even though
not everything was done according to it, which we think is totally acceptable. Especially with no prior experience on these
technologies, we think that the most important purpose of this project plan was to get us started and not set everything in stone.
As we received no feedback on the project plan, we self-evaluate 50 points based on the mentioned points.

(2) Basic good git principles were used throughout the project (branches, etc.). Kept track of implemented features in README
and added developer notes for other team members. Clear documentation as seen from this file.  
**--> Self-evaluation: 200 points**

**MORE FEATURES**

**Save/load and resolution feature (0-100 points)**
1. The service supports saving and loading for games with the simple message protocol described in Game Developer Information :heavy_check_mark:

(1) All five message types are implemented. User can SAVE and LOAD. If user has no save data,
ERROR message type is returned to the game. Resolution of the iframe is fetched from the message with type SETTING.

Same points as in "Game/Service interaction".  
**--> Self-evaluation: 100 points**

**Mobile Friendly (0-50 points)**
1. Attention is paid to usability on both traditional computers and mobile devices (smart phones/tablets) :heavy_check_mark:
2. It works with devices with varying screen width and is usable with touch based devices. :heavy_check_mark:

(1,2) The site runs well both on mobile and desktop due to Bootstrap. Looks nice and works nicely.  
**--> Self-evaluation: 50 points**

**Own game (0-100 points)**

1. Develop a simple game in JavaScript that communicates with the service (at least high score, save, load) :heavy_check_mark:
2. You can host the game as a static file in your Django project or elsewhere. But you should include it in your repository. :heavy_check_mark:

(1,2) Own game (html file) added to root. Hosted elsewhere and url added to game store. Coded in a rush so
quality is not the best but supports all required features. Game name "OWN GAME" in store.
**--> Self-evaluation: 80 points**
-------------------------------------------------------------------------------------------------------------------------------
**WORK DIVISION**

We started the project together with a design meeting and project setup. From there, we implemented
features with our own schedules by doing what was still needed to be done. Lots of pair coding was done
during the project. Rough division of work:

Minna Laitinen: authentication, basic player functionalities, basic developer functionalities  
Minna Seppälä: basic player functionalities, game/service interaction, save/load and resolution feature  
Van Chau: basic player functionalities, game/service interaction, mobile friendly  

Overall, everyone was involded in all parts of the project (backend, frontend, design).

-------------------------------------------------------------------------------------------------------------------------------
**INSTRUCTIONS**

[LINK TO THE PROJECT](https://secret-journey-02861.herokuapp.com/)

Admin account (same as other users but can access django admin site)  
username: admin  
password: admin

1. As a non-registered user, you can browse the store by scrolling or using the search bar
   which finds a full or partial match with your query string and game titles or categories. Game pages can be accessed 
   with a limited view (hidden game, global high scores) For more functionalities, you have to signup or login from the header.
2. As a registered user, you can buy the game and play. The game is now in your purchased games, which can be seen by clicking "Play
   games" in the home page's jumbotron.
3. As a registered user, you can add a game from the header. Now in the game page you can edit or delete the game and view 
   the sales statistics of that game. All your added games can be viewed from "My inventory" in home page.

For instructions on how to run the project locally, [see developer notes](#dev)

-------------------------------------------------------------------------------------------------------------------------------
<a name="projectplan"></a>
**PROJECT PLAN**
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
X search functionality (how users can find games)

BASIC DEVELOPER FUNCTIONALITIES (mandatory)

X Add game URL, set price, and manage game (remove, modify)
X Basic game inventory and sales statistics 
X Developers are only allowed to modify/add/etc. their own games 

GAME/SERVICE INTERACTION (mandatory)

X Save player's scores and display global high scores 
X Messages from service to the game

QUALITY OF WORK (mandatory)

X Comments, architecture
X Purposeful use of framework (DRY principle, Model-View-Template separation)
X User experience (styling, interaction)
X Testing (manual is enough -Piazza)

NON-FUNCTIONAL REQUIREMENTS (mandatory)

X Project plan
X Overall documentation, demo, teamwork, project management

SAVE/LOAD AND RESOLUTION FEATURE (optional)

_ The game supports saving/loading of the games with simple message protocol

3RD PARTY LOGIN (optional)

_ Support for OpenID, gmail, or Facebook login

RESTFUL API (optional)

_ Design and implementation of RESTful API to the service

OWN GAME (optional)

_ Simple game in JavaScript that communicated with the service

MOBILE FRIENDLY (optional)

X Usability on both traditional computers and mobile devices

SOCIAL MEDIA SHARING (optional)

_ Enable sharing games in social media site (Facebook, Twitter, Google+, etc.)

-------------------------------------------------------------------------------------------------------------------------------
**DEVELOPER NOTES**

How to get rid of "Class has no objects member" error caused by pylint
1. pip install pylint-django
2. In VSC go to settings (File > Preferences > Settings > Extensions > Django configuration and open json file)
3. Insert {"python.linting.pylintArgs": ["--load-plugins=pylint_django"],}

<a name="dev"></a>
How to run the project locally
1. Clone the project to your computer
2. Create python virtual environment and install Django (remember to update pip)
3. Install dependencies from requirements.txt with the command "pip install -r requirements.txt"
4. Migrate models ("python manage.py migrate", you might have to first run the command makemigration)
5. Run local server with the command "python manage.py runserver"