#!/usr/bin/env python3
import argparse
import numpy as np
import matplotlib.pyplot as plt

def plot_kinematic(robot_speed, belt_speed, time_end, num_points=500):
    """
    Plots position vs. time for a robot and an object on a conveyor belt.
    
    Parameters:
    - robot_speed: float, speed of the robot (m/s)
    - belt_speed: float, speed of the conveyor belt object (m/s)
    - time_end:   float, total time to simulate (s)
    - num_points: int, number of time points to compute
    """
    t = np.linspace(0, time_end, num_points)
    pos_robot  = robot_speed * t
    pos_object = belt_speed * t

    plt.figure()
    plt.plot(t, pos_robot,  label=f'Robot (v={robot_speed} m/s)')
    plt.plot(t, pos_object, label=f'Object on Belt (v={belt_speed} m/s)')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.title('Kinematic Schematic: Position vs Time')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(
        description="Plot robot vs. conveyor belt object kinematics."
    )
    parser.add_argument(
        '--robot_speed', '-r', type=float, default=2.0,
        help="Robot speed in meters per second (default: 2.0)"
    )
    parser.add_argument(
        '--belt_speed', '-b', type=float, default=1.0,
        help="Conveyor belt speed in meters per second (default: 1.0)"
    )
    parser.add_argument(
        '--time_end', '-t', type=float, default=10.0,
        help="Total time to simulate in seconds (default: 10)"
    )
    args = parser.parse_args()
    
    plot_kinematic(args.robot_speed, args.belt_speed, args.time_end)

if __name__ == "__main__":
    main()
