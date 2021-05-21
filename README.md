# Python_Bulletgame
Prototype for a Python danmaku-style game.
@author RJ REAVES
@author GEIR ANDERSON

How to play:

Run with:
    <New Method>
        bulletapp  [optional. number of starting lives]
    <Old Method>
        python3 gameloop.py [optional. number of starting lives]

Controls:

Move:
    w, a, s, d
    up arrow, left arrow, down arrow, right arrow

    hold shift to shrink hitbox and use alt fire, but move slower

Shoot:
    hold enter or x
    alt fire by holding shift and pressing enter or x

Quit:
    esc

Notes:
    default life count is 3
    one hit will kill the player, can't die for about 5 seconds after death
    enemies have different health levels, speeds, sizes, max_bullets, etc.
    killing enemies can lead to upgrades
    single bullets deal more damage than spread bullets
    game closes when player is out of lives
    player loses upgrades on death

    https://stackoverflow.com/questions/32078346/python-pygame-enemy-collision
    https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/projectiles/
    https://www.youtube.com/watch?v=sj8Sg8qnjOg
    https://stackoverflow.com/questions/49907034/python-pygame-score-display
    https://www.pygame.org/docs
    http://thepythongamebook.com/
