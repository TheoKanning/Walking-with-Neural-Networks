from math import pi
import pymunk
import pymunk.pygame_util

# Collision Types #


# Weight Fractions #
HEAD_WEIGHT_FRACTION = 0.0826
TORSO_WEIGHT_FRACTION = 0.551
UPPER_ARM_WEIGHT_FRACTION = 0.0325
FOREARM_WEIGHT_FRACTION = 0.0187 + 0.0065  # Including hand
THIGH_WEIGHT_FRACTION = 0.105
LEG_WEIGHT_FRACTION = 0.0475
FOOT_WEIGHT_FRACTION = 0.0143

# Height Fractions #
HEAD_HEIGHT_FRACTION = 0.1075
TORSO_HEIGHT_FRACTION = 0.3
UPPER_ARM_HEIGHT_FRACTION = 0.172
FOREARM_HEIGHT_FRACTION = 0.157  # Not including hand
THIGH_HEIGHT_FRACTION = 0.232
LEG_HEIGHT_FRACTION = 0.247
FOOT_HEIGHT_FRACTION = 0.0425

# Starting Height Fractions #
SHOULDER_STARTING_HEIGHT_FRACTION = LEG_HEIGHT_FRACTION + THIGH_HEIGHT_FRACTION + TORSO_HEIGHT_FRACTION
ELBOW_STARTING_HEIGHT_FRACTION = LEG_HEIGHT_FRACTION + THIGH_HEIGHT_FRACTION + TORSO_HEIGHT_FRACTION - UPPER_ARM_HEIGHT_FRACTION / 2
HIP_STARTING_HEIGHT_FRACTION = LEG_HEIGHT_FRACTION + THIGH_HEIGHT_FRACTION
KNEE_STARTING_HEIGHT_FRACTION = LEG_HEIGHT_FRACTION
FOOT_STARTING_HEIGHT_FRACTION = 0

# Joint Constraints #
ELBOW_MIN_ANGLE = 0
ELBOW_MAX_ANGLE = 3 * pi / 4
SHOULDER_MIN_ANGLE = -pi / 2
SHOULDER_MAX_ANGLE = pi
HIP_MIN_ANGLE = 0
HIP_MAX_ANGLE = 3 * pi / 4
KNEE_MIN_ANGLE = -2 * pi / 3
KNEE_MAX_ANGLE = 0
FOOT_MIN_ANGLE = -pi / 4
FOOT_MAX_ANGLE = pi / 4

# Size and Weight Constants
TOTAL_MASS = 80  # Made up units
TOTAL_HEIGHT = 300  # Pygame pixels
STARTING_X_POSITION = 300
STARTING_Y_POSITION = 150
SEGMENT_WIDTH = 5


def create_torso():
    """
    Creates a pymunk body and shape to represent the torso
    :returns torso body, torso shape
    """
    mass = TOTAL_MASS * TORSO_WEIGHT_FRACTION
    length = TOTAL_HEIGHT * TORSO_HEIGHT_FRACTION
    inertia = pymunk.moment_for_segment(mass, (0, length / 2), (0, -length / 2))
    torso_body = pymunk.Body(mass, inertia)
    torso_body.position = STARTING_X_POSITION, TOTAL_HEIGHT * HIP_STARTING_HEIGHT_FRACTION + length / 2 + STARTING_Y_POSITION
    torso_shape = pymunk.Segment(torso_body, (0, length / 2), (0, -length / 2), SEGMENT_WIDTH)
    return torso_body, torso_shape


class HumanBody:
    def __init__(self):
        self.torso_body, self.torso_shape = create_torso()

    def draw(self, screen):
        """
        Draws all bodies using the supplied pygame screen
        :param screen: pygame screen
        """
        pymunk.pygame_util.draw(screen, self.torso_shape)