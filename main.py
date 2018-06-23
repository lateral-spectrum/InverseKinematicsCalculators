import math
from output import *

"""
    Inverse Kinematics calculations for SCARA 3DOF robotic arm using trig.
"""

theta_2_positive = False
target_x = 100
target_y = 32
shoulder_length = 150
elbow_length = 80

if theta_2_positive:
    n = pow(target_x, 2) + pow(target_y, 2) - shoulder_length - elbow_length
    d = 2 * shoulder_length * elbow_length
    theta_2 = math.acos(n / d)

    p1 = math.atan2(target_y, target_x)
    n = elbow_length * math.sin(theta_2)
    d = shoulder_length + (elbow_length * math.cos(theta_2))
    p2 = math.atan(n / d)
    theta_1 = p1 - p2

    theta_1_degrees = math.degrees(theta_1)
    theta_2_degrees = math.degrees(theta_2)

    print_result(theta_1_degrees, theta_2_degrees, target_x, target_y)

else:
    n = pow(target_x, 2) + pow(target_y, 2) - pow(shoulder_length, 2) - pow(elbow_length, 2)
    d = 2 * shoulder_length * elbow_length
    theta_2 = -math.acos(n / d)

    p1 = math.atan2(target_y, target_x)
    n = shoulder_length * math.sin(theta_2)
    d = shoulder_length + (elbow_length * math.cos(theta_2))
    p2 = math.atan(n / d)
    theta_1 = p1 + p2

    theta_1_degrees = math.degrees(theta_1)
    theta_2_degrees = math.degrees(theta_2)

    print_result(theta_1_degrees, theta_2_degrees, target_x, target_y)
