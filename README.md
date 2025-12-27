# Satellite Imagery-Based Property Valuation

A multimodal deep learning system that predicts property prices using both tabular property features and satellite imagery.

## 📁 Project Files

1. **`data_fetcher.ipynb`** - Downloads satellite images using latitude/longitude coordinates from CSV files
2. **`preprocessing.ipynb`** - Cleans and preprocesses tabular data and images, saves to `processed_data.pt`
3. **`model_training.ipynb`** - Trains multimodal models, generates predictions, creates visualizations

## How to Run (Step-by-Step)

### **Step 1: Setup Data**
1. Place your CSV files in `Data/CSV/` folder:
   - `train.csv` - Must contain columns: `id`, `price`, `lat`, `long`, plus property features
   - `test.csv` - Same columns as train (except `price`)

### **Step 2: Get Google Maps API Token**
**CRITICAL STEP**: Before running `data_fetcher.ipynb`:
1. Go to: mailbox.com
2. Generate a free Maps Static API token
3. In `data_fetcher.ipynb`, find this line:
   ```python
   API_KEY = "YOUR_GOOGLE_MAPS_API_KEY_HERE"
