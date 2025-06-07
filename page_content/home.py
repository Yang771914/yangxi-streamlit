import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>YANG Xi</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:yangxi020728@163.com">yangxi020728@163.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.png")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a marketing professional student with both marketing thinking and market insight technical abilities. During my undergraduate studies, I focused on learning marketing theory and honing my ability to apply it to solve business problems, which helped me build a solid foundation. 

        In my graduate studies, I concentrated on learning how to extract market insights through big data, becoming proficient in using programming tools such as Python, R, and Octoparse. I have completed courses in Marketing Management, Digital Marketing, Organizational Marketing, Customer Analysis, Social Media Analytics, and Machine Learning.
        
        I like to describe my strengths as “Inspiration Dynamo”, “Team Glue”, and “Ace Detail Catcher”.  Being good at capturing details helps me to effectively translate creative ideas into practical solutions.  Boarding from a young age has also developed my ability to communicate and collaborate with others, enabling me to act as a bridge in a team. I believe that my unique personal characteristics, solid marketing foundation, and keen market insights will enable me to excel in the company.
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Data Analysis: Pandas, NumPy, Matplotlib, Seaborn
        - Machine Learning: Scikit-learn, TensorFlow, Keras
        - Data Visualization: Tableau, Power BI
        - Design and Video Editing: Canva, PS, CDR, AI, iMovie, Jianying
        - Statistical Analysis: Hypothesis Testing, Regression Analysis
        - Communication: Presentation Skills, Technical Writing
        
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 