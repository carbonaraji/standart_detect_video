# 🚀 YOLO Video Object Detection

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Ultralytics YOLO](https://img.shields.io/badge/Ultralytics-YOLOv8-00FFFF)](https://github.com/ultralytics/ultralytics)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green?logo=opencv&logoColor=white)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 🎥 **Мгновенная детекция объектов на видео с помощью нейросетей YOLO.**  
> Скрипт принимает на вход любое видео, обрабатывает его покадрово, рисует рамки (bounding boxes) вокруг найденных объектов и сохраняет результат в новый видеофайл.

---

## ✨ Возможности

- 🧠 **Использование передовых моделей YOLO** (YOLOv8/v11) от Ultralytics.
- 🎬 **Обработка видео любой длины** с сохранением оригинального FPS и разрешения.
- 📺 **Режим реального времени** — параллельно с сохранением, видео выводится в окно предпросмотра.
- ⚙️ **Гибкая настройка** — легко регулировать порог уверенности (Confidence) и IoU.
- 🛑 **Удобное управление** — возможность прервать обработку в любой момент нажатием одной клавиши.

---

## 🛠️ Установка и зависимости

Для работы проекта вам понадобится **Python 3.8+**.

### 1. Клонируйте репозиторий
git clone https://github.com/ваш-username/ваш-репозиторий.git
cd ваш-репозиторий


### 2. Создайте виртуальное окружение (рекомендуется)
bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
### 3. Установите зависимости
Все необходимые библиотеки уже прописаны в файле requirements.txt. Просто выполните:
bash
pip install -r requirements.txt
<details>
<summary>📄 Содержимое <code>requirements.txt</code></summary>

txt
ultralytics>=8.0.0
opencv-python>=4.5.0
numpy>=1.21.0
</details>

### 4. Подготовьте файлы
Скачайте веса модели YOLO (например, yolov8n.pt) с официального сайта Ultralytics и поместите в папку проекта.
Поместите ваше исходное видео (например, input.mp4) в папку проекта.
▶️ Запуск
Откройте файл main.py и измените пути к файлам в начале скрипта:
python
model = YOLO("yolov8n.pt")       # Путь к вашей модели YOLO
VIDEO_PATH = "input.mp4"         # Путь к входному видео
Запустите скрипт:
bash
python main.py
💡 Результат:
Обработанное видео с рамками будет сохранено в файл output_video.mp4 в корне проекта.
Во время обработки откроется окно предпросмотра yoloframe.
⚙️ Настройка параметров
В блоке model.predict() вы можете тонко настроить работу нейросети:
python
results = model.predict( 
    source=frame,      
    conf=0.5,          # 🎯 Порог уверенности (0.0 - 1.0). Чем выше, тем меньше ложных срабатываний.
    iou=0.45,          # 📐 Порог IoU (Intersection over Union) для NMS (подавления дублей рамок).
    save=False,        # ❌ Не сохранять кадры как картинки (мы пишем сразу в видео).
    show=False,        # ❌ Отключаем встроенный показ YOLO (используем свой через cv2).
    verbose=False      # 🔇 Отключает вывод логов в консоль для каждого кадра.
)
💡 Важные нюансы и управление
⌨️ Прерывание работы: Во время вывода видео в окно yoloframe, нажмите клавишу q, чтобы остановить обработку и сохранить уже обработанные кадры.
📁 Пути: Убедитесь, что в VIDEO_PATH указан правильный формат (.mp4, .avi, .mov).
🎞️ Кодеки: Скрипт использует кодек mp4v. Если итоговое видео не открывается в стандартном плеере, попробуйте установить VLC Media Player или измените кодек в коде на avc1 или XVID.

📂 Структура проекта
├── main.py              # Основной скрипт обработки видео
├── requirements.txt     # Список зависимостей проекта
├── yolov8n.pt           # Веса модели YOLO (нужно скачать)
├── input.mp4            # Ваше исходное видео (нужно добавить)
├── output_video.mp4     # Результат работы (появится после запуска)
└── README.md            # Этот файл

🤝 Вклад в проект
Если у вас есть идеи по улучшению (например, добавление трекинга объектов, подсчет скорости или экспорт в другие форматы) — буду рад Pull Request'ам! 🚀
Форкните репозиторий (git checkout -b feature/AmazingFeature)
Закоммитьте изменения (git commit -m 'Add some AmazingFeature')
Запушьте в ветку (git push origin feature/AmazingFeature)
Откройте Pull Request
📄 Лицензия
Распространяется под лицензией MIT. Подробнее см. в файле LICENSE.
<div align="center">
<b>⭐ Не забудьте поставить звезду репозиторию, если проект был полезен! ⭐</b>
</div>
