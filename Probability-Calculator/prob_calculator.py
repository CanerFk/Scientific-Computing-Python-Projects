import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_dict = {}

        for ball in drawn_balls:
            if ball in drawn_dict:
                drawn_dict[ball] += 1
            else:
                drawn_dict[ball] = 1

        for color, count in expected_balls.items():
            if color not in drawn_dict or drawn_dict[color] < count:
                break
        else:
            success_count += 1

    return success_count / num_experiments