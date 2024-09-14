import streamlit as st 
from streamlit_timeline import timeline
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from streamlit_carousel import carousel
import streamlit.components.v1 as components

### METADATA
st.set_page_config(
    page_title="Umar Balak | Portfolio",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)


# components.html(
#     """
# <!DOCTYPE html>
# <html>
# <head>
# <meta name="viewport" content="width=device-width, initial-scale=1">
# <style>
# * {box-sizing: border-box;}
# body {font-family: Verdana, sans-serif;}
# .mySlides {display: none;}
# img {vertical-align: middle;}

# /* Slideshow container */
# .slideshow-container {
#   max-width: 1000px;
#   position: relative;
#   margin: auto;
# }

# /* Caption text */
# .text {
#   color: #f2f2f2;
#   font-size: 15px;
#   padding: 8px 12px;
#   position: absolute;
#   bottom: 8px;
#   width: 100%;
#   text-align: center;
# }

# /* Number text (1/3 etc) */
# .numbertext {
#   color: #f2f2f2;
#   font-size: 12px;
#   padding: 8px 12px;
#   position: absolute;
#   top: 0;
# }

# /* The dots/bullets/indicators */
# .dot {
#   height: 15px;
#   width: 15px;
#   margin: 0 2px;
#   background-color: #bbb;
#   border-radius: 50%;
#   display: inline-block;
#   transition: background-color 0.6s ease;
# }

# .active {
#   background-color: #717171;
# }

# /* Fading animation */
# .fade {
#   animation-name: fade;
#   animation-duration: 1.5s;
# }

# @keyframes fade {
#   from {opacity: .4} 
#   to {opacity: 1}
# }

# /* On smaller screens, decrease text size */
# @media only screen and (max-width: 300px) {
#   .text {font-size: 11px}
# }
# </style>
# </head>
# <body>

# <h2>Automatic Slideshow</h2>
# <p>Change image every 2 seconds:</p>

# <div class="slideshow-container">

# <div class="mySlides fade">
#   <div class="numbertext">1 / 3</div>
#   <img src="https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920" style="width:100%">
#   <div class="text">Caption Text</div>
# </div>

# <div class="mySlides fade">
#   <div class="numbertext">2 / 3</div>
#   <img src="https://unsplash.com/photos/eHlVZcSrjfg/download?force=true&w=1920" style="width:100%">
#   <div class="text">Caption Two</div>
# </div>

# <div class="mySlides fade">
#   <div class="numbertext">3 / 3</div>
#   <img src="https://unsplash.com/photos/zVhYcSjd7-Q/download?force=true&w=1920" style="width:100%">
#   <div class="text">Caption Three</div>
# </div>

# </div>
# <br>

# <div style="text-align:center">
#   <span class="dot"></span> 
#   <span class="dot"></span> 
#   <span class="dot"></span> 
# </div>

# <script>
# let slideIndex = 0;
# showSlides();

# function showSlides() {
#   let i;
#   let slides = document.getElementsByClassName("mySlides");
#   let dots = document.getElementsByClassName("dot");
#   for (i = 0; i < slides.length; i++) {
#     slides[i].style.display = "none";  
#   }
#   slideIndex++;
#   if (slideIndex > slides.length) {slideIndex = 1}    
#   for (i = 0; i < dots.length; i++) {
#     dots[i].className = dots[i].className.replace(" active", "");
#   }
#   slides[slideIndex-1].style.display = "block";  
#   dots[slideIndex-1].className += " active";
#   setTimeout(showSlides, 2000); // Change image every 2 seconds
# }
# </script>

# </body>
# </html> 

#     """,
#     height=600,
# )


