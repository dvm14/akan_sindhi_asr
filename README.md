# Akan–Sindhi Automatic Speech Recognition (ASR)

This repository contains experiments and implementations for building Automatic Speech Recognition (ASR) systems for **Akan (a Ghanaian language)** and **Sindhi (an Indo-Aryan language spoken in Pakistan and India)**. The project explores a naive baseline approach, a classical machine learning approach and an NLP-based approach for speech recognition in low-resource language settings.

Low-resource languages often lack large labeled speech datasets and pretrained models. This project investigates practical approaches to improving ASR performance by combining acoustic feature extraction, traditional speech modeling techniques, and baseline machine learning models.

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
│   Saved models used during experiments.
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
│   │   English Tokenization experiment for Akan.
│   │
│   ├── Twi_twi_tokenizer.ipynb
│   │   Twi Tokenization experiments for AKan.
│   │
│   └── nlp_naive_baseline.ipynb
│       Naive baseline model for the Akan dataset.
│
├── main.py
│   Code for our application
│
├── requirements.txt
│   Python dependencies required to run the project.
│
└── README.md
    Project documentation.
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

We output a random transcription from the training data for each test audio


### Deep leanring Model
We fine-tuned the Whisper-small model, a transformer-based encoder-decoder architecture designed for automatic speech recognition

---

## Technologies Used

- Python  
- Jupyter Notebook  
- NumPy  
- Pandas  
- Librosa for audio feature extraction  
- NLP tokenization utilities  

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

---

## Motivation

Speech recognition technologies primarily support high-resource languages such as English, Mandarin, and Spanish. Many languages remain underserved due to limited datasets and research.

---

## Contributors

Tiffany Degbotse  
Diya Mirji
