import cv2
import numpy as np
import argparse
import os
import time

# optei por usar o kmeans do próprio cv2

# a lib opencv utiliza trabalha com BGR, que consiste nos canais RGB invertidos

# ranges de hsv e cores alvo padrão
HSV_RANGES = {
    'green': {
        'h_min': 35, 'h_max': 85,  # Tonalidade verde comum
        's_min': 50, 's_max': 255,
        'v_min': 50, 'v_max': 255
    },
    'blue': {
        'h_min': 95, 'h_max': 130, # Tonalidade azul comum
        's_min': 50, 's_max': 255,
        'v_min': 50, 'v_max': 255
    }
}

# cor BGR para o overlay
OVERLAY_COLORS = {
    'green': (0, 255, 0),  # Verde
    'blue': (255, 0, 0)   # Azul (BGR)
}

