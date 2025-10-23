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


# algorítimos de segmentação

# HSV divide em matriz, saturação, valor

def segment_hsv(image_bgr, target, h_min, h_max, s_min, s_max, v_min, v_max):

    # converte de BGR -> HSV
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

    # define o range de cores (limites inferiores e superiores)
    lower_bound= np.array([h_min, s_min, v_min])
    upper_bound= np.array([h_max, s_max, v_max])

    # cria a máscara usando a lib open-cv
    mask = cv2.inRange(image_hsv, lower_bound, upper_bound)

    return mask

# kmeans -> algorítmo de clusterização.
# o parâmetro k determina o número de centróides 

def segment_kmeans(image_bgr, k, target):
    # reformata a imagem
    image_float = image_bgr.reshape((-1, 3)).astype(np.float32)

    #critérios de parada: (tipo, max_iter, epsilon)
    # max_iter - nr máximo de iterações do algoritmo
    # epsilon - criterio de parada com base na precisão
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(
        data=image_float,
        K=k,
        bestLabels=None,
        criteria=criteria,
        attempts=10,
        flags=cv2.KMEANS_PP_CENTERS
    )

    # identifica o cluster alvo
    # encontra o centróide mais próximo da cor alvo (em BGR).
    target_bgr = OVERLAY_COLORS[target] 

    # calcular a dist. euclidiana de cada centróide para a cor alvo
    distances = np.linalg.norm(centers - np.array(target_bgr), axis=1)

    # o cluster alvo é o que tem a menor distancia
    target_cluster_index = np.argmin(distances)

    # criar a máscara: pixels pertencentes ao cluster alvo são 255
    mask = np.zeros( labels.shape, dtype=np.uint8)
    mask[labels.flatten() ==  target_cluster_index] = 255
    mask= mask.reshape(image_bgr.shape[:2]) # voltar para o 2D

    return mask
