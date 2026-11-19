import streamlit as st
import pandas as pd

st.set_page_config(page_title="CapMax Leads Dashboard", layout="wide")
st.title("CapMax - Week 1: Leads Dashboard")
st.write("WebMax Business Intelligence & AI Analytics - Starter Prototype")

# Load data
try:
    df = pd.read_csv("data/clean/leads_clean.csv")
except:
    df = pd.read_csv("data/raw/leads.csv")

# Clean column names just in case
df.columns = [c.strip().lower() for c in df.columns]

# --- 5 BUSINESS INDICATORS ---
df['estimated_value_zar'] = pd.to_numeric(df['estimated_value_zar'], errors='coerce') 
total_leads = len(df)
total_value = df['estimated_value_zar'].sum()
converted = len(df[df['status'].str.lower() == 'converted'])
conversion_rate = (converted / total_leads * 100) if total_leads > 0 else 0
avg_value = df['estimated_value_zar'].mean()
interested = len(df[df['status'].str.lower() == 'interested'])

col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Total Leads", total_leads)
col2.metric("Total Value (ZAR)", f"R{total_value:,.0f}")
col3.metric("Converted Leads", converted)
col4.metric("Conversion Rate", f"{conversion_rate:.1f}%")
col5.metric("Avg Deal Value", f"R{avg_value:,.0f}")
col6.metric("Interested Leads", interested) 
value_by_source = df.groupby('source')['estimated_value_zar'].sum().sort_values(ascending=False)
st.bar_chart(value_by_source)
st.write("**Finding:** Referral is #1 with R122,000 - almost double the next source.")

# --- CHART 2: Leads by Status ---
st.subheader("2. Leads by Status")
leads_by_status = df.groupby('status').size()
st.bar_chart(leads_by_status)
st.write("**Finding:** Interested is the biggest group (17 leads, R111,500). Follow them up fast.")

# --- CHART 3: Trend by Month (bonus) ---
st.subheader("3. Leads per Month")
df['lead_created_at'] = pd.to_datetime(df['lead_created_at'], errors='coerce')
df['month'] = df['lead_created_at'].dt.to_period('M').astype(str)
leads_by_month = df.groupby('month').size()
st.line_chart(leads_by_month)
st.write("**Finding:** Oct 2026 = 41 leads, Nov 2026 = 21 leads.")

st.divider()
st.write("**Recommendation:** Focus on Referral programme and follow up the 17 Interested leads fast.")
st.write("**Limitation:** Small sample (63 rows), fictional demo data. Estimated value is not actual sales.") 
