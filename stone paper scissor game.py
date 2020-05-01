#Stone Paper Scissor Game
import random
lst = ['s','p','k']

print("~~~~~~~~~~~~~~~~~~~~~~Welcome in Stone Paper Scissor Game~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


chance = 10
turn = 0
player_score = 0
comp_score = 0

while turn < chance:
    print("s for stone")
    print("p for Paper")
    print("k for Scissor")
    player_input = str(input("WHICH ONE DO YOU WANT TO TAKE:"))
    comp_input = random.choice(lst)
    if player_input == comp_input:
        print("Tie!!")
        turn = turn + 1
        print(f"your choice is {player_input} and computer choice is {comp_input}")
        print(f"your score is {player_score} and computer score is {comp_score}")
        print(f"{chance - turn} times you can play more")
        print("~~~~~~~~~~~~~~~~~~~~~~~TIE, PLAY AGAIN!!~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif player_input == 's' and comp_input == 'p':
        print("You LOOSE!!! , Computer WON!!!")
        turn = turn + 1
        comp_score = comp_score + 1
        print(f"your choice is {player_input} and computer choice is {comp_input}")
        print(f"your score is {player_score} and computer score is {comp_score}")
        print(f"{chance - turn} times you can play more")
        print("~~~~~~~~~~~~~~~~~~~~~~~TRY AGAIN~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif player_input == 's' and comp_input == 'k':
        print("You WON!!! , Computer LOOSE!!!")
        turn = turn + 1
        player_score = player_score + 1
        print(f"your choice is {player_input} and computer choice is {comp_input}")
        print(f"your score is {player_score} and computer score is {comp_score}")
        print(f"{chance - turn} times you can play more")
        print("~~~~~~~~~~~~~~~~~~~~~~~CONGRATULATIONS~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif player_input == 'p' and comp_input == 's':
        print("You WON!!! , Computer LOOSE!!!")
        turn = turn + 1
        player_score = player_score + 1
        print(f"your choice is {player_input} and computer choice is {comp_input}")
        print(f"your score is {player_score} and computer score is {comp_score}")
        print(f"{chance - turn} times you can play more")
        print("~~~~~~~~~~~~~~~~~~~~~~~CONGRATULATIONS~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif player_input == 'p' and comp_input == 'k':
        print("You LOOSE!!! , Computer WON!!!")
        turn = turn + 1
        comp_score = comp_score + 1
        print(f"your choice is {player_input} and computer choice is {comp_input}")
        print(f"your score is {player_score} and computer score is {comp_score}")
        print(f"{chance-turn} times you can play more")
        print("~~~~~~~~~~~~~~~~~~~~~~~TRY AGAIN~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif player_input == 'k' and comp_input == 'p':
        print("You WON!!! , Computer LOOSE!!!")
        turn = turn + 1
        player_score = player_score + 1
        print(f"your choice is {player_input} and computer choice is {comp_input}")
        print(f"your score is {player_score} and computer score is {comp_score}")
        print(f"{chance - turn} times you can play more")
        print("~~~~~~~~~~~~~~~~~~~~~~~CONGRATULATIONS~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif player_input == 'k' and comp_input == 's':
        print("You LOOSE!!! , Computer WON!!!")
        turn = turn + 1
        comp_score = comp_score + 1
        print(f"your choice is {player_input} and computer choice is {comp_input}")
        print(f"your score is {player_score} and computer score is {comp_score}")
        print(f"{chance-turn} times you can play more")
        print("~~~~~~~~~~~~~~~~~~~~~~~TRY AGAIN~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("ENTER VALID CHOICE")
        print("TRY AGAIN!!!")

print("GAME OVER!!")
if player_score == comp_score:
    print("OVERALL,GAME IS DRAW")
elif player_score > comp_score:
    print("OVERALL, YOU WIN THE GAME......CONGRATULATIONS!!!!!!!!!!!")
else:
    print("OVERALL, YOU LOOSE THE GAME......PLAY AGAIN!!!!!!!!!!!")
    print(f"YOUR FINAL SCORE IS {player_score} AND COMPUTER FINAL SCORE IS {comp_score}")
# func()
# print("DO YOU WANT TO PLAY AGAIN:")
#
# var = input("write 1 for yes and 0 for no")
# if var == 1:
#     func()
# else:
#     pass
