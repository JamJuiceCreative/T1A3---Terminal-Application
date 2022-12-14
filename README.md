# <p style="text-align:center"> ZAPP - Zombie Apocalypse Planning Poker</p>

## <p style="text-align:center">-----------------RULES----------------</p>
<p style="text-align:center">---ZOMBIE APOCALYPSE PLANNING POKER---</p>

ZAPP is a consensus card game based off of
planning poker or scrum poker only it's the 
end of the world and a zombie apocalypse!

1. From a range of cards; 
'Ace', '2', '3', '5', '8', 'King'.
You and your fellow survivors must determine the
difficulty of a challenge by each throwing a card.

2. Ace being the challenge is easy and 8 being the 
task is hard. Throwing a 'King'; the challenge is 
impossible and you will skip the round and move on 
to the next.

3. If you all throw different cards, you will each 
throw again until you have reached a consensus and 
have all thrown the same card.

4. The game will then evaluate your groups decisions
against the difficulty rating of the challenge and
determine whether you succeeded or failed. 

5. Success will award points based on the difficulty 
of the challenge however your overall score will be
penalised incrementally based on the value of the
cards you all agreed upon. 

In other words, the lower the card, the less valuable
resources like guns, ammo, food and people you'll need
to expend. But you'll still need to pass the challenge
or you're coming home empty handed.  

Have fun survivor and good luck!!!

## <p style="text-align:center">Help for executing program;</p>
___
Instructions for running zapp.sh;

1. In ubuntu (linux) terminal check if python is installed:

        python -V
            Python 3.12.0a2

2. If python is not installed or it's an outdated version;
    Download the latest version of python:

        sudo apt install python3

3. Make sure the following packages are installed in your system;

        art==5.8
        attrs==22.1.0
        colored==1.4.4
        iniconfig==1.1.1
        packaging==22.0
        pluggy==1.0.0
        pytest==7.2.0

4. If any are missing; (for example - colored)

        pip install colored

5. finally run executable file zapp.sh;

        ./zapp.sh

## <p style="text-align:center">Project Overview;</p>


Project Management Platform: https://trello.com/b/1Fb6TSx0/terminal-app-zapp-zombie-appocalypse-planning-poker<br>
Source Control Repository:
https://github.com/JamJuiceCreative/T1A3---Terminal-Application
___
## <p style = "text-align:center"> References </p> 
Rules for Planning Poker - https://en.wikipedia.org/wiki/Planning_poker<br>
### External Packages; <br>
art 5.8 - https://pypi.org/project/art/ <br>
colored 1.4.4 - https://pypi.org/project/colored/ <br>