### SIDEBAR
st.markdown(
    """
    <style>
    /* Justify text for about me */
    .justified-text {
        text-align: justify;
        margin: 0 15px; /* Adjust the margins for better readability */
        color: #4d4d4d;
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
st.sidebar.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Whisper&display=swap'); /* Replace with the Whisper font link */

    .custom-font {
        font-family: 'Whisper', sans-serif; 
        font-size: 52px;
        text-align: center;
        margin-bottom: 12px;
        color: black; 
    }
    </style>
    
    <div class="custom-font">
        Umar A. Balak
    </div>
    """,
    unsafe_allow_html=True
)
st.sidebar.caption(
    '''
    <div class="justified-text">
    I am a final-year B.Tech CSE student specializing in AI/ML with a strong academic record.
    My passion for technology led me to develop innovative projects such as an AI Proctor system and an Image classification model.
    With a CGPA of 9.65 and several hackathon wins, including 1st prize in the Quasar 2.0 Hackathon, I have honed my skills in Python, TensorFlow, and machine learning.
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
        <a href="mailto:umarbalak35@gmail.com" target="_blank" class="button">
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
        <a href="https://github.com/UmarBalak" target="_blank" class="button">
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
        <a href="https://www.linkedin.com/in/umar-balak/" target="_blank" class="button">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png" alt="LinkedIn" width="25" height="25">
        </a>
    </div>
    """, 
    unsafe_allow_html=True
)

st.sidebar.write('---')

st.sidebar.markdown(
    """
    <div style="text-align: center; font-size: 12px;">
        A personal portfolio project © 2024.
    </div>
    """,
    unsafe_allow_html=True
)

### CONTENT
# aboutme, certs, proj, resume = st.tabs(["About me",
#                                     "Certifications",
#                                     "Projects", 
#                                     "Resume"])
aboutme, proj, resume = st.tabs(["About me",
                                    "Projects", 
                                    "Resume"])
with aboutme:
    ### TIMELINE
    st.header("Career Snapshot")
    with open('../streamlit-portfolio/timeline.json', "r") as f:
        data = f.read()
    timeline(data, height=600)

    st.write("---")

# with certs:
#     c1_img, c1_text = st.columns([2,5])
#     with c1_img:
#         st.image("https://udemy-certificate.s3.amazonaws.com/image/UC-ZZHX1T1F.jpg?v=1544266446000", use_column_width="auto")

#     with c1_text:
#         st.markdown("### Data Science A-Z™: Hands-On Exercises | :blue[*SuperDataScience.com* (2018)]")
#         st.markdown("The full walkthrough of how to be a data scientist. This course taught me how to clean and prepare data for analysis, perform basic data visualisations, model and curve-fit data & present findings to stakeholders. The **first capstone project** involved advanced data visualization in Tableau to derive insights from Credit Score and Tenure relationships, while performing churn modelling and Chi-Squared testing. The **second capstone project** involved advanced data mining in Microsoft Visual Studio (SSIS/SQL) to deal with ETL Error Handling on a Vehicle Service database containing more than 1 million entries.")

#         st.caption("Skills obtained with this certification: [(See certificate here)](https://ude.my/UC-ZZHX1T1F)")
#         col1, col2, col3, col4, col5, col6 = st.columns(6)
#         with col1: st.info("Data Mining")
#         with col2: st.info("Data Visualization")
#         with col3: st.info("Tableau")
#         with col4: st.info("Gretl")
#         with col5: st.info("SSIS")
#         with col6: st.info("SQL")

#     st.divider()

#     c2_img, c2_text = st.columns([2, 5])

#     with c2_img:
#         st.image("https://i.imgur.com/wUPtNuw.png", use_column_width="auto")

#     with c2_text:
#         st.markdown("### Data Science Specialization | :blue[*John Hopkins University* (2020)]")
#         st.markdown(
#             "Covered the concepts and tools for an entire data science pipeline in R programming. Successful participants learn how to use the tools of the trade, think analytically about complex problems, manage large data sets, deploy statistical principles, create visualizations, build and evaluate machine learning algorithms, publish reproducible analyses, and develop data products. The **capstone projects** involved the measuring of atmospheric pollution for assessing societal health problems, and analysis of Fitbit movement activity monitoring to derive activity levels and patterns.")

#         st.caption("Skills obtained with this certification: [(See certificate here)](https://coursera.org/share/3543a8a5fd1219abc4e65ffa3856c3a2)")
#         col1, col2, col3, col4, col5 = st.columns(5)
#         with col1: st.info("R programming")
#         with col2: st.info("Regression Analysis")
#         with col3: st.info("Machine Learning")
#         with col4: st.info("Github")

#     st.divider()

#     c3_img, c3_text = st.columns([2, 5])

#     with c3_img:
#         st.image("https://i.imgur.com/SNs3nPL.png", use_column_width="auto")
#     with c3_text:
#         st.markdown("### Deep Learning Specialization | :blue[*deeplearning.ai* (2020)]")
#         st.markdown("In this Specialization, I've built neural network architectures such as Convolutional Neural Networks, Recurrent Neural Networks, LSTMs, Transformers, and learned how to make them better with strategies such as Dropout, BatchNorm, and Xavier/He initialization. You mastered these theoretical concepts, learned their industry applications using Python and TensorFlow. As **capstone project**, I tackled real-world cases such as speech recognition, music synthesis, chatbots, machine translation, natural language processing, and more.")
#         st.caption(
#             "Skills obtained with this certification: [(See certificate here)](https://coursera.org/share/347c89a8fab8b4ddeb55f29674c00d83)")
#         col1, col2, col3, col4, col5 = st.columns(5)
#         with col1: st.info("Python")
#         with col2: st.info("Deep Learning")
#         with col3: st.info("CNNs")
#         with col4: st.info("Computer Vision")
#         with col5: st.info("NLP")

#     st.divider()

#     c4_img, c4_text = st.columns([2, 5])
#     with c4_img:
#         st.image("https://i.imgur.com/XKb0yGo.png", use_column_width="auto")
#     with c4_text:
#         st.markdown("### TensorFlow Developer | :blue[*deeplearning.ai* (2020)]")
#         st.markdown("Following the Deep Learning specialization, I enrolled in a Professional Certificate program to learn how to build and train neural networks using TensorFlow, how to improve network performance using convolutions when trained to identify real-world images, correcting for overfitting using augmentation and dropout, how to teach machines to understand, analyze, and respond to human speech with natural language processing systems. The **capstone projects** involved Customer Sentiment analysis using NLP, and prediction analysis in time-series.")
#         st.caption(
#             "Skills obtained with this certification: [(See certificate here)](https://coursera.org/share/3e4c0da4f54954f5cca49e43f5433e49)")
#         col1, col2, col3, col4, col5 = st.columns(5)
#         with col1: st.info("Python")
#         with col2: st.info("Deep Learning")
#         with col3: st.info("RNNs")
#         with col4: st.info("GRUs")
#         with col5: st.info("LSTMs")

#     st.divider()

#     c5_img, c5_text = st.columns([2, 5])
#     with c5_img:
#         st.image("https://i.imgur.com/qpbfMVJ.png", use_column_width="auto")
#     with c5_text:
#         st.markdown("### Responsive Web Design | :blue[*freeCodeCamp* (2020)]")
#         st.markdown("As a 300 hour investment lecture, I learned the fundamentals of building websites that work seamlessly across various devices. Several projects were created to show expertise over HTML and CSS programming languages, applied visual design, applied accessibility, web design presentation principles and the creative ways CSS (flexboxes, grids) can be used to enhance user experience.")
#         st.caption(
#             "Skills obtained with this certification: [(See certificate here)](https://www.freecodecamp.org/certification/brunoguerreiro/responsive-web-design)")
#         col1, col2, col3, col4, col5 = st.columns(5)
#         with col1: st.info("Web design")
#         with col2: st.info("HTML")
#         with col3: st.info("CSS")
#         with col4: st.info("Front-end")

#     st.divider()

#     c6_img, c6_text = st.columns([2, 5])
#     with c6_img:
#         st.image("https://i.imgur.com/MIu8dX4.png", use_column_width="auto")
#     with c6_text:
#         st.markdown("### Fundamentals of Digital Marketing | :blue[*Google* (2020)]")
#         st.markdown("This Interactive Advertising Bureau-accredited course contained 26 modules created by Google trainers, packed full of practical exercises and real-world examples to help you turn knowledge into action in the field of digital marketing. I learned the concepts of creating an online business, building a strong presence that urges call-to-action, how to optimize search ads, geodemographic personalization of products, connect with customers through various forms of marketing (e-mail, video, paid search, local search), optimize website content and perform decision-making analytics. **This course allowed me to better understand how to present web content online to captivate audiences.**")
#         st.caption(
#             "Skills obtained with this certification: [(See certificate here)](https://drive.google.com/file/d/1La55rHhtuHFwiEpr3i1o3G1yu9XYgA-I/view?usp=sharing)")
#         col1, col2, col3, col4, col5 = st.columns(5)
#         with col1: st.info("Marketing")
#         with col2: st.info("Web design")
#         with col3: st.info("e-Commerce")
#         with col4: st.info("SEO")
#         with col5: st.info("ROI")


with proj:
    st.header("My Projects")
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    # Add content to the first column
    with col1:
        st.subheader("ProcotrVision")
        with st.expander("AI-driven Proctored Exam System"):
            st.image("https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920", caption="", use_column_width=True)
            st.write("**Description:** A comprehensive system for proctored exams, utilizing advanced AI technologies for real-time monitoring.")
            st.write("**Key Features:**")
            st.write("- Implemented YOLOv8 for background monitoring to detect unauthorized individuals, significantly reducing cheating incidents.")
            st.write("- Deployed OpenCV and MediaPipe for eye gaze tracking and head movement detection.")
            st.write("**Technologies:** YOLOv8, OpenCV, MediaPipe")
            st.write("[View Live Demo](https://your-streamlit-app-url)")

    # Add content to the second column
    with col2:
        st.subheader("TinyVGG")
        with st.expander("Image Classification Model Inspired by VGG16"):
            st.image("https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920", caption="", use_column_width=True)
            st.write("**Description:** An optimized image classification model based on the VGG16 architecture, designed for efficiency.")
            st.write("**Key Features:**")
            st.write("- Trained the model on the CIFAR-10 dataset, achieving a classification accuracy of 92%.")
            st.write("- Efficient architecture for smaller resource usage with a model size of 4MB.")
            st.write("**Technologies:** TensorFlow, Keras, CNN")
            st.write("[View Live Demo](https://your-streamlit-app-url)")

    # Add another row with two more expanders
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("CineMate")
        with st.expander("Movie Recommendation System"):
            st.image("https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920", caption="", use_column_width=True)
            st.write("**Description:** Created with K-Nearest Neighbors and TF-IDF to deliver the top 10 personalized movie picks.")
            st.write("**Key Features:**")
            st.write("- Personalized top 10 movie recommendations based on user preferences.")
            st.write("- Dataset of 8,000 Netflix movies and 75,000 TMDB movies.")
            st.write("**Technologies:** KNN, TF-IDF")
            st.write("[View Live Demo](https://your-streamlit-app-url)")

    with col4:
        st.subheader("MoodMapper")
        with st.expander("Sentiment Analysis Tool"):
            st.image("https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920", caption="", use_column_width=True)
            st.write("**Description:** Logistic Regression and TF-IDF vectorization used for sentiment categorization.")
            st.write("**Key Features:**")
            st.write("- Analyzed 50,000+ movie reviews, achieving 90% accuracy.")
            st.write("- Categorizes sentiment based on textual input using Logistic Regression.")
            st.write("**Technologies:** Logistic Regression, TF-IDF")
            st.write("[View Live Demo](https://your-streamlit-app-url)")


st.markdown("""
    <style>
    .right {
        float: right;
        color: #999;
        font-weight: bold;
    }
    .section-header{
        font-size: 24px;
        font-weight: bold;
        color: #4B8BBE;
    }
    .section-sub-header {
        font-size: 18px;
        font-weight: bold;
        # color: #4B8BBE;
        color: black;
        margin-bottom: 10px;
        border-bottom: 1px solid #4B8BBE;
        padding-bottom: 5px;
    }
    .skills-header {
        font-size: 18px;
        font-weight: bold;
        # color: #4B8BBE;
        color: black;
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
    st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)
    with st.expander("Show/Hide", expanded=True):
        st.markdown('<div class="section-sub-header">Saraswati College Of Engineering</div>', unsafe_allow_html=True)
        st.write("Bachelor of Engineering in Computer Science And Engineering (AIML) with **8.64 CGPA**")
        st.markdown('<div class="right">Navi Mumbai, India | 2021 – 2025</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-sub-header">Anjuman-E-Islam Janjira Jr. College of Science and Arts</div>', unsafe_allow_html=True)
        st.write("Class XII with **92.50%**")
        st.markdown('<div class="right">Murud, Maharashtra | 2019 – 2021</div>', unsafe_allow_html=True)

    # Skills Section with Progress Bars
    st.markdown('<div class="section-header">Skills</div>', unsafe_allow_html=True)
    with st.expander("Show/Hide", expanded=True):
        st.markdown('<div class="skills-header">Programming Languages</div>', unsafe_allow_html=True)
        st.write("Python, SQL")

        st.markdown('<div class="skills-header">Libraries / Frameworks</div>', unsafe_allow_html=True)
        st.write("TensorFlow, Keras, Scikit-Learn, NumPy, Pandas, Streamlit")

        st.markdown('<div class="skills-header">Tools / Platforms</div>', unsafe_allow_html=True)
        st.write("Jupyter Notebook, Google Colab, VS Code, Git, GitHub")

        st.markdown('<div class="skills-header">Databases</div>', unsafe_allow_html=True)
        st.write("MySQL")


    # Projects Section with Icons and Better Formatting
    st.markdown('<div class="section-header">Projects</div>', unsafe_allow_html=True)
    with st.expander("Show/Hide", expanded=True):
        st.markdown('<div class="section-sub-header">AI-driven Proctored Exam System</div>', unsafe_allow_html=True)
        st.write("""
        - A comprehensive system for proctored exams, utilizing advanced AI technologies for real-time monitoring.
        - **Implemented YOLOv8** for background monitoring to detect unauthorized individuals, significantly reducing cheating incidents.
        - Deployed **OpenCV** and **MediaPipe** for eye gaze tracking and head movement detection.
        - **Technologies:** YOLOv8, OpenCV, MediaPipe.
        """)
        
        st.markdown('<div class="section-sub-header">TinyVGG: Image Classification Model Inspired by VGG16</div>', unsafe_allow_html=True)
        st.write("""
        - An optimized image classification model based on the **VGG16 architecture**, designed for efficiency.
        - Trained the model on the **CIFAR-10 dataset**, achieving a classification accuracy of **92%** with a model size of **4MB**.
        - **Technologies:** TensorFlow, Keras, CNN.
        """)

        st.markdown('<div class="section-sub-header">CineMate: Movie Recommendation System</div>', unsafe_allow_html=True)
        st.write("""
        - Created with **K-Nearest Neighbors** and **TF-IDF** to deliver the **top 10 personalized** movie picks.
        - Includes **8,000 top Netflix movies** and **75,000 top TMDB movies**.
        - **Technologies:** KNN, TF-IDF.
        """)
        
        st.markdown('<div class="section-sub-header">MoodMap: Sentiment Analysis Tool</div>', unsafe_allow_html=True)
        st.write("""
        - **Logistic Regression** and **TF-IDF** vectorization used for sentiment categorization.
        - Analyzed over **50,000 movie reviews**, achieving **90% accuracy**.
        """)

    # Experience Section with Date Formatting
    st.markdown('<div class="section-header">Experience</div>', unsafe_allow_html=True)
    with st.expander("Show/Hide", expanded=True):
        st.markdown('<div class="section-sub-header">Quasar 2.0 Hackathon - 1st Prize Winner</div>', unsafe_allow_html=True)
        st.write("""
        - Developed AI-driven Proctored Exam System using **YOLOv8** for unauthorized person detection, with **OpenCV** and **MediaPipe** for eye gaze and head tracking.
        """)
        st.markdown('<div class="right">March 2024</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-sub-header">NASA Space App Challenge</div>', unsafe_allow_html=True)
        st.write("""
        - Created an intelligent project collaboration system with a recommendation engine powered by machine learning.
        """)
        st.markdown('<div class="right">October 2023</div>', unsafe_allow_html=True)

    # Certifications Section with Icons
    st.markdown('<div class="section-header">Certifications</div>', unsafe_allow_html=True)
    with st.expander("Show/Hide", expanded=True):
        st.markdown('<div class="section-sub-header">Microsoft Azure AI-900 - Microsoft</div>', unsafe_allow_html=True)
        st.write("Microsoft Certified: Azure AI Fundamentals")
        st.markdown('<div class="right">March 2023</div>', unsafe_allow_html=True)