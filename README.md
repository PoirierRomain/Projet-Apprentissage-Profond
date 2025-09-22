![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This repo contains the dataset for a Convolutional Neural Network (CNN) project developed at ENSEEIHT. It aims to classify different types of cheese from images.

**Authors:** Lucas Chatellier, Paul Croizet, Yassine Mehmouden, Romain Poirier

## Project Overview

The goal of this project is to recognize and classify the following cheeses:

- Beaufort
- Comté
- Brie
- Camembert
- Tomme de Savoie
- Morbier
- Roquefort
- Bleu d’Auvergne

We chose these cheeses to cover various types (soft, cooked) and to study distinctions in **color, shape, and texture**. For example, Morbier, Roquefort, and Bleu d’Auvergne are distinguished by color, while Beaufort and Comté require shape analysis, and Camembert vs. Brie requires texture analysis.

## Dataset

- **Images:** 200 images per cheese, totaling 1,600 images.
- **Sources:** Mostly collected from online search engines; Tomme de Savoie also photographed manually.
- **Diversity:** Images include various angles, lighting, and cheese cuts to enhance model generalization.
- **Scripts:** Python scripts included to rename images meaningfully and load the dataset into structured dictionaries.

## Usage

1. Clone the repository:
```bash
git clone https://github.com/PoirierRomain/Projet-Apprentissage-Profond.git
cd Projet-Apprentissage-Profond
```
