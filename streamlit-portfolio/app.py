import streamlit as st 
from streamlit_timeline import timeline
from streamlit_option_menu import option_menu
import time

### METADATA
st.set_page_config(
    page_title="Umar Balak | Portfolio",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;} /* Hides the main menu */
    footer {visibility: hidden;} /* Hides the footer */
    header {visibility: hidden;} /* Hides the header */
    .css-1d391kg {visibility: hidden;} /* Hides the status indicator */
    .css-1v3fvcr {visibility: hidden;} /* Hides the Streamlit watermark */
    .css-1v0mbdj {visibility: hidden;} /* Hides the overall container */
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# if 'loading_animation_shown' not in st.session_state:
#     # Custom CSS to give a coding theme look
#     st.markdown(
#         """
#         <style>
#         /* Importing a programmer-style font */
#         @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&display=swap');

#         /* Loading text styling */
#         .loading-text {
#             font-family: 'Fira Code', monospace;
#             font-size: 40px;
#             color: black;
#             white-space: nowrap;
#             overflow: hidden;
#             border-right: 4px solid; /* Cursor */
#             width: 14ch; /* Control the length of the text animation */
#             animation: typing 1.5s steps(14, end), blink-caret 0.75s step-end infinite;
#             margin-top: 10%;
#             text-align: center;
#             margin-left: auto;
#             margin-right: auto;
#             text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Subtle shadow for contrast */
#         }

#         /* Typing effect */
#         @keyframes typing {
#             from { width: 0 }
#             to { width: 14ch }
#         }

#         /* Blinking cursor */
#         @keyframes blink-caret {
#             from, to { border-color: transparent }
#             50% { border-color: black }
#         }

#         /* Loading bar container */
#         .loading-bar-container {
#             width: 50%;
#             height: 10px;
#             background-color: #e0e0e0;
#             margin: 20px auto;
#             border-radius: 10px;
#             overflow: hidden;
#         }

#         /* Loading bar itself */
#         .loading-bar {
#             height: 100%;
#             width: 0%;
#             background-color: #F16060;
#             border-radius: 10px;
#             animation: load-progress 1.5s linear forwards;
#         }

#         /* Loading bar animation */
#         @keyframes load-progress {
#             0% { width: 0% }
#             100% { width: 100% }
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     # Create a placeholder for the loading message and bar
#     loading_message = st.empty()

#     # Display the loading message with custom HTML/CSS
#     loading_message.markdown(
#         """
#         <div class="loading-text">Hello World!</div>
#         <div class="loading-bar-container">
#             <div class="loading-bar"></div>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
#     # Simulate loading or initialization tasks
#     time.sleep(2)  # Replace with actual setup code if needed

#     st.session_state['loading_animation_shown'] = True

#     # Clear the message after loading
#     loading_message.empty()

