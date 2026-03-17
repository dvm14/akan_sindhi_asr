# **Live Demo App**
**Try the ASR system here:**  
**https://akansindhiasr-production.up.railway.app/**

---

# Akan–Sindhi Automatic Speech Recognition (ASR)

This repository contains experiments and implementations for building Automatic Speech Recognition (ASR) systems for **Akan (a Ghanaian language)** and **Sindhi (an Indo-Aryan language spoken in Pakistan and India)**. The project explores a naive baseline approach, a classical machine learning approach, and a deep learning approach for speech recognition in low-resource language settings.

Low-resource languages often lack large labeled speech datasets and pretrained models. This project investigates practical approaches to improving ASR performance by combining acoustic feature extraction, traditional speech modeling techniques, and modern transformer-based ASR models.

---

## Project Goals

- Build speech recognition pipelines for **Akan** and **Sindhi**
- Explore **classical machine learning ASR techniques**
- Develop **baseline models for low-resource speech recognition**
- Develop **deep learning ASR techniques**
- Compare modeling approaches across different languages
- Analyze challenges in ASR for underrepresented languages

---

## Repository Structure

```
akan_sindhi_asr/
│
├── models/
│   Documentation and references for trained models.
│
│   └── models.md
│       Links to fine-tuned Whisper ASR models hosted on Hugging Face.
│
├── notebooks/
│   Jupyter notebooks containing experiments and model development.
│
│   ├── ClassicalMlProject_Akan.ipynb
│   │   Classical ML ASR pipeline for Akan speech recognition.
│   │
│   ├── ClassicalMlProject_Sindhi.ipynb
│   │   Classical ML ASR pipeline for Sindhi speech recognition.
│   │
│   ├── NLP_asr_sindhi.ipynb
│   │   NLP-based ASR experiments for Sindhi.
│   │
│   ├── Twi_english_tokenizer.ipynb
│   │   English tokenizer experiment for Akan.
│   │
│   ├── Twi_twi_tokenizer.ipynb
│   │   Twi tokenizer experiments for Akan.
│   │
│   └── nlp_naive_baseline.ipynb
│       Naive baseline model for the Akan dataset.
│
├── static/
│   Files used for the live inference demo interface.
│
│   ├── samples/
│   │   Example audio samples used in the demo.
│   │
│   │   ├── akan.wav
│   │   └── sindhi.wav
│   │
│   └── index.html
│       Frontend interface for testing the ASR models.
│
├── main.py
│   Backend application used for running ASR inference.
│
├── requirements.txt
│   Python dependencies required to run the project.
│
└── README.md
    Project documentation.
```

---

## Datasets

We loaded the datasets for each language through hugging face from these dataset links:
- Akan: https://huggingface.co/datasets/google/WaxalNLP under subset "aka_asr"
- Sindhi: https://huggingface.co/datasets/google/fleurs under "sd_in"

(We did not need to keep the data locally)

---

## Pretrained Models

Fine-tuned Whisper models trained during this project are available on Hugging Face.

### Akan Models

- **Whisper-small (English tokenizer)**  
  https://huggingface.co/tiffany101/whisper-small

- **Whisper-small (Twi tokenizer)**  
  https://huggingface.co/tiffany101/whisper-twi-v2

### Sindhi Models

- **Whisper-small (Sindhi tokenizer)**  
  https://huggingface.co/dvm14/whisper-small-sindhi

- **Whisper-small (English tokenizer)**  
  https://huggingface.co/dvm14/whisper-small-nosindhi

link to models can also be found in:

```
models/models.md
```

---

## Methodology Overview

The project explores several components commonly used in speech recognition systems.

### Acoustic Feature Extraction

Raw speech signals are converted into compact acoustic representations using **Mel-frequency cepstral features (MFCCs)** or **log Mel spectrograms**. These features capture spectral properties of speech that are important for recognition. Delta and delta-delta features are often added to capture temporal dynamics.

### Acoustic Modeling

The acoustic model learns to associate acoustic patterns with linguistic units such as characters or phonemes. Classical pipelines explored in this project include **Gaussian Mixture Model – Hidden Markov Model (GMM-HMM)** architectures and other machine learning classifiers.

### Language Modeling and Decoding

Language models incorporate linguistic context during decoding. Character-level **n-gram models** are trained from transcription data to estimate the probability of character sequences and improve transcription quality.

### Baseline Model

As a simple baseline, the system outputs a random transcription from the training set for each test audio sample. This provides a lower bound for evaluating more sophisticated models.

### Deep Learning Model

We fine-tuned **Whisper-small**, a transformer-based encoder-decoder architecture designed for automatic speech recognition. Fine-tuning allows the model to adapt to low-resource languages such as Akan and Sindhi.

---

## Technologies Used

- Python  
- Jupyter Notebook  
- NumPy  
- Pandas  
- Librosa (audio feature extraction)  
- Hugging Face Transformers  
- Whisper ASR models  

---

## Installation

Clone the repository:

```bash
git clone https://github.com/dvm14/akan_sindhi_asr.git
cd akan_sindhi_asr
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Experiments

Most experiments are implemented in the notebooks.

Open the notebooks in the `notebooks/` directory and run the cells sequentially.

Example:

```
notebooks/ClassicalMlProject_Akan.ipynb
notebooks/ClassicalMlProject_Sindhi.ipynb
```

---

## Motivation

Speech recognition technologies primarily support high-resource languages such as English, Mandarin, and Spanish. Many languages remain underserved due to limited datasets and research.

Improving ASR for languages such as **Akan** and **Sindhi** helps make speech technologies more inclusive and accessible, while also advancing research on speech recognition for low-resource languages.

---

## Contributors

**Tiffany Degbotse**  
**Diya Mirji**
