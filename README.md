# 🪨📄✂️ Rock Paper Scissors AI

Juego de Piedra, Papel o Tijera contra tu ordenador usando detección de manos en tiempo real



- Detección de gestos de mano en tiempo real con MediaPipe
- Interfaz gráfica personalizada
- Sistema de puntuación
- Contador regresivo de 3 segundos

## Como jugar

1. Presiona `S` para iniciar una ronda
2. Haz tu gesto cuando termine el contador:
   - **Piedra**: Puño cerrado
   - **Papel**: Mano abierta
   - **Tijera**: Dedos índice y medio extendidos
3. El marcador se actualiza automáticamente

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Emmanuel-Edogiawe/Rock_Paper_Scissors_AI.git
cd Rock_Paper_Scissors_AI
```

2. Crea un entorno virtual:
```bash
python -m venv .venv
```

3. Activa el entorno virtual:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso
```bash
python main.py
```

### Controles:
- `S` - Iniciar ronda
- `R` - Reiniciar marcador
- `Q` - Salir

## Estructura del proyecto
```
rock_paper_scissors_ai/
│
├── main.py                 # Archivo principal
├── requirements.txt        # Dependencias
├── README.md              # Documentación
│
└── Resources/             # Recursos gráficos
    ├── BG.png            # Imagen de fondo
    ├── 1.png             # Piedra
    ├── 2.png             # Papel
    └── 3.png             # Tijera
```

## Tecnologías utilizadas

- Python 3.11.9
- OpenCV
- MediaPipe
- CVZone

## 📝 Requisitos

- Webcam
- Python 3.7 o superior
