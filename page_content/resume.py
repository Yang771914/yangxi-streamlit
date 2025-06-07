import streamlit as st
import base64
import os

def resume_page():
    st.markdown("## Download Resume")
    
    col1, col2 = st.columns(2)
    
    with col1:
        cn_pdf_path = os.path.join("static", "docs", "resume_cn.pdf")
        if os.path.exists(cn_pdf_path):
            with open(cn_pdf_path, "rb") as pdf_file:
                cn_PDFbyte = pdf_file.read()
            st.download_button(
                label="Download Chinese Resume",
                data=cn_PDFbyte,
                file_name="YANG_Xi_Resume_CN.pdf",
                mime='application/octet-stream'
            )
        else:
            st.warning("Chinese resume PDF file not found")
    
    with col2:
        en_pdf_path = os.path.join("static", "docs", "resume_en.pdf")
        if os.path.exists(en_pdf_path):
            with open(en_pdf_path, "rb") as pdf_file:
                en_PDFbyte = pdf_file.read()
            st.download_button(
                label="Download English Resume",
                data=en_PDFbyte,
                file_name="YANG_Xi_Resume_EN.pdf",
                mime='application/octet-stream'
            )
        else:
            st.warning("English resume PDF file not found")
    st.title("YANG Xi")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** yangxi020728@163.com
    - **Phone:** (86) 13928107974
    - **Wechat:** 13928107974
    - **Address:** Hubei Road, Luohu District, Shenzhen, Guangdong Province, China

    """)

    st.header("Professional Summary")
    st.markdown("""
    Social media marketing professional with a passion for building authentic brand narratives and fostering genuine connections with audiences. Adept at creating relatable, engaging content that resonates with users and drives brand loyalty. Meticulous about detail and proactive in safeguarding brand integrity, I consistently ensure that every post aligns with core brand values. Eager to leverage my creativity, marketing acumen, and keen market insight to transform your social media presence into a powerful, trust-building dialogue with your audience.
    """)

    st.header("Work Experience")
    st.markdown("""
    **Shenzhen Refond Optoelectronics Co., Ltd.**
    - *Mar 2024 – Jul 2024*
    - Managed LinkedIn and Instagram company accounts, developing content aligned with product positioning
    - Coordinated with 50+ overseas tech influencers, building collaboration partnerships
    - Led visual materials for international client visits

    **Foshan Electrical and Lighting Co., Ltd.**
    - *Nov 2022 – Feb 2023*
    - Supported integrated lighting marketing solutions for key accounts
    - Conducted competitor benchmarking for 5G smart light poles
    - Proposed content strategies for social media accounts

    **Huizhou NVC Lighting Technology Co., Ltd.**
    - *Apr 2022 – Jul 2022*
    - Managed Douyin marketing for home lighting products, achieving 220,000+ views and a 15% follower increase
    - Co-led a Weibo campaign with 12 brands, generating 300,000+ impressions
    - Contributed to IP marketing for the “NVC x Line Friends” series, achieving top-3 best-seller status
    - Conducted e-commerce competitor analysis and drafted differentiated copywriting, increasing conversion rates by 12%
    """)

    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing**
    - The Chinese University of Hong Kong (QS 36)
    - Graduated: November 2025
    - GPA: 3.4/3.5

    **Bachelor of Commerce (Marketing)**
    - The Australian National University (QS 30)
    - Graduated: December 2023
    - GPA: 7.0/8.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, JavaScript, Java, C++
    - **Web Technologies:** HTML, CSS, React, Node.js, Django
    - **Databases:** MySQL, PostgreSQL, MongoDB
    - **Tools:** Git, Docker, Jenkins, AWS
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)

    st.header("Honors and Awards")
    st.markdown("""
    - Club Leadership Award
    - First place in the International Business Plan Competition
    - ANU Excellence Scholarship
    """)

    st.header("Projects")
    st.markdown("""
    **Advertising Ecosystem Optimization at QQ Music**
    - Conducted data analysis to identify key drivers of CTR and quantified the role of anti-fraud strategies using multiple regression. 
    - Collected and analyzed 300+ user surveys, applying K-means clustering to classify users into 4 behavioral segments and develop targeted ad strategies.

    **Brand Incubation for Ponpon Lab & 4Tea**
    - Led 0-to-1 strategic development for two brands, refining value propositions with STP, 4P, and CBBE frameworks. 
    - Designed immersive experiences and built marketing matrices across TikTok, WeChat, and O2O touchpoints, supported by data-driven optimization via A/B testing and UGC initiatives.

     **ANU Tech-Launcher Participation Study**
    - Designed surveys with Likert and Constant Sum techniques.
    - Analyzed 200+ responses using SPSS, and identified 3 key drivers of program engagement through t-tests and regression analysis
    """)

    st.header("Languages")
    st.markdown("""
    - **English:** Native
    - **Spanish:** Intermediate
    """)

    st.markdown("## Interests")
    st.markdown("""
    - Blogging about technology trends
    - Hiking and outdoor activities
    - Baking and pastry making
    """)
    
    st.markdown("### My Baking Gallery")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("static/images/baking1.jpg", use_column_width=True)
    
    with col2:
        st.image("static/images/baking2.jpg", use_column_width=True)
        
    with col3:
        st.image("static/images/baking3.jpg", use_column_width=True)
        
    with col4:
        st.image("static/images/baking4.jpg", use_column_width=True)
    
    st.markdown("---")
