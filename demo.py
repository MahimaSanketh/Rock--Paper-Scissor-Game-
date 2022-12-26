# rock paper scissor
import random
print('Enter "rock / paper / scissor"')
score_user = 0
socre_bot = 0
while 0 <= 10:  # this while loops use for itration this code (infinity)
    user_value = input('enter your key :  ')
    game_list = ['rock', 'paper', 'scissor']
    bot_value = random.choice(game_list)

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
