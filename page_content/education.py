import streamlit as st

def education_page():
    st.markdown("## Education")
    
    # 为每所学校创建两列布局
    # CUHK部分
    col1, col2 = st.columns([0.7, 0.3])
    
    with col1:
        st.markdown("""
        ### Master of Science in Marketing
        **The Chinese University of Hong Kong** | QS 36 | *August 2024 - November 2025*
        
        - GPA: 3.4/3.5
        - Research Direction: Big Data marketing
        - Relevant Coursework: Machine Learning in Marketing, Customer Analytics, Social Media Analytics, Organizational Marketing, Strategic Brand Management, Business Negotiation, Marketing Analytics, Marketing Management, Marketing Research, Buyer Behaviour, Big Data Strategy, Digital Marketing
        """)
    
    with col2:
        st.image("static/images/cuhk.jpg", use_column_width=True)
    
    # ANU部分
    col3, col4 = st.columns([0.7, 0.3])
    
    with col3:
        st.markdown("""
        ### Bachelor of Commerce
        **The Australian National University** | QS 30 | *February 2021 - December 2023*
        
        - GPA: 7.0/8.0
        - Specialized field: Marketing
        - Relevant Coursework: Basic Accounting, Brand Management, Marketing Research, Consumer Behavior, e-marketing, Strategic Marketing, International Trade, Export Business Planning
        """)
    
    with col4:
        st.image("static/images/anu.jpg", use_column_width=True)
    
    st.markdown("---")
    
    st.markdown("## Honors and Awards")
    
    cert1, cert2, cert3 = st.columns(3)

    with cert1:
        st.markdown("""
        ### Club Leadership Award
        **The Australian National University** | *June 2024*

        Recognized as the Outstanding Leader of the Year by the 2024 ANU Chinese Students and Scholars Association for my leadership in organizing eight cross-cultural exchange events. 
        """)

    with cert2:
        st.markdown("""
        ### International Business Plan Competition
        **The Australian National University** | *July 2023*

        Led a team to win First Place and a AUD 2,000 prize in the ANU University-wide International Business Plan Competition. The business plan demonstrated a deep understanding of the target market, strong analytical skills in addressing complex business challenges.
        """)

    with cert3:
        st.markdown("""
        ### ANU Excellence Scholarship
        **The Australian National University** | *November 2022*
        
        Awarded based on outstanding academic performance, this competitive scholarship recognizes the recipient's exceptional analytical skills, innovative thinking, and ability to solve complex problems demonstrated in coursework and research projects.
        """)
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### High-End Product Purchase Prediction Model
    - Build a purchase behavior prediction system based on user attributes, focusing on analyzing the impact of marital status on consumption decisions
    - XGBoost algorithm integrated with dynamic threshold optimization and innovative feature engineering
    - 22% increase in high-value user identification rate; married mid-to-high consumption groups exhibit 37% higher purchase probability than average
    
    ### International Business Plan
    - Utilized PEST and a market scoring matrix to accurately identify target markets, and combined SWOT and competitor analyses to develop an LCCP strategy that optimized the website's localization adaptation rate to 90%
    - Developed a brand social media manga marketing strategy, created visual mock-ups, and optimized Naver search advertising—projected to achieve 150,000 impressions. Leveraged data tools to identify three KOLs aligned with the brand
    - Produced an 80-page international expansion proposal featuring 25 strategic recommendations, 76% of which were adopted, supporting the Australian technology company Tiparra's entry into the South Korean e-sports market.
    """)
    
    st.markdown("---")