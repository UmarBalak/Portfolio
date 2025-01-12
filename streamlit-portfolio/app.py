import streamlit as st 
from streamlit_timeline import timeline
from streamlit_option_menu import option_menu

### METADATA
st.set_page_config(
    page_title="Umar Balak | Portfolio",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

custom_css = """
<style>
/* Set the main content to a fixed width and center it */
div[data-testid="stAppViewContainer"] {
    max-width: 1300px; /* Set your desired width */
    margin: auto; /* Centers the container */
    padding-top: 10px; /* Optional: Add space at the top */
    padding-bottom: 10px; /* Optional: Add space at the bottom */
    border-radius: 20px; /* Optional: Add rounded corners */
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

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

page = option_menu(
        menu_title=None,
        options=["About", "Projects"],
        icons = ["person", "bar-chart"],
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
resume_url = "https://raw.githubusercontent.com/UmarBalak/Portfolio/main/streamlit-portfolio/assets/Resume.pdf"
s1, resume, s2 = st.sidebar.columns([1, 3, 1])
resume.markdown(
    f"""
    <div class="sidebar-button" style="text-align: center; margin-top: 15px;">
        <a href="{resume_url}" target="_blank" class="button" style="
            background-color: #FF4B4B; 
            color: white; 
            padding: 8px 15px; 
            border: none; 
            border-radius: 5px; 
            cursor: pointer; 
            font-size: 14px; 
            font-weight: 600; 
            text-decoration: none;
            display: inline-block;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s ease, transform 0.2s ease;">
            <i class="fa-solid fa-file-pdf"></i> Download Resume
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
        st.subheader("CNNCanvas")
        st.markdown("Dynamic Convolutional Neural Network Designer <small style='color:#FF6B6B; margin-left:10px; font-size:0.6em; background-color:#FFF3F3; padding:3px 6px; border-radius:4px;'>Ongoing</small>", unsafe_allow_html=True)
        image_url = "https://raw.githubusercontent.com/UmarBalak/Portfolio/main/streamlit-portfolio/assets/images/cnncanvas.png"
        st.markdown(
            f"""
            <div style="border: 2px solid #FF4B4B; border-radius: 5px; padding: 5px; display: inline-block;">
                <img src="{image_url}" style="display: block; width: 100%; border-radius: 5px;" />
            </div>
            """,
            unsafe_allow_html=True
        )
        with st.expander("More Info", expanded=True):
            st.write("**Description:** An interactive web application for designing and visualizing Convolutional Neural Network architectures.")
            st.write("**Key Features:**")
            st.write("- Dynamic layer configuration")
            st.write("- Real-time parameter and model size estimation")
            st.write("**Technologies:** Python, Streamlit, Machine Learning")
        st.link_button("Try Now", "https://cnncanvas.streamlit.app/")
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
    with col6:
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
        with st.expander("More Info"):
            st.write("**Description:** Created with K-Nearest Neighbors and TF-IDF to deliver the top 10 personalized movie picks.")
            st.write("**Key Features:**")
            st.write("- Personalized top 10 movie recommendations based on user preferences.")
            st.write("- Dataset of 8,000 Netflix movies and 75,000 TMDB movies.")
            st.write("**Technologies:** KNN, TF-IDF")
        st.link_button("Try Now", "https://cinem8.streamlit.app/")
