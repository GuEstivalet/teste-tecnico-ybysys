# teste-tecnico-ybysys

## Objetivo do experimento:
Explorar e comparar as características 2 diferentes algorítmos de visão computacional: HSV e K-means.  

## Estrutura do projeto



teste-tecnico-ybysys/

├── main.py

├── requirements.txt

├── README.md

├── inputs/

│   ├── barroco.jpg

│   ├── blue-green.jpg

│   ├── blue.jpg

│   └── green.png


└── outputs/

.    └── (masks e overlays)




### Iniciar um ambiente virtual, especialmente para distros Linux based:


```bash
    python -m venv venv

    source venv/bin/activate  # No Linux/macOS

    venv\Scripts\activate     # No Windows
```


## Requirements.txt


Imporante assegurar-se de que os pré-equisitos sejam atendidos antes de replicar o experimento.

```bash
pip install -r requirements.txt
```

## Como Rodar

O script principal é o `main.py`. **O argumento `--input` é obrigatório** para especificar o caminho da imagem.

### Exemplos de execuções


HSV:

- a) python3 main.py --input inputs/blue.jpg --hsv --target blue

- b) python3 main.py --input inputs/blue-green.jpg --hsv --target green 

K-MEANS:

- a) python3 main.py --input inputs/blue.png --kmeans --target blue --k 4

- b) python3 main.py --input inputs/green.png --kmeans --target green --k 6


## Características de cada algorítmo

- HSV:

- K-means:

## Limitações esperadas



## Desafios encontrados

O maior desafio foi o ponto departida.
Porém, ao desenvolver as  funções que aplicam os algoritmos o processo ficou mais claro.
Ademais, foi utilizada IA generativa para definir os valroes padões de HSV_RANGES e OVERLAY_COLORS.
