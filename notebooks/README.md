# CapMax Data Science - Week 1: Leads Analysis

## Question
Which lead source brings the most value, and how many leads convert?

## Data
- Raw: `data/raw/leads.csv` (63 rows)
- Clean: `data/clean/leads_clean.csv` (63 rows, 0 duplicates)

## Cleaning (01_cleaning.ipynb)
- Fixed capital letters / spaces in `status` and `source`
- Fixed dates in `lead_created_at`
- Fixed `estimated_value_zar` - removed commas, R, spaces and converted to number
- Removed rows with no `lead_id`

## Key Findings (02_analysis.ipynb)
1. **Referral is #1:** 16 leads, R122,000 value - almost double the next source
2. **Conversion:** 9 Converted out of 63 = 14.3%. Top status is Interested (17 leads, R111,500)
3. **Trend:** Oct 2026 = 41 leads, Nov 2026 = 21 leads

## Recommendation
Focus on Referral programme and follow up the 17 Interested leads fast.

## Limitation
Small sample (63 rows), fictional demo data. Estimated value is not actual sales.

## How to Run
pip install -r requirements.txt
streamlit run app.py 