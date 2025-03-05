import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture

# Streamlit Web Interface with enhanced UI
st.set_page_config(page_title="Women's Healthcare Recommendations", layout="wide")

st.title("Personalized Women's Healthcare Recommendations")
st.subheader("Enter Your Health Details")

# Layout for better UI
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Enter your age:", min_value=18, max_value=100, step=1)
    bmi = st.number_input("Enter your BMI:", min_value=10.0, max_value=50.0, step=0.1)
    physical_activity = st.slider("Rate your physical activity (1-10):", 1, 10, 5)
    mental_health = st.slider("Rate your mental health (1-10):", 1, 10, 5)
    chronic_conditions = st.number_input("Number of chronic conditions:", min_value=0, max_value=10, step=1)

with col2:
    reproductive_health = st.slider("Rate your reproductive health (1-10):", 1, 10, 5)
    hormonal_balance = st.slider("Rate your hormonal balance (1-10):", 1, 10, 5)
    menstrual_cycle = st.selectbox("Menstrual Cycle Regularity:", ["Irregular", "Somewhat Regular", "Regular", "Very Regular"])
    pcos_risk = st.slider("Enter PCOS risk probability (0-1):", 0.0, 1.0, 0.5)
    menopause_stage = st.selectbox("Enter menopause stage:", ["Pre", "Peri", "Post"])
    pregnancy_status = st.selectbox("Enter pregnancy status:", ["Not Pregnant", "Pregnant", "Postpartum"])

if st.button("Get Recommendations"):
    # Convert categorical data to numerical
    mappings = {
        "Menstrual Cycle Regularity": {"Irregular": 1, "Somewhat Regular": 2, "Regular": 3, "Very Regular": 4},
        "Menopause Stage": {"Pre": 0, "Peri": 1, "Post": 2},
        "Pregnancy Status": {"Not Pregnant": 0, "Pregnant": 1, "Postpartum": 2}
    }
    
    user_data = pd.DataFrame([{ 
        'Age': age, 'BMI': bmi, 'Physical_Activity': physical_activity, 'Mental_Health_Score': mental_health,
        'Chronic_Conditions': chronic_conditions, 'Reproductive_Health_Score': reproductive_health,
        'Hormonal_Balance_Score': hormonal_balance,
        'Menstrual_Cycle_Regularity': mappings["Menstrual Cycle Regularity"][menstrual_cycle],
        'PCOS_Risk': pcos_risk,
        'Menopause_Stage': mappings["Menopause Stage"][menopause_stage],
        'Pregnancy_Status': mappings["Pregnancy Status"][pregnancy_status]
    }])
    
    # Simulated dataset for clustering
    np.random.seed(42)
    simulated_data = pd.DataFrame(np.random.rand(20, 11) * [52, 15, 9, 9, 5, 9, 9, 4, 1, 3, 3],
                                  columns=user_data.columns)
    
    df = pd.concat([simulated_data, user_data], ignore_index=True)
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    
    gmm = GaussianMixture(n_components=3, random_state=42)
    gmm_labels = gmm.fit_predict(df_scaled)
    df['Cluster_GMM'] = gmm_labels
    user_cluster = df.iloc[-1]['Cluster_GMM']
    
    def generate_recommendations(cluster):
        recommendations = {
            0: ('Focus on reproductive health, hormonal balance, and mental wellness. Regular gynecological check-ups, balanced diet, and stress management techniques. '
                'Learn more: [Mayo Clinic - Women\'s Health](https://www.mayoclinic.org/healthy-lifestyle)'),
            1: ('Monitor chronic conditions, optimize nutrition, and balance hormones. Consider PCOS screening if at risk. Regular exercise and mental well-being practices are essential. '
                'Resources: [PCOS Awareness Association](https://www.pcosaa.org/)'),
            2: ('Preventive care with focus on menopause management, lifestyle, fitness, and emotional well-being. Incorporate strength training, maintain a heart-healthy diet, and consult specialists for hormonal therapy if needed. '
                'Check out: [North American Menopause Society](https://www.menopause.org/)')
        }
        return recommendations.get(cluster, "No specific recommendations available.")
    
    st.subheader("Your Personalized Recommendation")
    st.write(generate_recommendations(user_cluster))
