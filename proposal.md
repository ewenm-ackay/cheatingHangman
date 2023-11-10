# Proposal

## What will (likely) be the title of your project?

#### Cheating Hangman

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

We will design a hangman game that cheats by choosing a new word based on the users most recent guess using dictionaries. We also want to animate the hangman.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

***Our guaranteed deliverable:*** A logically sound, perfected version of Cheating Hangman. The user will be allowed to pick between 1 guess and 25 guesses. The user can input a cheatcode to get an extra 26th guess to guarantee they guess the word. We want to draw the hangman, even if its with words. If the user chooses 26 guesses, each incorrect guess will correspond with one of the folowing body parts, returned in a print statement. Head, body, left arm, right arm, left leg, right leg, left thumb, right thumb, left big toe, right big toe, on and on until we have 20 toes, 2 arms, 2 legs, a body, and a head, for a total of 26 guesses. 
1. If the user inputs 1 guess: the entire body is drawn on failure.
2. If the user inputs 2 guesses: the head, the body and one arm for the first failure and one arm, the left and the right left on the second failure (no toes)
3. If the user inputs 3  guesses: the head and the body on the first failure, two arms on the second and two legs on the third.
4. If the user inputs 4 guesses: the head on the first failure, the body on the second, two arms on the third, and two legs on the fourth.
5. If the user inputs 5 guesses: The head and body will be drawn on the first failure, and each limb drawn seperately consequitevely.
For **ALL** inputs for guesses after 5, one finger will be added for each input from 6-16, and one toe will be added for inputs from 17-26, and any input out of these bounds will be prompted for re-entry.

***What we really really want to have, and do not want to exclude:*** An ASCII art of possible letters, a graveyard of used letters, and a drawing of the hanging man as the game goes on.

***What would be AWESOME to include:*** A user-friendly GUI with an on-screen keyboard and an aesthetically pleasing graphical rendering of our hangman, where we can see pieces be added as the user guesses.

#### If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

    N/A

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

Ewen Mackay, Johnny Tan and Md Ar-Rashid

#### In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

We will develop logic in psuedo code to randomly choose words out of the biggest dictionary available, to perfect the cheating hangman. As the user guesses more, the possible words decrease. We want the program to randomly choose a letter from the largest pool of possible words, and if that means giving the user a letter in our word and progress towards a final guess, we will implement logic to initiate this scenario.

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

If a graphical rendering of the hangman game and GUI is too difficult, we may result to ASCII art for our drawing. A box of possible letters and a "Graveyard" for used letters would also be good.


### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

We also want a user friendly interface as well as a graphical rendition of the progress of the hangmang. 
- possible letters
- graveyard for used letters

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

As a group, we should figure out who is best at which part(s). We want to figure out and research any topics we may need to learn before even coding ANYTHING. Outline the entire project logically, on paper preferably, and begin by discussing our strengths and weaknesses in each area.
