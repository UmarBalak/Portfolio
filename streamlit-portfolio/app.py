import streamlit as st 
from streamlit_timeline import timeline
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import openpyxl
import base64
from plotly.subplots import make_subplots

### METADATA
st.set_page_config(
    page_title="Umar Balak | Portfolio",
    page_icon="📈",
    layout="wide",
)

### SIDEBAR

st.markdown(
    """
    <style>
    /* Justify text for about me */
    .justified-text {
        text-align: justify;
        margin: 0 15px; /* Adjust the margins for better readability */
    }
    .sidebar-button {
        margin: 20px 0 0 0;
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Whisper&display=swap'); /* Replace with the Whisper font link */

    .custom-font {
        font-family: 'Whisper', sans-serif; 
        font-size: 48px;
        text-align: center;
        margin-bottom: 12px;
        color: black; 
    }
    </style>
    
    <div class="custom-font">
        Harry J. Potter
    </div>
    """,
    unsafe_allow_html=True
)
st.sidebar.caption(
    '''
    <div class="justified-text">
    I am a final-year B.Tech CSE student specializing in AI/ML with a strong academic record.
    My passion for technology led me to develop innovative projects such as an AI Proctor system and an Image classification model.
    With a CGPA of 9.65 and several hackathon wins, including 1st prize in the NASA Space App Challenge, I have honed my skills in Python, TensorFlow, and machine learning.
    I thrive on solving real-world problems through code and am always exploring new challenges.
    </div>
    ''',
    unsafe_allow_html=True
    )
    
# Create 4 columns for the logos with reduced spacing
c1, c2, gmail, github, linkedin, c4, c5= st.sidebar.columns(7)
# Gmail button
gmail.markdown(
    """
    <div class="sidebar-button">
        <a href="mailto:hv@gmail.com" target="_blank" class="button">
            <img src="https://lh3.googleusercontent.com/0rpHlrX8IG77awQMuUZpQ0zGWT7HRYtpncsuRnFo6V3c8Lh2hPjXnEuhDDd-OsLz1vua4ld2rlUYFAaBYk-rZCODmi2eJlwUEVsZgg" alt="Gmail" width="25" height="25">
        </a>
    </div>
    """, 
    unsafe_allow_html=True
)

# GitHub button
github.markdown(
    """
    <div class="sidebar-button">
        <a href="https://github.com/cryobiochem" target="_blank" class="button">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="25" height="25">
        </a>
    </div>
    """, 
    unsafe_allow_html=True
)

# LinkedIn button
linkedin.markdown(
    """
    <div class="sidebar-button">
        <a href="https://www.linkedin.com/in/bmguerreiro/" target="_blank" class="button">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png" alt="LinkedIn" width="25" height="25">
        </a>
    </div>
    """, 
    unsafe_allow_html=True
)

st.sidebar.write('---')

# Resume/CV download button
st.sidebar.markdown(
    """
    <div style="text-align: center; font-size: 12px;">
        A personal portfolio project © 2024.
    </div>
    """,
    unsafe_allow_html=True
)

### CONTENT
aboutme, certs, proj, resume = st.tabs(["About me",
                                    "Certifications",
                                    "Projects", 
                                    "Resume"])


with aboutme:
    ### TIMELINE
    with open('../streamlit-portfolio/timeline.json', "r") as f:
        data = f.read()
    timeline(data, height=600)

