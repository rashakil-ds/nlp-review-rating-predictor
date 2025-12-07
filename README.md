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
> “Rashedul is amazing, man! He works at Siemens Energy!”

The model predicts:
- **Stars:** 5⭐
- **Confidence:** 0.9716 


Thank you

