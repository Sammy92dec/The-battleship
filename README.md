# Battle-Ship
 
A strategic board game played by one player. In this case, this game will be played by guessing randomly hidden ships. 
The program allows you to guess by row and column. The board is small and the turns are 20x to make the chances of the ships to be found easily. A quick and short game to find 3 ships will keep a player interested in playing more.

Here is a live link to the game :- https://thebattleship-7ec99083b645.herokuapp.com/

## How to play

The rules of the game are fairly simple. It begins by asking the player to choose a username and their board is created.
The user will select a row and column from 0 - 6.
After both a valid row and column are entered by the user, a sign is displayed on the board depending on whether or not their guess was correct. If the user managed to hit a ship successfully, they are told their guess was correct by seeing "X" displayed on the board which corresponds with the row and column selected by the user. If their guess was incorrect, however "O" is displayed on the board.
If the user happens to select a row or column outside of that range or enter an unrecognized key, they will be given an error message and asked to type in a valid row.

The player has a total of SHips goes to try and sink 10 out of 40 hidden ships on the board. 
Once they run out of all SHIPS, they are presented with a game-over message and the game ends. 
If the user successfully manages to guess the correct position of all NO>SHIPS, however, then they are presented with an congratulatory message and told they have sunk all ships. Upon each successful hit that the user correctly guesses on the board.


Here is a live link to the game :- https://thebattleship-7ec99083b645.herokuapp.com/

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)

* [Features](#features)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  
  * [Acknowledgments](#acknowledgments)

---

## User experience (UX)



### User stories
A simple and fun game to play.
Easy to understand the structure of the webpage. 


#### User goals
To play a fun game.
To  play a game that is easy to navigate and understand.

### Future Implementations

- To set a break for best out of five.
- To be able to start over without pressing run program.
- To have players board. 

### Accessibility

## Technologies Used

### Languages Used

### Frameworks, Libraries & Programs Used

## Testing


### Solved bugs

##  **Deploying to Heroku**

1. Go to [Heroku](https://id.heroku.com/login), create account if you don't have and log in.
- Head to your dashboard and click "New", then "Create new app"
- New/CreateNewApp
    
3. Next step is to give your app a name and to choose region. After that click on "Create app".

- Name/Region/Create
    
4. After that head to "Settings" tab which you can find on top of your Heroku page.

5. Then in the "Buildpacks" section you will need to add buildpacks. Pay attention to the order in which you add buildpacks you need. In my case I had to add Python first and nodejs second.

6. First add "Python", by clicking on Python icon and then click on "Add Buildpack".

7. Then add "nodejs", by clicking on nodejs icon and then click on "Add Buildpack".

8. Then head to "Deployment" tab which you can also find on top of your Heroku page and under "Deployment method" click on "GitHub"(in my case that's where my repository is).

9. After that, just under the "Deployment method" section is "Connect to GitHub" section where you need to find your repository and then click on "Connect".

10. Just under "Connect to GitHub" section is "Automatic deploys" section where you can click on "Enable Automatic Deploys" if that's what you want and just under is "Manual Deploy" section, where you need to click on "Deploy Manually".


## Credits

- My sister Nazret for supporting me through the whole process.

- AleksandarJavorovic in github for the README content.

- "Love Sandwiches" project for inspirtation and Should me how to deploy the game with Heroku.

### Code Used

- Inspiration for the program came from youtube tutorials that I have watched and other students projects from code insistute.But the code are original.

### Content

Written by Samrawit Tekheste.
  
###  Acknowledgments
