# BERT-Based End-to-End NLP Review Rating Predictor  
A NLP pipeline that predicts 1–5 star ratings from text reviews using a fine-tuned DistilBERT model.

---

## Overview

This project implements an end-to-end NLP system that converts raw text reviews into **star ratings (1★–5★)** using a **BERT**-based classifier.

It includes:

- Data preprocessing & stratified splitting  
- DistilBERT fine-tuning for multi-class classification  
- Evaluation (accuracy, precision, recall, F1)  
- Saving/loading inference-ready models  
- FastAPI backend for real-time predictions  
- Streamlit dashboard for user interaction  
- Clean & modular project architecture  

---

## Problem Statement

Given a review such as:

> “The food was excellent, and the service was amazing!”

The model predicts:

- **Stars:** ⭐⭐⭐⭐⭐  
- **Label ID:** 4  
- **Confidence:** 0.92  

---

## Model Files - Not Included in GitHub
models/best_model_distilbert/
├── config.json
├── tokenizer.json
├── tokenizer_config.json
├── vocab.txt
├── special_tokens_map.json
├── model.safetensors
├── label2id.json
└── id2label.json

Thank you

