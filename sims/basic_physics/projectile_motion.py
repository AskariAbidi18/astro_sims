import sys, os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from astro_sims.constants.phys_constants import g

from math import sin, cos, radians as deg_to_rad
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


class ProjectileMotion:
    def __init__(self, x0, y0, v0, angle_deg, dt):
        self.dt = dt
        self.x_history = []
        self.y_history = []

        angle_rad = deg_to_rad(angle_deg)
        vx0 = v0 * cos(angle_rad)
        vy0 = v0 * sin(angle_rad)

        self.state = [x0, y0, vx0, vy0]

    def derivatives(self, state):
        x, y, vx, vy = state
        dxdt = vx
        dydt = vy
        dvxdt = 0
        dvydt = -g
        return [dxdt, dydt, dvxdt, dvydt]

    def step(self):
        x, y, vx, vy = self.state
        dxdt, dydt, dvxdt, dvydt = self.derivatives(self.state)
        dt = self.dt

        x = x + dxdt * dt
        y = y + dydt * dt
        vx = vx + dvxdt * dt
        vy = vy + dvydt * dt

        self.state = [x, y, vx, vy]

    def run(self):
        while self.state[1] >= 0:
            self.x_history.append(self.state[0])
            self.y_history.append(self.state[1])
            self.step()

    def plot(self):
        plt.plot(self.x_history, self.y_history)
        plt.title("Projectile Motion Trajectory")
        plt.xlabel("Distance (m)")
        plt.ylabel("Height (m)")
        plt.grid()
        plt.show()

    def animate(self):
        fig, ax = plt.subplots()

        # TRAIL
        trail, = ax.plot([], [], '-', linewidth=2)
        # MOVING DOT
        dot, = ax.plot([], [], 'o', markersize=8)

        # Camera bounds
        ax.set_xlim(0, max(self.x_history) * 1.1)
        ax.set_ylim(0, max(self.y_history) * 1.1)

        # Init function required to avoid empty frame errors
        def init():
            trail.set_data([], [])
            dot.set_data([], [])
            return trail, dot

        # Frame updater
        def update(frame):
            # Update TRAIL (0 → frame)
            trail.set_data(
                self.x_history[:frame],
                self.y_history[:frame]
            )
            # Update MOVING DOT
            dot.set_data(
                [self.x_history[frame]],
                [self.y_history[frame]]
            )
            return trail, dot

        anim = FuncAnimation(
            fig,
            update,
            init_func=init,
            frames=len(self.x_history),
            interval=15,
            blit=False  # blit causes problems on TkAgg
        )

        writer = PillowWriter(fps=30)
        anim.save("projectile.gif", writer=writer)
        plt.close()


if __name__ == "__main__":
    sim = ProjectileMotion(
        x0=0,
        y0=0,
        v0=32,
        angle_deg=76,
        dt=0.01
    )

    sim.run()
    sim.plot()
    sim.animate()
