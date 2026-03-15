---
license: mit
title: LeafSense
sdk: docker
emoji: 🌿
colorFrom: green
colorTo: blue
short_description: AI-Powered Plant Disease Detection
---
<div align="center">

  <img src="./assets/logo.png" alt="LeafSense Logo" width="120">
  
  # LeafSense
  ### AI-Powered Plant Disease Detection

  [![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
  [![PyTorch](https://img.shields.io/badge/PyTorch-2.5-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
  [![ResNet50](https://img.shields.io/badge/ResNet50-Transfer_Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://arxiv.org/abs/1512.03385)
  [![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

</div>


## 📋 Table of Contents

- 🔍 [Overview](#overview)
- ✨ [Features](#features)
- 🌿 [Supported Plants & Diseases](#supported-plants--diseases)
- 📁 [Project Structure](#project-structure)
- 👨‍💻 [Tech Stack](#tech-stack)
- 🧠 [Model Architecture](#model-architecture)
- ⚙ [Installation & Setup](#installation--setup)
- 💻 [Usage](#usage)
- 🎯 [Project Objectives](#project-objectives)
- 📓 [Notebooks](#notebooks)
- 📚 [API Reference](#api-reference)
- 📜 [License](#license)

---

## 🔍Overview

LeafSense was developed as a learning project with the goal of building an end-to-end plant disease detection pipeline — from data exploration and model training to a polished, production-ready web application. A user simply uploads a photograph of a plant leaf, and the system:

1. **Identifies the plant species** (e.g., Tomato, Potato, Grape)
2. **Detects the disease** (e.g., Early Blight, Late Blight, Bacterial Spot) or confirms the plant is **Healthy**
3. **Displays top-3 predictions** with animated confidence bars
4. **Provides disease information** including description, treatment recommendations, and severity level

---

### 🎥 [Deployed Link: LeafSense](https://yash-77-leafsense.hf.space/)

or

Click below GIF to see project👇

<a href="https://yash-77-leafsense.hf.space/" target="_blank">
  <img src="./assets/banner.gif" alt="LeafSense Images" width="100%">
</a>

#### Google Drive Link: [LeafSense Demo Images](https://drive.google.com/drive/folders/1NS94kByLhVpu6d1ZtQdkCTrnDpDRK-DL?usp=sharing)
---

## ✨Features

- **Multi-Page Architecture**: 5 dedicated pages -> Home, Diagnose, Results, Insights, and About
- **Glassmorphism UI**: Frosted-glass cards, animated background orbs, floating leaf particles, and smooth transitions
- **Dark / Light Theme**: Toggle between themes with instant swap and `localStorage` persistence
- **Dual Output**: Identifies both plant species and disease from a single prediction
- **Top-3 Predictions**: Shows the three most likely diagnoses with animated confidence bars
- **Disease Information**: Detailed descriptions, treatment recommendations, and severity indicators for all 38 classes
- **Severity Indicators**: Visual badges -> ✅ Healthy (green), ⚠️ Mild (orange), 🔴 Severe (red)
- **Drag & Drop Upload**: Intuitive drag-and-drop zone with image preview before submission
- **Sample Gallery**: 7 pre-loaded sample leaf images for one-click instant testing
- **SweetAlert2 Validation**: Client-side file type (PNG/JPG/JPEG) and size (10 MB max) checks with styled popups
- **Fully Responsive**: Mobile-first design with breakpoints at 1024px, 768px, 480px, and 360px + touch device optimizations
- **Loading Spinner**: Visual feedback overlay with backdrop blur while the model processes
- **Model Transparency**: Dedicated Insights page with architecture diagrams, metrics, dataset info, and disease coverage

---

## 🌱Supported Plants & Diseases

The model classifies leaf images into **38 classes** across **14 plant species**:

| # | Plant | Conditions Detected |
|---|-------|-------------------|
| 1 | **Apple** | Apple Scab, Black Rot, Cedar Apple Rust, Healthy |
| 2 | **Blueberry** | Healthy |
| 3 | **Cherry** | Powdery Mildew, Healthy |
| 4 | **Corn (Maize)** | Cercospora Leaf Spot (Gray Leaf Spot), Common Rust, Northern Leaf Blight, Healthy |
| 5 | **Grape** | Black Rot, Esca (Black Measles), Leaf Blight (Isariopsis Leaf Spot), Healthy |
| 6 | **Orange** | Huanglongbing (Citrus Greening) |
| 7 | **Peach** | Bacterial Spot, Healthy |
| 8 | **Pepper (Bell)** | Bacterial Spot, Healthy |
| 9 | **Potato** | Early Blight, Late Blight, Healthy |
| 10 | **Raspberry** | Healthy |
| 11 | **Soybean** | Healthy |
| 12 | **Squash** | Powdery Mildew |
| 13 | **Strawberry** | Leaf Scorch, Healthy |
| 14 | **Tomato** | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Mosaic Virus, Yellow Leaf Curl Virus, Healthy |

---

## 📁Project Structure

```
leaf-sense-detector/
├── app.py                  # Flask application (routes, error handling)
├── model.py                # Model loading, preprocessing & prediction
├── classes.py              # 38 class names, parse_label(), DISEASE_INFO dict
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation (this file)
├── WebApp.md               # Web app development plan
├── LICENSE                 # License file
│
├── models/
│   ├── resnet50_plant.pth  # Trained ResNet50 weights (~99.5% accuracy) ← USED
│   └── custom_cnn.pth      # Trained Custom CNN weights (~98.8% accuracy)
│
├── notebooks/
│   ├── 01_data_exploration.ipynb      # Dataset analysis & visualization
│   ├── 02_custom_cnn_training.ipynb   # Custom CNN architecture & training
│   ├── 03_resnet50_transfer.ipynb     # ResNet50 transfer learning & training
│   └── 04_evaluation.ipynb            # Model comparison & evaluation
│
├── templates/
│   ├── base.html           # Base layout (navbar, footer, particles, theme)
│   ├── index.html          # Home page (hero, features, how-it-works, CTA)
│   ├── diagnose.html       # Diagnose page (upload zone, sample gallery)
│   ├── result.html         # Results page (diagnosis, confidence bars)
│   ├── insights.html       # Model insights (architecture, metrics, coverage)
│   └── about.html          # About page (mission, tech stack, developer)
│
├── static/
│   ├── assets/images/      # Logo and brand assets
│   ├── css/
│   │   └── style.css       # Glassmorphism design system (~2500 lines)
│   ├── js/
│   │   └── main.js         # Theme toggle, drag-drop, animations, SweetAlert2
│   ├── samples/            # 7 sample leaf images for gallery
│   └── uploads/            # Uploaded images (created at runtime)
│
└── dataset/
    └── plantvillage-dataset/
        ├── color/           # RGB images (used for training)
        ├── grayscale/       # Grayscale images
        └── segmented/       # Segmented images
```

---

## 👨‍💻Tech Stack

| Category | Technology |
|----------|-----------|
| **Language** | Python 3.10+ |
| **Deep Learning** | PyTorch, TorchVision |
| **Model** | ResNet50 (Transfer Learning) |
| **Web Framework** | Flask, Jinja2 |
| **Frontend** | HTML5, CSS3 (Glassmorphism), JavaScript (ES6) |
| **UI Libraries** | Font Awesome 6.5, SweetAlert2, Google Fonts (Inter) |
| **Image Processing** | Pillow (PIL) |
| **Dataset** | PlantVillage (54,305 images, 38 classes) |
| **Data Science** | NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn |
| **Deployment** | Hugging Face, Gunicorn, Git |

---

## 🧠Model Architecture

The deployed model is a **ResNet50** pre-trained on ImageNet, fine-tuned on the PlantVillage dataset with a custom fully connected head:

```
ResNet50 (backbone - frozen then fine-tuned)
    └── Custom FC Head:
        ├── Linear(2048 → 512)
        ├── ReLU
        ├── Dropout(0.3)
        └── Linear(512 → 38)
```

### Training Details

| Parameter | Value |
|-----------|-------|
| **Input Size** | 224 × 224 × 3 (RGB) |
| **Optimizer** | Adam |
| **Loss Function** | CrossEntropyLoss |
| **Batch Size** | 32 |
| **Preprocessing** | Resize(224,224) → ToTensor → Normalize(ImageNet) |
| **Data Augmentation** | RandomHorizontalFlip, RandomRotation, ColorJitter |
| **Test Accuracy** | ~99.5% |
| **Device** | CPU (inference) / GPU (training) |

### Inference Pipeline

```
Input Image → Resize(224×224) → ToTensor → Normalize → ResNet50 → Softmax → Top-3 Classes
```

Normalization uses ImageNet statistics:
- **Mean:** [0.485, 0.456, 0.406]
- **Std:** [0.229, 0.224, 0.225]

---

## 🚀Installation & Setup

### Prerequisites

- Python 3.10 or higher
- pip or conda package manager
- ~500 MB disk space (for PyTorch and model weights)

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/yash-kakadiya/leaf-sense.git
   cd leaf-sense
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   # Using conda
   conda create -n leaf-sense python=3.10
   conda activate leaf-sense

   # OR using venv
   python -m venv venv
   source venv/bin/activate        # Linux/Mac
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Verify model file exists**

   Ensure `models/resnet50_plant.pth` is present. This file contains the trained model weights.

5. **Run the application**

   ```bash
   python app.py
   ```

6. **Open in browser**

   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💻Usage

### Upload a Leaf Image

1. Open the web app and navigate to the **Diagnose** page
2. **Drag & drop** a leaf image onto the upload zone, or click **Browse Files** to select one
3. Preview the image, then click **🔬 Analyze Leaf**
4. View the diagnosis results with confidence scores and treatment info

### Use Sample Images

1. On the Diagnose page, scroll to **"Or Try a Sample Image"**
2. Click any of the 7 pre-loaded sample images
3. Results appear instantly

### Explore the App

- **Home**: Overview of LeafSense capabilities, features, and supported plants
- **Diagnose**: Upload interface with drag-and-drop and sample gallery
- **Insights**: Model architecture, performance metrics, training pipeline, and full disease coverage
- **About**: Project mission, technology stack, objectives, and developer info

### Interpret Results

- **Plant Name**: The identified plant species (e.g., Tomato, Potato)
- **Disease/Condition**: The detected disease or "Healthy" status
- **Confidence Bar**: Animated fill with percentage
- **Top-3 Predictions**: Three most likely diagnoses ranked by confidence
- **Severity**: Healthy ✅, Mild ⚠️, or Severe 🔴
- **Disease Info**: Description of the condition and recommended treatment

---

## 🎯Project Objectives

| # | Objective 
|---|-----------
| 1 | Data Collection & Preprocessing 
| 2 | Custom CNN Development 
| 3 | Transfer Learning (ResNet50)
| 4 | Model Evaluation & Comparison
| 5 | Application Interface (Web App)
| 6 | Plant Identification Feature
| 7 | Backend Integration & Deployment

---

## 📓Notebooks

The `notebooks/` directory contains the complete ML/DL pipeline:

| Notebook | Description |
|----------|-------------|
| `01_data_exploration.ipynb` | Dataset statistics, class distribution, sample visualization, image dimension analysis |
| `02_custom_cnn_training.ipynb` | Custom CNN architecture design, training loop, loss/accuracy curves (~98.8% accuracy) |
| `03_resnet50_transfer.ipynb` | ResNet50 transfer learning, fine-tuning strategy, training with augmentation (~99.5% accuracy) |
| `04_evaluation.ipynb` | Side-by-side model comparison, confusion matrices, per-class metrics, final model selection |

---

## 📡API Reference

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page: hero section, features, how-it-works, plant coverage |
| `/diagnose` | GET | Diagnose page: upload zone with drag-and-drop + sample gallery |
| `/predict` | POST | Accepts leaf image upload, returns diagnosis results |
| `/insights` | GET | Model insights: architecture, metrics, dataset info, disease coverage |
| `/about` | GET | About page: mission, tech stack, objectives, developer info |

### `POST /predict`

**Form Data:**
| Field | Type | Description |
|-------|------|-------------|
| `file` | File | Leaf image (PNG, JPG, or JPEG, max 10 MB) |

**Response:** Renders `result.html` with:
- Top prediction (plant name, disease, confidence)
- Top-3 predictions with confidence bars
- Disease information (description, treatment, severity)

**Error Handling:**
| Scenario | Response |
|----------|----------|
| No file uploaded | Flash error → redirect to `/diagnose` |
| Invalid file type | Flash error → redirect to `/diagnose` |
| Model prediction fails | Flash error → redirect to `/diagnose` |
| File too large (>10 MB) | 413 → redirect to `/diagnose` with flash message |

---

## 📜License

This project is licensed under the MIT License - see the [`LICENSE`](LICENSE) file for details.

<br>
<div align="center">
  <b>Developed with 💚 by <a href="https://github.com/Yash-Kakadiya" target="_blank" style="text-decoration:none; color:#F4C430;"> ¥@$# Kakadiya</a></b>
</div>