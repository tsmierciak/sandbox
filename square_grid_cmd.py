# -*- coding: utf-8 -*-
"""
Simple program to illustrate cartesian mesh visualisation
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import argparse
import math


def make_parser():

    """Build command line parser"""
    parser = argparse.ArgumentParser(description='Square grid rotated by the angle')
    return parser


def set_parser_arguments(parser):
    """Add specific command line arguments to the parser"""
    parser.add_argument('--angle', dest='ang', default=0, type=int,
                        help='Sets the rotation angle in degrees (default 0)')
    parser.add_argument('--dimensions', dest='dim', default="4, 4", type=str,
                        help='Sets the dimensions of the grid (default (4,4)')


def show_square(grid_resolution='5, 4', angle=0):
    """Draw Cartesian grid in a square [-1,1]x[1,1] rotated by given angle
    Parameters
    ----------
    grid_resolution : int or tuple
        number of cells in X and Y direction. If single number is given then
        mesh resolution in both directions is the same
    angle
        rotation angle in degrees
    """
    res = eval(grid_resolution)

    try:
        resolution = res[0:2]
    except TypeError:
        resolution = (res,) * 2

    fig, ax = plt.subplots()
    angle = np.deg2rad(angle)
    c, s = math.cos(angle), math.sin(angle)
    rot = np.array([[c, -s], [s, c]])
    x = np.linspace(-1.0, 1.0, resolution[0] + 1, dtype=np.float64)
    y = np.linspace(-1.0, 1.0, resolution[1] + 1, dtype=np.float64)
    xx, yy = np.meshgrid(x, y)
    coordinates = np.dot(np.c_[xx.flatten(), yy.flatten()], rot.T)
    square_mesh = matplotlib.collections.QuadMesh(*resolution, coordinates,
                                                  edgecolors='black')
    ax.add_collection(square_mesh)
    ax.autoscale()
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    parser = make_parser()
    set_parser_arguments(parser)
    args = parser.parse_args()
    show_square(angle=args.ang, grid_resolution=args.dim)
