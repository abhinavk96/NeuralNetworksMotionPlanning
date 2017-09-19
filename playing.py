"""
Once a model is learned, use this to play it.
"""

from carGame import carGame
import numpy as np
from neuralNetwork import neural_net

NUM_SENSORS = 1


def play(model):

    car_distance = 0
    game_state = carGame()

    # Do nothing to get initial.
    _, state = game_state.update(0)

    # Move.
    while True:
        car_distance += 1

        # Choose action.
        action = (np.argmax(model.predict(state, batch_size=1)))
        print("Action:", action)

        # Take action.
        _, state = game_state.update(action)

        # Tell us something.
        if car_distance % 1000 == 0:
            print("Current distance: %d frames." % car_distance)


if __name__ == "__main__":
    saved_model = 'saved-models/164-150-100-50000-77500.h5'
    model = neural_net(NUM_SENSORS, [164, 150], saved_model)
    play(model)