page = option_menu(
        menu_title=None,
        options=["About", "Projects", "Resume"],
        icons = ["person", "bar-chart", "share"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

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
# st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Whisper&display=swap'); /* Replace with the Whisper font link */

    .custom-font {
        font-family: 'Whisper', sans-serif; 
        font-size: 46px;
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
    Welcome to my digital playground! I’m a final-year B.Tech student specializing in AI and machine learning. With a strong foundation in Python and expertise in TensorFlow, Keras, and more, I excel at turning complex problems into innovative solutions. My journey includes working on a range of complex AI projects, from developing an AI-driven proctored exam system to creating efficient image classification models. Passionate about pushing technological boundaries and tackling real-world challenges, I am eager to continue exploring new possibilities in AI. Feel free to check out my projects and connect if you’re interested in collaborating or learning more!
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
            <img src="https://lh3.googleusercontent.com/0rpHlrX8IG77awQMuUZpQ0zGWT7HRYtpncsuRnFo6V3c8Lh2hPjXnEuhDDd-OsLz1vua4ld2rlUYFAaBYk-rZCODmi2eJlwUEVsZgg" alt="Gmail" width="20" height="20">
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
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="20" height="20">
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
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png" alt="LinkedIn" width="20" height="20">
        </a>
    </div>
    """, 
    unsafe_allow_html=True
)

if page == "About":
    timeline_data =                 {
                        "title": {
                            "media": {
                            "url": "https://raw.githubusercontent.com/UmarBalak/Portfolio/main/streamlit-portfolio/assets/images/about-pic.jpg",
                            "caption": ""
                            },
                            "text": {
                            "headline": "My Journey",
                            "text": "<p>A timeline of key milestones that highlight my technical growth, problem-solving abilities, and dedication to excellence.<br><b>Discover why I'm prepared to add value to your organization at the conclusion.</b></p>"
                            }


                        },
                        "events": [
                        {
                            "start_date": {
                                "year": "2019",
                                "month": "5"
                            },
                            "text": {
                                "headline": "Scored 88.40% in 10th grade",
                                "text": "<p>Studied in Anjuman Islam Janjira High School for class 10th and scored 88.40% in Maharashtra Board Examination.</p>"
                            }
                        },
                        {
                            "start_date": {
                                "year": "2021",
                                "month": "5"
                            },
                            "text": {
                                "headline": "12th Science with PCMB",
                                "text": "<p>Studied in Anjuman Islam Janjira Jr. College for class 12th and scored 92.50%</p>"
                            }
                        },
                        {
                            "media": {
                                "url": "https://raw.githubusercontent.com/UmarBalak/Portfolio/main/streamlit-portfolio/assets/images/scoe.jpg",
                                "caption": ""
                            },
                            "start_date": {
                                "year": "2021",
                                "month": "6"
                            },
                            "end_date": {
                                "year": "2025",
                                "month": "6"
                            },
                            "text": {
                                "headline": "Saraswati College Of Engineering, Kharghar",
                                "text": "<p>Started pursuing Bachelors of engineering in CSE with specialization Artificial Intelligence and Machine Learning.</p>"
                            }
                        },
                        {
                            "start_date": {
                                "year": "2022",
                                "month": "6"
                            },
                            "text": {
                                "headline": "First Year CGPA: 7.85",
                                "text": "<p>Successfully completed my first year in CSE, achieving a CGPA of 7.85.</p>"
                            }
                        },
                        {
                        "media": {
                            "url": "https://raw.githubusercontent.com/UmarBalak/Portfolio/main/streamlit-portfolio/assets/images/azure-certificate.png",
                            "caption": ""
                        },
                        "start_date": {
                            "year": "2023",
                            "month": "3"
                        },
                        "text": {
                            "headline": "Microsoft Certified: Azure AI Fundamentals (AI-900)",
                            "text": "<p>Demonstrated expertise in foundational knowledge of AI and Machine Learning concepts using Microsoft Azure AI services.</p>"
                        }
                    },
                    {
                            "start_date": {
                                "year": "2023",
                                "month": "6"
                            },
                            "text": {
                                "headline": "Second Year CGPA: 8.63",
                                "text": "<p>Improved my performance in the second year, bringing my CGPA up to 8.63.</p>"
                            }
                        },
                        {
                        "media": {
                            "url": "https://raw.githubusercontent.com/UmarBalak/Portfolio/main/streamlit-portfolio/assets/images/nasa.jpg",
                            "caption": ""
                        },
                        "start_date": {
                            "year": "2023",
                            "month": "10"
                        },
                        "text": {
                            "headline": "Participated in NASA Space App Challenge",
                            "text": "<p>Gained valuable experience by developing an intelligent project collaboration system, applying skills in machine learning and web development.</p>"
                        }
                    },
                        {
                            "media": {
                                "url": "https://raw.githubusercontent.com/UmarBalak/Portfolio/main/streamlit-portfolio/assets/images/quasar.jpg",
                                "caption": ""
                            },
                            "start_date": {
                                "year": "2024",
                                "month": "3"
                            },
                            "text": {
                                "headline": "1st Prize - Quasar 2.0 Hackathon",
                                "text": "<p>Developed an innovative AI Proctored Exam System that excelled in real-time monitoring and cheating detection, securing 1st place.</p>"
                            }
                        },
                        {
                            "start_date": {
                                "year": "2024",
                                "month": "6"
                            },
                            "text": {
                                "headline": "Third Year CGPA: 9.65",
                                "text": "<p>Completed the third year with consistent progress, achieving a CGPA of 9.65, showing my continuous improvement.</p>"
                            }
                        },
                        {
                            "start_date": {
                                "year": "2024",
                                "month": "9"
                            },
                            "text": {
                                "headline": "Onwards and Upwards: Shaping the Future with AI",
                                "text": "<p>Currently working on complex AI projects, focusing on making impactful innovations in federated learning, real-time video processing, and intelligent systems. Stay tuned as I push the boundaries of AI to create technology that transforms industries.</p>"
                            }
                        }
                        ]
                    }
    ### TIMELINE
    data = timeline_data
    c1, c2, c3 = st.columns([1, 30, 1])
    with c2:
        st.header("Career Snapshot")
        timeline(data, height=500)

    st.write("---")

    c4, c5, c6 = st.columns([1, 30, 1])
    with c5:
        st.header("Skills & Technologies")
        st.markdown("""
        <style>
        .pill-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 14px;
            max-width: 100%;
        }

        .pill {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 20px;
            border: 1px solid #FF4B4B;
            font-weight: 600;
            cursor: default;
            transition: background-color 0.3s ease, color 0.3s ease;
            white-space: nowrap;
        }

        .pill:hover {
            background-color: #FF4B4B;
            color: white;
        }

        </style>
        """, unsafe_allow_html=True)

        # Display pills using custom HTML and CSS
        st.markdown("""
        <div class="pill-container">
            <div class="pill">Deep Learning</div>
            <div class="pill">Machine Learning</div>
            <div class="pill">Convolutional Neural Networks (CNN)</div>
            <div class="pill">Python</div>
            <div class="pill">TensorFlow</div>
            <div class="pill">Scikit-Learn</div>
            <div class="pill">Keras</div>
            <div class="pill">Pandas</div>
            <div class="pill">NumPy</div>
            <div class="pill">OpenCV</div>
            <div class="pill">Streamlit</div>
            <div class="pill">SQL</div>
            <div class="pill">MySQL</div>  
            <div class="pill">Git</div>
            <div class="pill">GitHub</div>
            <div class="pill">Jupyter Notebook</div>
            <div class="pill">Power BI</div>
        </div>
        """, unsafe_allow_html=True)

elif page == "Projects":
    # st.header("My Projects")
    st.markdown("<br>", unsafe_allow_html=True)
    a, col1, b, col2, c = st.columns([1, 12, 1, 12, 1])

    # Add content to the first column
    with col1:
        st.subheader("TinyVGG")
        st.markdown("CNN Based Image Classification Model")
        image_url = "https://raw.githubusercontent.com/UmarBalak/Portfolio/main/streamlit-portfolio/assets/images/tinyvgg.png"
        st.markdown(
            f"""
            <div style="border: 2px solid #FF4B4B; border-radius: 5px; padding: 5px; display: inline-block;">
                <img src="{image_url}" style="display: block; width: 100%; border-radius: 5px;" />
            </div>
            """,
            unsafe_allow_html=True
        )
        with st.expander("More Info", expanded=True):
            st.write("**Description:** An optimized image classification model based on the VGG16 architecture, designed for efficiency.")
            st.write("**Key Features:**")
            st.write("- Trained the model on the CIFAR-10 dataset, achieving a classification accuracy of 92%.")
            st.write("- Efficient architecture for smaller resource usage with a model size of 4MB.")
            st.write("**Technologies:** TensorFlow, Keras, CNN")
        st.link_button("Try Now", "https://tinyvgg.streamlit.app/")

    # Add content to the second column
    with col2:
        st.subheader("CineMate")
        st.markdown("Movie Recommendation System")
        image_url = "https://raw.githubusercontent.com/UmarBalak/Portfolio/main/streamlit-portfolio/assets/images/cinemate.png"
        st.markdown(
        f"""
        <div style="border: 2px solid #FF4B4B; border-radius: 5px; padding: 5px; display: inline-block;">
            <img src="{image_url}" style="display: block; width: 100%; border-radius: 5px;" />
        </div>
        """,
        unsafe_allow_html=True
        )
        with st.expander("More Info", expanded=True):
            st.write("**Description:** Created with K-Nearest Neighbors and TF-IDF to deliver the top 10 personalized movie picks.")
            st.write("**Key Features:**")
            st.write("- Personalized top 10 movie recommendations based on user preferences.")
            st.write("- Dataset of 8,000 Netflix movies and 75,000 TMDB movies.")
            st.write("**Technologies:** KNN, TF-IDF")
        st.link_button("Try Now", "https://cinem8.streamlit.app/")
    st.write("---")
    # Add another row with two more expanders
    d, col3, e, col4, f = st.columns([1, 12, 1, 12, 1])

    with col3:
        st.subheader("ProctorVision")
        st.markdown("AI-driven Proctored Exam System")
        image_url = "https://raw.githubusercontent.com/UmarBalak/Portfolio/main/streamlit-portfolio/assets/images/proctorvision.png"
        st.markdown(
            f"""
            <div style="border: 2px solid #FF4B4B; border-radius: 5px; padding: 5px; display: inline-block;">
                <img src="{image_url}" style="display: block; width: 100%; border-radius: 5px;" />
            </div>
            """,
            unsafe_allow_html=True
        )
        with st.expander("More Info"):
            st.write("**Description:** A comprehensive system for proctored exams, utilizing advanced AI technologies for real-time monitoring.")
            st.write("**Key Features:**")
            st.write("- Implemented background monitoring to detect unauthorized individuals.")
            st.write("- Deployed OpenCV and MediaPipe for eye gaze tracking and head movement detection.")
            st.write("**Technologies:** YOLOv8, OpenCV, MediaPipe")
        st.link_button("Try Now", "https://proctorvision.streamlit.app/")

    with col4:
        st.subheader("MoodMapper")
        st.markdown("Sentiment Analysis Tool")
        image_url = "https://raw.githubusercontent.com/UmarBalak/Portfolio/main/streamlit-portfolio/assets/images/moodmapper.png"
        st.markdown(
        f"""
        <div style="border: 2px solid #FF4B4B; border-radius: 5px; padding: 5px; display: inline-block;">
            <img src="{image_url}" style="display: block; width: 100%; border-radius: 5px;" />
        </div>
        """,
        unsafe_allow_html=True
        )
        with st.expander("More Info"):
            st.write("**Description:** Logistic Regression and TF-IDF vectorization used for sentiment categorization.")
            st.write("**Key Features:**")
            st.write("- Analyzed 50,000+ movie reviews, achieving 90% accuracy.")
            st.write("- Categorizes sentiment based on textual input using Logistic Regression.")
            st.write("**Technologies:** Logistic Regression, TF-IDF")
        st.link_button("Try Now", "https://moodmapr.streamlit.app/")
    st.write("---")
    g, col5, h, col6, i = st.columns([1, 12, 1, 12, 1])
    with col5:
        st.subheader("AIML Practical Hub")
        st.markdown("A dedicated platform for BE AIML practicals.")
        image_url = "https://raw.githubusercontent.com/UmarBalak/Portfolio/main/streamlit-portfolio/assets/images/practical-hub.png"
        st.markdown(
            f"""
            <div style="border: 2px solid #FF4B4B; border-radius: 5px; padding: 5px; display: inline-block;">
                <img src="{image_url}" style="display: block; width: 100%; border-radius: 5px;" />
            </div>
            """,
            unsafe_allow_html=True
        )
        with st.expander("More Info"):
            st.write("**Description:** A centralized hub for BE AIML practicals, offering regularly updated code and documentation for student learning.")
            st.write("**Key Features:**")
            st.write("- Provides organized code and comprehensive documentation for each AIML practical.")
            st.write("- Simplifies access to practicals with regularly updated content for seamless learning.")
            st.write("**Technologies:** Python, Streamlit")
        st.link_button("Try Now", "https://beaiml.streamlit.app/")

elif page == "Resume":
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
        color: #FF4B4B;
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
    </style>
    """, unsafe_allow_html=True)
    st.write('')
    c1, c2, c3 = st.columns([1, 25, 1])
    # Education Section
    with c2:
        resume_url = "https://raw.githubusercontent.com/UmarBalak/Portfolio/main/streamlit-portfolio/assets/Resume.pdf"
        st.markdown(
            f"""
            <a href="{resume_url}" download>
                <button style="width:100%; padding:10px; background-color:white; color:#FF4B4B; border:2px solid #FF4B4B; border-radius:5px; cursor:pointer; text-align:center;">Download Resume</button>
            </a>
            """,
            unsafe_allow_html=True
        )
        st.write("---")
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
            st.markdown('<div class="section-sub-header">ProctorVision: AI-driven Proctored Exam System</div>', unsafe_allow_html=True)
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

        