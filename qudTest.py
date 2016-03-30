#!/usr/bin/python

from rift import PyRift
import math
import time

foo = PyRift()

while True:
    foo.poll()

    q_0 = foo.rotation[0];
    q_1 = foo.rotation[1];
    q_2 = foo.rotation[2];
    q_3 = foo.rotation[3];

    phi = math.atan((2 * q_0 * q_1 + q_2 * q_3) / 1 - 2 * (q_1 * q_1 + q_2 * q_2));
    phi = (phi * 180) / 3.1415;

    theta = math.asin(2 * (q_0 * q_2 - q_3 * q_1));
    theta = (theta * 180) / 3.1415;

    psi = math.atan(2 * (q_0 * q_3 + q_1 * q_2) / (1 - 2 * (q_2 * q_2 + q_3 * q_3)));
    psi = (psi * 180) / 3.1415;

    print("-----------------------------------------------------------------")
    print("Quarternions : %f %f %f %f" % (q_0, q_1, q_2, q_3))
    print("rotation in euler coordinates from 0 to 180: %f %f %f " % (phi, theta, psi))
    # time.sleep(1);

# print("rotation quat: %f %f %f %f" % (foo.rotation[0],
#     foo.rotation[1],
#     foo.rotation[2],
#     foo.rotation[3]))

# Convert quarternions to euler

# double a = foo.rotation[0];
# double b = foo.rotation[1];
# double c = foo.rotation[2];
# double d = foo.rotation[3];

# double kat_x = atan2(-2*b*c)+2*b*d), 1 - 2 * (a*a + b*b));
# kat_x = (kat_x * 180) / 3.1415;

# double kat_y = asin(2 * (a*c + b*d));
# kat_y = (kat_y * 180) / 3.1415;

# double kat_z = atan2(2 * (-a*b + 2*c*d), 1 - 2 * (b*b + c*c));
# kat_z = (kat_z * 180) / 3.1415;
