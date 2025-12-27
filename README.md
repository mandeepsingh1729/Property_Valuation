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
   MAPBOX_TOKEN = "YOUR_API_KEY_HERE"
### **Step 3: Run Data Fetcher**
This will:
1. Read latitude/longitude from your CSV files
2. Download satellite images for each property
3. Save images to: Data/images/train/ and Data/images/test/
4. Images are named by property ID (e.g., "12345.jpg")

### **Step 4: Run Preprocessing**
This will:
1. Load and clean tabular data (handle missing values, create new features)
2. Load and resize all satellite images (224x224 pixels)
3. Normalize numerical features, encode categorical variables
4. Save everything to: processed_data.pt

### **Step 5: Run Model Training**
This will:
1. Load processed_data.pt
2. Train multimodal models (CNN for images + MLP for tabular)
3. Implement early stopping based on validation loss
4. Generate test predictions
5. Create training loss visualizations
### **Step 5: Dependencies**
# Install all required packages
pip install torch torchvision pandas numpy scikit-learn matplotlib pillow requests
