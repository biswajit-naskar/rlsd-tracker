import pandas as pd 
import random 
from datetime import datetime, timedelta 
from pathlib import Path 
 
def generate_beneficiaries(count=50): 
    villages = ['Baliara', 'Sandeshkhali', 'Gosaba', 'Sagar', 'Bakkhali'] 
    blocks = ['Hingalganj', 'Kakdwip', 'Namkhana', 'Patharpratima'] 
    genders = ['Male', 'Female'] 
    education = ['Primary', 'Secondary', 'Higher Secondary', 'Graduate'] 
    occupations = ['Farmer', 'Fisherman', 'Daily Wage Labor', 'Homemaker'] 
 
    data = [] 
    for i in range(count): 
        age = random.randint(18, 55) 
        block = random.choice(blocks) 
        beneficiary = { 
            'beneficiary_id': f'BEN{str(i+1).zfill(5)}', 
            'full_name': f'Beneficiary_{i+1}', 
            'date_of_birth': (datetime.now() - timedelta(days=age*365)).strftime('%Y-%m-%d'), 
            'gender': random.choice(genders), 
            'contact_number': f'9{random.randint(100000000, 999999999)}', 
            'village': random.choice(villages), 
            'block': block, 
            'district': 'North 24 Parganas' if block == 'Hingalganj' else 'South 24 Parganas', 
            'state': 'West Bengal', 
            'education_level': random.choice(education), 
            'occupation': random.choice(occupations), 
            'family_income': random.randint(20000, 120000), 
            'is_active': True 
        } 
        data.append(beneficiary) 
    return pd.DataFrame(data) 
 
def main(): 
    print("Generating sample data...") 
    data_dir = Path(__file__).parent.parent.parent / 'data' / 'sample_data' 
    data_dir.mkdir(parents=True, exist_ok=True) 
    df = generate_beneficiaries(50) 
    df.to_csv(data_dir / 'sample_beneficiaries.csv', index=False) 
    print(f"Generated {len(df)} beneficiaries") 
 
if __name__ == "__main__": 
    main() 
