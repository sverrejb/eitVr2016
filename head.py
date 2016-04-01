from rift import PyRift
from math import atan, asin, pi
import socket


def to_angles(quaterions):
    q_0 = quaterions[0]
    q_1 = quaterions[1]
    q_2 = quaterions[2]
    q_3 = quaterions[3]

    theta = asin(2 * (q_0 * q_2 - q_3 * q_1))
    theta = (theta * 180) / pi

    psi = atan(2 * (q_0 * q_3 + q_1 * q_2) / (1 - 2 * (q_2 * q_2 + q_3 * q_3)))
    psi = (psi * 180) / pi

    return int(theta)+90, int(psi)+90

hmd = PyRift()

HOST = '129.241.65.95'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

if __name__ == '__main__':
    while True:
        hmd.poll()
        quaternions = hmd.rotation
        theta, psi = to_angles(quaternions)
        payload = str(theta).zfill(3)+"," + str(psi).zfill(3)
        s.send(payload)

s.close()
