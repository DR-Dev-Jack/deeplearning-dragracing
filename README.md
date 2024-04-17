# deeplearning dragracing
 Really simple pycharm car "simulation" in wich ai will drive alongside other cars.

![screenie of basic game](https://github.com/DR-Dev-Jack/deeplearning-dragracing/blob/main/other/screenie.png?raw=true)
# diy
to make your own model for the simulation:

STEP 1: Change ai_play to "False" and collect_data to "True" in config.py . This will make it so the ai does not play the game but the user does and all the user his choices get recorded.

STEP 2: Play the game, and let it collect data to make an model off.

STEP 3: Run "second_brain.ipynb" to create a model called "DiyModel.h5" with the created collection of data.

STEP 4: Turn ai_play back to "True", collect_data back to "False" and change model to "DIYModel" in the config.
now you can run your own ai.

You can also turn random stuff on like my custom build "ray tracing".