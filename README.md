# 🌿 Leaf Disease Image Captioning ML

An AI-powered Machine Learning project that analyzes plant leaf images and generates meaningful captions using Computer Vision, Deep Learning, and NLP techniques.

The system processes uploaded leaf images, extracts visual patterns, and produces AI-generated descriptive outputs using transformer-based image captioning models.

---

# 🚀 Project Overview

This project combines:
- Image Processing
- Deep Learning
- Hugging Face Transformers
- NLP Caption Generation
- Flask Web Integration

to create an intelligent plant image understanding system.

---

# 🧠 Workflow Architecture

```text
                    ┌──────────────┐
                    │    START     │
                    └──────┬───────┘
                           ↓
              ┌────────────────────────┐
              │ Upload Leaf Image      │
              └──────────┬─────────────┘
                         ↓
              ┌────────────────────────┐
              │ Flask Receives Input   │
              └──────────┬─────────────┘
                         ↓
              ┌────────────────────────┐
              │ Image Preprocessing    │
              │ RGB Conversion         │
              └──────────┬─────────────┘
                         ↓
              ┌────────────────────────┐
              │ Feature Extraction     │
              │ ViTImageProcessor      │
              └──────────┬─────────────┘
                         ↓
              ┌────────────────────────┐
              │ Vision Transformer     │
              │ Extracts Features      │
              └──────────┬─────────────┘
                         ↓
              ┌────────────────────────┐
              │ GPT-2 Decoder          │
              │ Generates Caption      │
              └──────────┬─────────────┘
                         ↓
              ┌────────────────────────┐
              │ Caption Decoding       │
              │ NLP Text Output        │
              └──────────┬─────────────┘
                         ↓
              ┌────────────────────────┐
              │ Display Caption        │
              │ on Web Interface       │
              └──────────┬─────────────┘
                         ↓
                    ┌──────────────┐
                    │    FINISH    │
                    └──────────────┘
```

---

# ⚙️ Real AI Pipeline

```text
Input Image
     ↓
Image Preprocessing
     ↓
Vision Transformer Encoder
     ↓
Feature Embeddings
     ↓
GPT-2 Language Decoder
     ↓
Generated Caption
```

---

# 📂 Project Structure

```bash
Leaf-Disease-Image-Captioning_ML/
│
├── src/                    # Source Code
├── static/
│   └── uploaded_images/
│
├── templates/
│   └── index.html
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── trained/
│
├── notebooks/
├── docs/
├── tests/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🔥 Features

✅ AI-generated image captions  
✅ Transformer-based deep learning workflow  
✅ Flask web application  
✅ Real-time image analysis  
✅ NLP-based text generation  
✅ Hugging Face Transformers integration  
✅ VisionEncoderDecoder architecture  
✅ GPU/CPU support with PyTorch  

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming |
| Flask | Backend Framework |
| PyTorch | Deep Learning |
| Transformers | AI Models |
| ViT-GPT2 | Image Captioning |
| PIL | Image Processing |
| HTML/CSS | Frontend UI |

---

# 🤖 Model Used

### Hugging Face Transformer Model
```text
nlpconnect/vit-gpt2-image-captioning
```

### Architecture
- Vision Transformer (ViT)
- GPT-2 Language Decoder
- Encoder-Decoder Framework

---

# ⚡ Installation

## Clone Repository

```bash
git clone https://github.com/Sabarisekaran/Leaf-Disease-Image-Captioning_ML.git
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate Environment

### Windows
```bash
.venv\Scripts\activate
```

### Linux/macOS
```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
python app.py
```

---

# 🌐 Open in Browser

```text
http://127.0.0.1:5000
```

---

# 📸 How the System Works

1️⃣ User uploads image  
2️⃣ Flask receives image  
3️⃣ Image converted to RGB  
4️⃣ ViT extracts visual features  
5️⃣ GPT-2 generates caption  
6️⃣ NLP decoder converts tokens  
7️⃣ Caption displayed on webpage  

---

# 📚 Learning Outcomes

Through this project, I learned:
- Deep Learning workflows
- Computer Vision pipelines
- NLP caption generation
- Transformer architectures
- Flask backend integration
- AI model inference process

---

# 🚀 Future Improvements

- Multi-language captions
- Better disease-specific captions
- Webcam live prediction
- Voice-based caption output
- Mobile responsive UI
- Advanced deployment pipeline

---

# 👨‍💻 Author

## Sabari Sekaran
B.Tech Artificial Intelligence & Data Science Student

🔗 LinkedIn:
https://www.linkedin.com/in/sabari-sekaran-mu-9238032a3/
