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

- b) python3 main.py --input inputs/green.jpg --method hsv --hmin 20 --hmax 90 --smin 40 --smax 255 --vmin 40 --vmax 255 --target green

Obs.: Aqui aumentamos o range do canal H, S e V em relação ao padrão e aplicamos o target green para a imagem com cor verde predominante.


K-MEANS:

- a) python3 main.py --input inputs/blue.png --kmeans --target blue --k 4

- b) python3 main.py --input inputs/green.png --kmeans --target green --k 6


## Características de cada algorítmo


- HSV:

A segmentação por cor no espaço HSV ataca o problema `definindo limites absolutos de cor através de seis parâmetros`(hmin, hmax, smin, smax, vmin, vmax). Seu ponto forte reside na velocidade e precisão determinística, sendo ideal para isolar cores puras e uniformes, como placas. O canal de Tonalidade (H) confere relativa robustez contra variações de brilho e sombra. Contudo, sua principal limitação é a sensibilidade ao limiar, pois requer um ajuste manual minucioso desses seis parâmetros para cada nova condição de iluminação ou variação sutil na cor alvo, falhando quando a cor desejada exibe ampla variação de brilho e saturação. 


- K-means:

O método K-Means aborda a segmentação através de `agrupamento de similaridade`, processando os pixels em lotes para encontrar K cores médias (centróides) que representam a imagem. O parâmetro-chave é o número de clusters --k, que define a granularidade da separação. Seu principal benefício é a adaptação a imagens complexas com gradações e misturas de cores, pois ele agrupa automaticamente tonalidades semelhantes. No entanto, é limitado pela sensibilidade ao parâmetro k<2 inadequado pode mesclar o alvo com o fundo. Além disso, a máscara final depende da identificação correta do cluster mais próximo de uma cor alvo "ideal" (verde puro ou azul puro), o que pode ser ambíguo em cenas com muitas cores. Ademais, pode-se observar um aumento significativo no Tempo de Execução do programa conforme o número de centróides definido aumenta.

## Desafios encontrados

O maior desafio foi o ponto departida. Porém, ao desenvolver as  funções que aplicam os algoritmos, o processo ficou mais claro.
Ademais, foi utilizada IA generativa para definir os valroes padões de HSV_RANGES e OVERLAY_COLORS.

## Material referência/inspiração

- https://www.ibm.com/br-pt/think/topics/k-means-clustering


- https://offsouza.medium.com/segmentando-objetos-pela-cor-opencv-487d5181b473