# TP4 - Procesamiento de Video 4K con PyTorch

## Descripción

Trabajo práctico de Sistemas Paralelos orientado al procesamiento de video 4K mediante distintas implementaciones:

* Python secuencial
* PyTorch CPU
* PyTorch GPU

El procesamiento se realiza frame por frame para evitar cargar el video completo en memoria.

## Creación del entorno virtual

Desde la carpeta del proyecto:

```bash

```

## Activación del entorno virtual

### Linux

```bash
source venv/bin/activate
```

### Windows (CMD)

```cmd
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

## Instalación de dependencias

```bash
pip install -r requirements.txt
```

Si no existe el archivo requirements.txt:

```bash
pip install opencv-python torch torchvision numpy
```

## Video utilizado

Por cuestiones de tamaño, el video no se encuentra incluido en el repositorio.

Video utilizado para las pruebas:

https://www.magnific.com/es/video-gratis/coliseo-ruinas-fondo_29549#fromView=search&page=1&position=10&uuid=79b72547-54e4-425a-8e57-07bb6c45af66

Características observadas:

* Resolución: 2160 x 3840
* FPS: 60
* Cantidad de frames: 1663
* Duración aproximada: 27.7 segundos

## Estructura del proyecto

```text
tp4-video/
│
├── src/
│   ├── benchmark_lectura.py
│   ├── gris_secuencial.py
│   ├── gris_torch_cpu.py
│   └── gris_torch_gpu.py
│
├── videos/
├── resultados/
├── requirements.txt
└── README.md
```

## Ejecución

Ejemplo:

```bash
cd src
python3 benchmark_lectura.py
```
