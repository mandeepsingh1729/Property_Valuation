import pandas as pd
import requests
import os
import time


MAPBOX_TOKEN = "pk.eyJ1IjoiaXR6em1lbWFuZHkiLCJhIjoiY21qYjgwc3BhMDd6MTNkcXZ1M3czNGxvbCJ9.QdtSrdjRj-fPq7MkkXu9mA" 
IMAGE_FOLDER = "mapbox_images"


def download_mapbox_image(lat, lon, property_id, prefix):
    url = f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/{lon},{lat},17,0/400x400"
    
    params = {
        'access_token': MAPBOX_TOKEN,
        'attribution': 'false',
        'logo': 'false'
    }
    
    filename = f'{IMAGE_FOLDER}/{prefix}_{property_id}.jpg'
    
    try:
        response = requests.get(url, params=params, timeout=30)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            return True
        else:
            print(f"  Error {response.status_code} for {filename}")
            if response.status_code == 401:
                print("Error")
            return False
    except Exception as e:
        print(f" Exception for {filename}: {e}")
        return False

def main():
    if not os.path.exists(IMAGE_FOLDER):
        os.makedirs(IMAGE_FOLDER)
    
   
    train_df = pd.read_csv('train.csv')
    test_df = pd.read_csv('test.csv')
    
    total_images = len(train_df) + len(test_df)
    print(f"{total_images} images")
    
    success = 0
    
    
    print("\n TRAIN images...")
    for idx, row in train_df.iterrows():
        property_id = row.get('id', f'train_{idx}')
        if download_mapbox_image(row['lat'], row['long'], property_id, 'train'):
            success += 1
        if idx % 50 == 0:
            print(f"  Progress: {idx+1}/{len(train_df)}")
        time.sleep(0.1)  
    
    
    print("\n TEST images...")
    for idx, row in test_df.iterrows():
        property_id = row.get('id', f'test_{idx}')
        if download_mapbox_image(row['lat'], row['long'], property_id, 'test'):
            success += 1
        if idx % 20 == 0:
            print(f"  Progress: {idx+1}/{len(test_df)}")
        time.sleep(0.1)
    
    print(f"\n Download complete: {success}/{total_images} images")
    print(f"   Saved to: {IMAGE_FOLDER}/")

if __name__ == "__main__":
    main()