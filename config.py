# Neural network
ai_play = True
collect_data = False # if the game data can be stored in the csv file to train the neural network.

# game config:
acceleration_speed = 0.03  # speed with witch you accelerate. Standard 0.03
brake_speed = 0.4  # speed with witch you brake. Standard 0.4
steering_speed = 0.15  # speed with witch you steer. Standard 0.15
stable_civilian_car_speed = 5
speedometer = True  # if set to false dashboard disappears. Standard True
crazy_speedometer = True  # if set to false speedometer wont go "ghelicopter ghelicopter"
max_speed = 120  # set the top speed of the car

collision = True
raycasting = True
crash_is_game_over = True

# bug testing:
hitbox_visuals = True  # shows the hit box for collision bug testing
raycasting_visuals = True  # shows ray casting for bug testing and fun
