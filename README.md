# HerHealth - A data driven health recommendations for women

## Overview
HerHealth is a **machine learning-powered healthcare platform** designed to provide **personalized health recommendations** for women. Using **Hierarchical Clustering** and **Gaussian Mixture Models (GMM)**, the system segments users based on their health indicators and provides tailored medical advice and resource links. 

## Features
- **Personalized Health Insights** based on Age, BMI, Menstrual Cycle, Pregnancy Status, and other factors.  
- **Machine Learning-Driven Recommendations** using clustering algorithms.  
- **User-Friendly Web Interface** built with Streamlit.  
- **Links to Credible Medical Resources** for further information.  
- **Scalable & Adaptable** to evolving health trends.  

## How It Works
1. **User Input:** Users enter key health details through a web-based interface.
2. **Data Processing:** The system cleans and normalizes the input data.
3. **Clustering Algorithm:** The ML model segments users into health-based clusters.
4. **Recommendation Engine:** Provides customized health advice and external resource links.
5. **Output Generation:** Displays insights in a user-friendly format.

## Architecture
- **Frontend:** Streamlit (User interface)
- **Backend:** Python (Flask for API handling)
- **Machine Learning:** Scikit-Learn (Hierarchical Clustering & GMM)
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Cloud Deployment:** (Future Scope) AWS/GCP

## Installation & Setup
### Prerequisites
Ensure you have Python **3.7+** installed.

### Steps to Run the Project
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/HerHealth.git
   cd HerHealth
   ```
2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

## Example Usage
- Enter health details (Age, BMI, Cycle Regularity, etc.).
- Click on **Get Recommendations**.
- Receive **personalized health insights** and trusted resource links.

## Future Enhancements
- **Integration with Wearables** for real-time health tracking.
- **AI Chatbot** for instant medical guidance.
- **Telemedicine Integration** for doctor consultations.

## Security & Privacy
- **Data Encryption** to protect user details.
- **Anonymous Processing** without exposing identities.
