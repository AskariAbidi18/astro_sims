import sys, os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from astro_sims.constants.phys_constants import g, M_sun, M_earth, G

class TwoBodyOrbit:
    def __init__(self, state1, state2):
        self.m1 = M_sun
        self.m2 = M_earth
        self.state1 = state1  # [x, y, vx, vy]
        self.state2 = state2  # [x, y, vx, vy]
        self.dt = 3600
        self.x1_history = []
        self.y1_history = []
        self.x2_history = []
        self.y2_history = []

    def derivatives(self, state1, state2):
        pass