with certs:
    c1_img, c1_text = st.columns([2,5])
    with c1_img:
        st.image("https://udemy-certificate.s3.amazonaws.com/image/UC-ZZHX1T1F.jpg?v=1544266446000", use_column_width="auto")

    with c1_text:
        st.markdown("### Data Science A-Z™: Hands-On Exercises | :blue[*SuperDataScience.com* (2018)]")
        st.markdown("The full walkthrough of how to be a data scientist. This course taught me how to clean and prepare data for analysis, perform basic data visualisations, model and curve-fit data & present findings to stakeholders. The **first capstone project** involved advanced data visualization in Tableau to derive insights from Credit Score and Tenure relationships, while performing churn modelling and Chi-Squared testing. The **second capstone project** involved advanced data mining in Microsoft Visual Studio (SSIS/SQL) to deal with ETL Error Handling on a Vehicle Service database containing more than 1 million entries.")

        st.caption("Skills obtained with this certification: [(See certificate here)](https://ude.my/UC-ZZHX1T1F)")
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1: st.info("Data Mining")
        with col2: st.info("Data Visualization")
        with col3: st.info("Tableau")
        with col4: st.info("Gretl")
        with col5: st.info("SSIS")
        with col6: st.info("SQL")

    st.divider()

    c2_img, c2_text = st.columns([2, 5])

    with c2_img:
        st.image("https://i.imgur.com/wUPtNuw.png", use_column_width="auto")

    with c2_text:
        st.markdown("### Data Science Specialization | :blue[*John Hopkins University* (2020)]")
        st.markdown(
            "Covered the concepts and tools for an entire data science pipeline in R programming. Successful participants learn how to use the tools of the trade, think analytically about complex problems, manage large data sets, deploy statistical principles, create visualizations, build and evaluate machine learning algorithms, publish reproducible analyses, and develop data products. The **capstone projects** involved the measuring of atmospheric pollution for assessing societal health problems, and analysis of Fitbit movement activity monitoring to derive activity levels and patterns.")

        st.caption("Skills obtained with this certification: [(See certificate here)](https://coursera.org/share/3543a8a5fd1219abc4e65ffa3856c3a2)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("R programming")
        with col2: st.info("Regression Analysis")
        with col3: st.info("Machine Learning")
        with col4: st.info("Github")

    st.divider()

    c3_img, c3_text = st.columns([2, 5])

    with c3_img:
        st.image("https://i.imgur.com/SNs3nPL.png", use_column_width="auto")
    with c3_text:
        st.markdown("### Deep Learning Specialization | :blue[*deeplearning.ai* (2020)]")
        st.markdown("In this Specialization, I've built neural network architectures such as Convolutional Neural Networks, Recurrent Neural Networks, LSTMs, Transformers, and learned how to make them better with strategies such as Dropout, BatchNorm, and Xavier/He initialization. You mastered these theoretical concepts, learned their industry applications using Python and TensorFlow. As **capstone project**, I tackled real-world cases such as speech recognition, music synthesis, chatbots, machine translation, natural language processing, and more.")
        st.caption(
            "Skills obtained with this certification: [(See certificate here)](https://coursera.org/share/347c89a8fab8b4ddeb55f29674c00d83)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Python")
        with col2: st.info("Deep Learning")
        with col3: st.info("CNNs")
        with col4: st.info("Computer Vision")
        with col5: st.info("NLP")

    st.divider()

    c4_img, c4_text = st.columns([2, 5])
    with c4_img:
        st.image("https://i.imgur.com/XKb0yGo.png", use_column_width="auto")
    with c4_text:
        st.markdown("### TensorFlow Developer | :blue[*deeplearning.ai* (2020)]")
        st.markdown("Following the Deep Learning specialization, I enrolled in a Professional Certificate program to learn how to build and train neural networks using TensorFlow, how to improve network performance using convolutions when trained to identify real-world images, correcting for overfitting using augmentation and dropout, how to teach machines to understand, analyze, and respond to human speech with natural language processing systems. The **capstone projects** involved Customer Sentiment analysis using NLP, and prediction analysis in time-series.")
        st.caption(
            "Skills obtained with this certification: [(See certificate here)](https://coursera.org/share/3e4c0da4f54954f5cca49e43f5433e49)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Python")
        with col2: st.info("Deep Learning")
        with col3: st.info("RNNs")
        with col4: st.info("GRUs")
        with col5: st.info("LSTMs")

    st.divider()

    c5_img, c5_text = st.columns([2, 5])
    with c5_img:
        st.image("https://i.imgur.com/qpbfMVJ.png", use_column_width="auto")
    with c5_text:
        st.markdown("### Responsive Web Design | :blue[*freeCodeCamp* (2020)]")
        st.markdown("As a 300 hour investment lecture, I learned the fundamentals of building websites that work seamlessly across various devices. Several projects were created to show expertise over HTML and CSS programming languages, applied visual design, applied accessibility, web design presentation principles and the creative ways CSS (flexboxes, grids) can be used to enhance user experience.")
        st.caption(
            "Skills obtained with this certification: [(See certificate here)](https://www.freecodecamp.org/certification/brunoguerreiro/responsive-web-design)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Web design")
        with col2: st.info("HTML")
        with col3: st.info("CSS")
        with col4: st.info("Front-end")

    st.divider()

    c6_img, c6_text = st.columns([2, 5])
    with c6_img:
        st.image("https://i.imgur.com/MIu8dX4.png", use_column_width="auto")
    with c6_text:
        st.markdown("### Fundamentals of Digital Marketing | :blue[*Google* (2020)]")
        st.markdown("This Interactive Advertising Bureau-accredited course contained 26 modules created by Google trainers, packed full of practical exercises and real-world examples to help you turn knowledge into action in the field of digital marketing. I learned the concepts of creating an online business, building a strong presence that urges call-to-action, how to optimize search ads, geodemographic personalization of products, connect with customers through various forms of marketing (e-mail, video, paid search, local search), optimize website content and perform decision-making analytics. **This course allowed me to better understand how to present web content online to captivate audiences.**")
        st.caption(
            "Skills obtained with this certification: [(See certificate here)](https://drive.google.com/file/d/1La55rHhtuHFwiEpr3i1o3G1yu9XYgA-I/view?usp=sharing)")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.info("Marketing")
        with col2: st.info("Web design")
        with col3: st.info("e-Commerce")
        with col4: st.info("SEO")
        with col5: st.info("ROI")

with proj:
    # Function to create a container with title, image, and description
    def create_project_container(title, image_url, description):
        st.markdown(f"### {title}")
        st.write(description)
        st.image(image_url, use_column_width=True)
        st.write("---")


    create_project_container("[crystal.ai](https://github.com/cryobiochem/crystal.ai)", "https://i.imgur.com/Huh4fMt.jpg", "Computer vision algorithm able to detect and classify crystals generated in the presence of certain molecules.")


    create_project_container("[Click&Cluster](https://cryobiochem.shinyapps.io/ClickAndCluster/)", "https://i.imgur.com/lkwWcuc.png", "Interactive drawing board with automated K-means clustering algorithm for data classification.")


    create_project_container("[AladdiNLP](https://cryobiochem.shinyapps.io/AladdiNLP/)", "https://i.imgur.com/WjeHJtH.png", "Word recommender system based on NLP, with N-gram tokenization from Twitter, blog posts and news articles.")

st.markdown("""
    <style>
    .right {
        float: right;
        color: #999;
        font-weight: bold;
    }
    .section-header {
        font-size: 22px;
        font-weight: bold;
        color: #4B8BBE;
        margin-bottom: 10px;
        border-bottom: 2px solid #4B8BBE;
        padding-bottom: 5px;
    }
    .skills-header {
        font-size: 18px;
        font-weight: bold;
        color: #4B8BBE;
        margin-bottom: 10px;
        border-bottom: 1px solid #4B8BBE;
        padding-bottom: 5px;
    }
    .expander-header {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .divider {
        border-bottom: 2px solid #ddd;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

with resume:
    st.markdown('<h1 style="background-color:#4B8BBE;color:white;padding:10px;text-align:center;border-radius:10px;">Resume</h1>', unsafe_allow_html=True)
    st.write('')
    # Education Section
    with st.expander("🎓 Education", expanded=True):
        st.markdown('<div class="section-header">Saraswati College Of Engineering</div>', unsafe_allow_html=True)
        st.write("Bachelor of Engineering in Computer Science And Engineering (AIML) with **8.64 CGPA**")
        st.markdown('<div class="right">Navi Mumbai, India | 2021 – 2025</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-header">Anjuman-E-Islam Janjira Jr. College of Science and Arts</div>', unsafe_allow_html=True)
        st.write("*Class XII with 92.50%*")
        st.markdown('<div class="right">Murud, Maharashtra | 2019 – 2021</div>', unsafe_allow_html=True)
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Skills Section with Progress Bars
    with st.expander("🛠️ Skills", expanded=True):
        st.markdown('<div class="skills-header">Programming Languages</div>', unsafe_allow_html=True)
        st.write("**Python, SQL**")

        st.markdown('<div class="skills-header">Libraries / Frameworks</div>', unsafe_allow_html=True)
        st.write("**TensorFlow, Keras, Scikit-Learn, NumPy, Pandas, Streamlit**")

        st.markdown('<div class="skills-header">Tools / Platforms</div>', unsafe_allow_html=True)
        st.write("**Jupyter Notebook, Google Colab, VS Code, Power BI, Git, GitHub**")

        st.markdown('<div class="skills-header">Databases</div>', unsafe_allow_html=True)
        st.write("**MySQL**")


    # Projects Section with Icons and Better Formatting
    with st.expander("🚀 Projects", expanded=True):
        st.markdown('<div class="section-header">AI-driven Proctored Exam System</div>', unsafe_allow_html=True)
        st.write("""
        - A comprehensive system for proctored exams, utilizing advanced AI technologies for real-time monitoring.
        - **Implemented YOLOv8** for background monitoring to detect unauthorized individuals, significantly reducing cheating incidents.
        - Deployed **OpenCV** and **MediaPipe** for eye gaze tracking and head movement detection.
        - **Technologies:** YOLOv8, OpenCV, MediaPipe.
        """)
        
        st.markdown('<div class="section-header">TinyVGG: Image Classification Model Inspired by VGG16</div>', unsafe_allow_html=True)
        st.write("""
        - An optimized image classification model based on the **VGG16 architecture**, designed for efficiency.
        - Trained the model on the **CIFAR-10 dataset**, achieving a classification accuracy of **92%** with a model size of **4MB**.
        - **Technologies:** TensorFlow, Keras, CNN.
        """)

        st.markdown('<div class="section-header">CineMate: Movie Recommendation System</div>', unsafe_allow_html=True)
        st.write("""
        - Created with **K-Nearest Neighbors** and **TF-IDF** to deliver the **top 10 personalized** movie picks.
        - Includes **8,000 top Netflix movies** and **75,000 top TMDB movies**.
        - **Technologies:** KNN, TF-IDF.
        """)
        
        st.markdown('<div class="section-header">MoodMap: Sentiment Analysis Tool</div>', unsafe_allow_html=True)
        st.write("""
        - **Logistic Regression** and **TF-IDF** vectorization used for sentiment categorization.
        - Analyzed over **50,000 movie reviews**, achieving **90% accuracy**.
        """)

    # Experience Section with Date Formatting
    with st.expander("🏅 Experience", expanded=True):
        st.markdown('<div class="section-header">Quasar 2.0 Hackathon - 1st Prize Winner</div>', unsafe_allow_html=True)
        st.write("""
        - Developed AI-driven Proctored Exam System using **YOLOv8** for unauthorized person detection, with **OpenCV** and **MediaPipe** for eye gaze and head tracking.
        """)
        st.markdown('<div class="right">March 2024</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-header">NASA Space App Challenge - 1st Prize Winner</div>', unsafe_allow_html=True)
        st.write("""
        - Created an intelligent project collaboration system with a recommendation engine powered by machine learning.
        """)
        st.markdown('<div class="right">October 2023</div>', unsafe_allow_html=True)

    # Certifications Section with Icons
    with st.expander("🎓 Certifications", expanded=True):
        st.markdown('<div class="section-header">Microsoft Azure AI-900 - Microsoft</div>', unsafe_allow_html=True)
        st.write("Certified in **March 2023**")
        st.markdown('<div class="right">March 2023</div>', unsafe_allow_html=True)