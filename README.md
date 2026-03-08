# 🌿 Plant Disease Detection System with Plant Identification

An AI-powered web application built with **PyTorch** and **Flask** that identifies **plant species** and **diagnoses diseases** from leaf images using deep learning. The system uses a fine-tuned **ResNet50** model trained on the **PlantVillage** dataset, achieving **~99.5% accuracy** across 38 classes covering 14 plant species and 26 diseases.

---

## 📋 Table of Contents

- 🔍 [Overview](#overview)
- ✨ [Features](#features)
- 🌿 [Supported Plants & Diseases](#supported-plants--diseases)
- 📁 [Project Structure](#project-structure)
- 👨‍💻 [Tech Stack](#tech-stack)
- 🧠 [Model Architecture](#model-architecture)
- ⚙ [Installation & Setup](#installation--setup)
- 🚀 [Usage](#usage)
- 🎯 [Project Objectives](#project-objectives)
- 📓 [Notebooks](#notebooks)
- 📚 [API Reference](#api-reference)
- 📜 [License](#license)

---

## 🔍Overview

This project was developed as a **Deep Learning college project** with the goal of building an end-to-end plant disease detection pipeline — from data exploration and model training to a fully functional web application. A user simply uploads a photograph of a plant leaf, and the system:

1. **Identifies the plant species** (e.g., Tomato, Potato, Grape)
2. **Detects the disease** (e.g., Early Blight, Late Blight, Bacterial Spot) or confirms the plant is **Healthy**
3. **Displays top-3 predictions** with confidence scores
4. **Provides disease information** including description, treatment recommendations, and severity level

---

## ✨Features

- **Dual Output**: Identifies both plant species and disease from a single prediction
- **Top-3 Predictions**: Shows the three most likely diagnoses with animated confidence bars
- **Disease Information**: Detailed descriptions, treatment recommendations, and severity indicators for all 38 classes
- **Severity Indicators**: Visual badges: ✅ Healthy (green), ⚠️ Mild (orange), 🔴 Severe (red)
- **Drag & Drop Upload**: Intuitive drag-and-drop zone with image preview before submission
- **Sample Gallery**: 7 pre-loaded sample leaf images for one-click instant testing
- **Responsive Design**: Mobile-friendly layout with CSS Grid/Flexbox and media queries
- **Client-Side Validation**: File type (PNG/JPG/JPEG) and size (10 MB max) checks before upload
- **Loading Spinner**: Visual feedback overlay while the model processes the image
- **Plant-Themed UI**: Vibrant green gradient design with animations and smooth transitions

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
plant-disease-detector/
├── app.py                  # Flask web application (routes, file handling)
├── model.py                # Model loading, preprocessing & prediction
├── classes.py              # 38 class names, parse_label(), DISEASE_INFO dict
├── requirements.txt        # Python dependencies with pinned versions
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
│   ├── index.html          # Upload page (drag-drop, sample gallery)
│   └── result.html         # Results page (diagnosis, confidence bars)
│
├── static/
│   ├── css/
│   │   └── style.css       # Plant-themed responsive styling
│   ├── js/
│   │   └── main.js         # Drag-drop, preview, spinner, validation
│   ├── samples/            # 7 sample leaf images for gallery
│   └── uploads/            # Uploaded images saved at runtime
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
| **Deep Learning** | PyTorch, TorchVision |
| **Model** | ResNet50 (Transfer Learning) |
| **Web Framework** | Flask |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **Image Processing** | Pillow (PIL) |
| **Dataset** | PlantVillage (54,305 images, 38 classes) |
| **Data Science** | NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn |
| **Language** | Python 3.10+ |

---

## 🧠Model Architecture

The deployed model is a **ResNet50** pre-trained on ImageNet, fine-tuned on the PlantVillage dataset with a custom fully connected head:

```
ResNet50 (backbone — frozen then fine-tuned)
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
   git clone https://github.com/yash-kakadiya/plant-disease-detector.git
   cd plant-disease-detector
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   # Using conda
   conda create -n plant-disease python=3.10
   conda activate plant-disease

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

## 💡Usage

### Upload a Leaf Image

1. Open the web app in your browser
2. **Drag & drop** a leaf image onto the upload zone, or click **Browse Files** to select one
3. Preview the image, then click **🔬 Analyze Leaf**
4. View the diagnosis results with confidence scores

### Use Sample Images

1. Scroll down to the **"Or Try a Sample Image"** section
2. Click any of the 7 pre-loaded sample images
3. Results appear instantly

### Interpret Results

- **Plant Name**: The identified plant species (e.g., Tomato, Potato)
- **Disease/Condition**: The detected disease or "Healthy" status
- **Confidence Bar**: Green (>85%), Orange (60-85%), Red (<60%)
- **Top-3 Predictions**: Three most likely diagnoses ranked by confidence
- **Severity**: Healthy ✅, Mild ⚠️, or Severe 🔴
- **Disease Info**: Description of the condition and recommended treatment

---

## 🎯Project Objectives

| # | Objective | Status |
|---|-----------|--------|
| 1 | Data Collection & Preprocessing | ✅ Done |
| 2 | Custom CNN Development | ✅ Done |
| 3 | Transfer Learning (ResNet50) | ✅ Done |
| 4 | Model Evaluation & Comparison | ✅ Done |
| 5 | Application Interface (Web App) | ✅ Done |
| 6 | Plant Identification Feature | ✅ Done |
| 7 | Backend Integration & Deployment | ✅ Done |

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

### `GET /`

Renders the upload page with the drag-and-drop zone and sample image gallery.

### `POST /predict`

Accepts a leaf image upload and returns the diagnosis page.

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
| No file uploaded | Flash error → redirect to `/` |
| Invalid file type | Flash error → redirect to `/` |
| Model prediction fails | Flash error → redirect to `/` |
| File too large (>10 MB) | 413 error |

---

## 📄License

This project is licensed under the terms of the license included in the [LICENSE](LICENSE) file.