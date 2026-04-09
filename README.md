# CS5814 HW3 — Relation Classification on NYT29

## Requirements
- Python 3.8+
- PyTorch
- Hugging Face Transformers
- scikit-learn

Install dependencies:
    pip install transformers datasets scikit-learn

## Dataset
Download the NYT29 dataset from Kaggle:
    https://www.kaggle.com/datasets/chandrasekhardcs/nyt29-dataset

Unzip and place the files in a folder called `nyt29/` in the same directory as the notebook.
The folder should contain: train.sent, train.tup, dev.sent, dev.tup, test.sent, test.tup

## How to Run
1. Open the notebook in Google Colab
2. Set the runtime to GPU (Runtime → Change runtime type → T4 GPU)
3. Run all cells in order from top to bottom
4. Training takes approximately 20 minutes for 5 epochs on a T4 GPU
5. The best model checkpoint is saved automatically as best_model.pt

## Model
- Architecture: bert-base-uncased with typed entity markers
- Classifier head: concat([CLS], [E1], [E2]) → Dropout → Linear
- Loss: BCEWithLogitsLoss (multi-label)
- Prediction threshold: 0.71 (tuned on dev set)

## Results
| Split | Micro-F1 | Macro-F1 |
|-------|----------|----------|
| Train | 0.9984   | 0.9197   |
| Dev   | 0.9662   | 0.7678   |
| Test  | 0.8905   | 0.5973   |
