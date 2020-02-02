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

Authentication → Authentication (login, logout, sign up) will be done using Django auth. This will allow user creation (players and developers) as well as permission handling. If there is enough time, email feature will be added using Django’s mail module.

Basic player functionalities → Players will only have the rights to play the games that they have purchased -- permissions will be stored in the database.  For purchasing the games, the mockup payment service offered by the course will be used. Players can find games by scrolling down the list of games in the home page, or (if there is the time to implement) look for specific ones via search bar.

Basic developer functionalities → Developer functionalities will contain components such as the ability to add games and managing the games in the developer’s inventory. The database will provide sales statistics as well as a list of games developed by the users, and restrict requests so that only the developer of the games can make changes to the games/inventory.

Game/service interaction → All communication between the game and the service will be handled via the window.postMessage() method, which will enable sending messages between the two platforms.

Save/load feature → The save/load feature can be implemented by saving all the necessary player data in a game into a JSON format, which will then be stored in the database. When the player accesses the game again, a message will pop up to ask whether the player wishes to continue playing from the saved data or start a new game. 

RESTful API → RESTful API will be used for accessing the database, be it for the purpose of purchasing games, retrieving saved game data, logging in to the service, etc.

-------------------------------------------------------------------------------------------------------------------------------
 
**MODELS AND VIEWS**
 
The project will have three models altogether: Player, Developer, and Game. Since Django’s User model provides the fields username, password, email, first_name, and last_name, the Player model can be created by extending the User model, and the Developer model from the Player model, thus allowing the developer to also have the role of a player. The Player model can have additional fields such as purchased_games and saved_games, and the Developer model created_games. The Game model will have the fields developer, price, on_sale, url, and scores. 
 
As for views, there will be home, game, my_games, store, statistics, and login, to begin with. Home view will serve as the home page of the service, displaying popular games and high scores. In game view a player can play games they have purchased, whereas my_games will display a list of games that a player has purchased. Statistics view will display sales statistics of the games to the developers, and store view will display all the games available for a player to purchase. Finally, there will also need to be some form of a login view to handle user registration, login, and logout features. 
 
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

DEVELOPER NOTES

How to get rid of "Class has no objects member" error caused by pylint
1. pip install pylint-django
2. In VSC go to settings (File > Preferences > Settings > Extensions > Django configuration and open json file)
3. Insert {"python.linting.pylintArgs": ["--load-plugins=pylint_django"],}


