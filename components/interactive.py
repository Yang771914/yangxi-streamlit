import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def display_interactive_chart():
    """Display an interactive chart for visualization"""
    st.subheader("Interactive Data Visualization")
    
    # Create options
    chart_type = st.selectbox(
        "Select Chart Type", 
        ["3D Scatter Plot", "Dynamic Bubble Chart", "Radar Chart", "Tree Map"]
    )
    
    # Generate demo data
    if chart_type == "3D Scatter Plot":
        # 生成3D数据
        np.random.seed(42)
        n_points = 100
        x = np.random.normal(0, 1, n_points)
        y = np.random.normal(0, 1, n_points)
        z = np.random.normal(0, 1, n_points)
        size = np.random.uniform(10, 30, n_points)
        
        fig = go.Figure(data=[go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=size,
                color=z,
                colorscale='Viridis',
                opacity=0.8
            )
        )])
        
        fig.update_layout(title="3D Interactive Data Display")
        st.plotly_chart(fig)
        
    elif chart_type == "Dynamic Bubble Chart":
        # Generate time series data
        dates = pd.date_range(start='2023-01-01', periods=20, freq='M')
        categories = ['A', 'B', 'C', 'D']
        
        data = []
        for cat in categories:
            for date in dates:
                data.append({
                    'Date': date,
                    'Category': cat,
                    'Value': np.random.randint(20, 100),
                    'Size': np.random.randint(10, 50)
                })
        
        df = pd.DataFrame(data)
        fig = px.scatter(df, x='Date', y='Value', 
                        size='Size', color='Category',
                        animation_frame=df['Date'].dt.strftime('%Y-%m'),
                        range_y=[0, 100])
        
        st.plotly_chart(fig)
        
    elif chart_type == "Radar Chart":
        # Generate multi-dimensional score data
        categories = ['Innovation', 'Teamwork', 'Technical Skills', 'Communication', 'Project Management', 'Problem Solving']
        values = np.random.uniform(60, 100, len(categories))
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Skill Assessment'
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=False
        )
        
        st.plotly_chart(fig)
        
    else:  # Tree Map
        # Generate hierarchical data
        df = pd.DataFrame([
            ["Skill Tree", "", 0],
            ["Programming", "Skill Tree", 40],
            ["Data Analysis", "Skill Tree", 30],
            ["Project Management", "Skill Tree", 30],
            ["Python", "Programming", 20],
            ["JavaScript", "Programming", 10],
            ["SQL", "Programming", 10],
            ["Data Visualization", "Data Analysis", 15],
            ["Statistical Analysis", "Data Analysis", 15],
            ["Agile Development", "Project Management", 15],
            ["Risk Management", "Project Management", 15]
        ], columns=["id", "parent", "value"])

        fig = px.treemap(df,
                        path=["parent", "id"],
                        values="value",
                        title="Skills Distribution")
        st.plotly_chart(fig)
    
    # Add description
    st.markdown("""
    ### Chart Instructions
    - All charts support interactive operations
    - Hover over to view detailed data
    - Support zoom, pan and rotation (3D charts)
    - Double click to reset view
    """)