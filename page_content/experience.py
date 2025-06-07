import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Overseas Marketing Intern
    **Shenzhen Refond Optoelectronics Co., Ltd.** | *Mar 2024 – Jul 2024*
    
    - Managed LinkedIn and Instagram company accounts, developing content aligned with product positioning and curating the “Mini LED Technology Revealed” series, resulting in a 10%+ increase in followers and shares by semiconductor industry KOLs
    - Coordinated with 50+ overseas tech influencers (YouTube/Instagram), building a collaboration shortlist and supporting over 10 KOL partnerships
    - Led visual materials for international client visits, adapting English product manuals, and designing custom welcome screens using CorelDRAW/Photoshop, supporting 11 international visits
    """)
    
    st.markdown("""
    ### Marketing Intern
    **Foshan Electrical and Lighting Co., Ltd.** | *Nov 2022 – Feb 2023*
    
    - Supported integrated lighting marketing solutions for key accounts, contributing to Huawei ecosystem partnerships, analyzing competitor pricing strategies, and creating standardized product presentations
    - Conducted competitor benchmarking for 5G smart light poles and environmental monitoring, supporting successful project implementation and sharing reusable best practices
    - Proposed content strategies for Douyin’s official account (e.g., factory tours and technical interviews), writing scripts and participating in shoots, doubling video viewership
    """)
    
    st.markdown("""
    ### E-commerce Internship
    **Huizhou NVC Lighting Technology Co., Ltd.** | *Apr 2022 – Jul 2022*
    
    - Managed Douyin marketing for home lighting products, analyzing target audiences and creating themed campaigns such as “Perfect Gifts” and “Ambient Lighting,” achieving top video views of 220,000+ and a 15% follower increase
    - Co-led a Weibo campaign (#EnvisionFutureDesign, EmbraceHealthyLife#) in collaboration with 12 brands, generating 300,000+ impressions
    - Contributed to the full-cycle IP marketing for the “NVC x Line Friends” collaboration series, proposing animated product images for Taobao, resulting in the series becoming a top-3 best-seller
    - Conducted competitive analysis for e-commerce (including Opple and Philips) and drafted differentiated copywriting (e.g., “flicker-free eye protection”), increasing conversion rates by 12%
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Advertising Ecosystem Optimization at QQ Music",
            "description": "Conducted data analysis to identify key drivers of CTR and quantified the role of anti-fraud strategies using multiple regression. Collected and analyzed 300+ user surveys, applying K-means clustering to classify users into 4 behavioral segments and develop targeted ad strategies.",
            "skills": ["Python", "SQL", "SPSS", "K-means", "Survey Analysis"],
            "outcome": "Identified significant variables impacting CTR, verified 'high CTR trap' phenomenon, and developed precise anti-fraud and ad placement strategies."
        },
        {
            "title": "Brand Incubation for Ponpon Lab & 4Tea",
            "description": "Led 0-to-1 strategic development for two brands, refining value propositions with STP, 4P, and CBBE frameworks. Designed immersive experiences and built marketing matrices across TikTok, WeChat, and O2O touchpoints, supported by data-driven optimization via A/B testing and UGC initiatives.",
            "skills": ["Brand Strategy", "Market Research", "Visual Design", "A/B Testing", "UGC"],
            "outcome": "Enhanced customer engagement and achieved GMV growth through experiential marketing and data-driven refinement."
        },
        {
           "title": "ANU Tech-Launcher Participation Study",
           "description": "Designed surveys with Likert and Constant Sum techniques, analyzed 200+ responses using SPSS, and identified 3 key drivers of program engagement through t-tests and regression analysis.",
           "skills": ["SPSS", "Survey Design", "Statistical Analysis", "User Research"],
           "outcome": "Provided actionable insights that boosted user engagement by 23%."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    # Add the interactive visualization demo
    with st.expander("Four Kinds of Interactive Data Visualization", expanded=False):
        st.markdown("**Introduction:** This is an interactive data visualization showcase featuring various visualization types including 3D scatter plots, dynamic bubble charts, radar charts, and skill tree maps. You can explore different visualization effects by selecting different chart types. Each chart supports interactive operations such as zooming, rotating, and data filtering.")
        display_interactive_chart()
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL, JavaScript
        - **Machine Learning:** scikit-learn, TensorFlow, PyTorch
        - **Data Processing:** Pandas, NumPy, PySpark
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
        - **Cloud Platforms:** AWS, Azure, Google Cloud
        - **Web Development:** Django, Flask, React
        - **Image/video processing:** Canva, PS, CDR, AI, iMovie, Jianying
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Collaboration & Leadership:** Proven team player in Agile settings; experienced in leading teams and mentoring peers
        - **Problem-solving:** Strong analytical thinking with ability to thrive in dynamic environments
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        - **Efficiency:** Effective task prioritization and deadline management
        """)
    
    st.markdown("---")