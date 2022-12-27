# rock paper scissor
import random
print('Enter "rock / paper / scissor"')
score_user = 0
loops = 0
socre_bot = 0
score_lavel = int(input('Enter Score value :  '))
# this while loops use for itration this code (infinity)
while loops <= score_lavel:
    user_value = input('enter your key :  ')
    game_list = ['rock', 'paper', 'scissor']
    bot_value = random.choice(game_list)
    loops += 1

    if bot_value == 'rock' and user_value == 'paper' or bot_value == 'paper' and user_value == 'scissor' or bot_value == 'scissor ' and user_value == 'rock':
        print('you won ')

        score_user += 1
        print('Your score is ' + str(score_user))

    elif bot_value == user_value:
        print('you value and bot value are equal')

    else:
        print('you lost')
        print('bot choice is  ' + bot_value)
        socre_bot += 1
        print('Bot score is : ' + str(socre_bot))
if score_user > score_lavel:
    print('You won this series$$')

else:
    print('you lost this series$$')
