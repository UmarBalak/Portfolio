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
    page_title="Umar A. Balak | Portfolio",
    page_icon="📈",
    layout="wide",
)

### SIDEBAR
# st.sidebar.markdown('<div style="text-align: left; margin-bottom: 12px"><a href="https://guerreiro.streamlit.app/">''<img src="https://i.imgur.com/t3cH48K.png" alt="Name" width="250">'
#     '</a></div>', unsafe_allow_html=True)
st.sidebar.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Whisper&display=swap'); /* Replace with the Whisper font link */

    .custom-font {
        font-family: 'Whisper', sans-serif; /* Apply Whisper font */
        font-size: 36px;
        text-align: left;
        margin-bottom: 12px;
        color: black; /* Adjust color if needed */
    }
    </style>
    
    <div class="custom-font">
        Umar A. Balak
    </div>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown("##### A personal portfolio project © 2024.")
st.sidebar.caption(
    "I am a final-year B.Tech CSE student specializing in AI/ML with a strong academic record. "
    "My passion for technology led me to develop innovative projects such as an AI Proctor system and a TinyVGG-based image classification model. "
    "With a CGPA of 9.65 and several hackathon wins, including 1st prize in the NASA Space App Challenge, I have honed my skills in Python, TensorFlow, and machine learning. "
    "I thrive on solving real-world problems through code and am always exploring new challenges. ")
    
# Create 4 columns for the logos with reduced spacing
c1, c2, gmail, github, linkedin, c4, c5= st.sidebar.columns(7)

# Add clickable logos side by side for Gmail, Google Scholar, Github, and Linkedin with reduced spacing
gmail.markdown('<div style="text-align: left"><a href="https://mail.google.com/mail/u/0/?view=cm&fs=1&to=guerreiro.bms@gmail.com&su=New%20job%20opportunity%20for%20Bruno%20M.%20Guerreiro" target="_blank">'
    '<img src="https://lh3.googleusercontent.com/0rpHlrX8IG77awQMuUZpQ0zGWT7HRYtpncsuRnFo6V3c8Lh2hPjXnEuhDDd-OsLz1vua4ld2rlUYFAaBYk-rZCODmi2eJlwUEVsZgg" alt="Gmail" width="32" height="32">'
    '</a></div>', unsafe_allow_html=True)
github.markdown('<div style="text-align: left"><a href="https://github.com/cryobiochem" target="_blank">'
    '<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="Github" width="32" height="32">'
    '</a></div>', unsafe_allow_html=True)
linkedin.markdown('<div style="text-align: left"><a href="https://www.linkedin.com/in/bmguerreiro/" target="_blank">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png" alt="LinkedIn" width="32" height="32">'
    '</a></div>', unsafe_allow_html=True)

st.sidebar.write('')

# Resume/CV download button
st.sidebar.markdown(f'<a href="https://pouch.jumpshare.com/download/vP2xyACw55AUc-mr9IdBV0s2oNr9koOjYp5Wig6F4O_dhDGJS_bpYbGOeQIzCkLCQSWYV-nC3-IH4CkRIJWpzA" download="Resume_CV.pdf"><button style="cursor: pointer; padding: 10px; border: none; border-radius: 5px;">Download CV</button></a>', unsafe_allow_html=True)
st.sidebar.caption("📌 Based in Mumbai/India")

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

st.write('---')
st.markdown('<div style="text-align: right;"><sub>Umar A. Balak © 2024</sub></div>', unsafe_allow_html=True)

with resume:
    st.markdown('#### Implications of a polysaccharide gel undercooler in Classical Nucleation Theory')

    # Authors & Affiliations
    #st.markdown('B. M. Guerreiro¹²*, M.M. Dionísio³, J.C. Lima³, J.C. Silva⁴, F. Freitas¹²*')
    #st.markdown('¹UCIBIO – Applied Molecular Biosciences Unit, Department of Chemistry, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
    #st.markdown('²Associate Laboratory i4HB - Institute for Health and Bioeconomy, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
    #st.markdown('³LAQV-REQUIMTE, Department of Chemistry, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
    #st.markdown('⁴CENIMAT/I3N, Department of Physics, School of Science and Technology, NOVA University Lisbon, Caparica, Portugal')
    #st.write('*Corresponding authors.')
    #st.write('---')
    #st.header('Thermodynamic Rationale')
    #st.write('During solidification, the atomic arrangement changes from a random or short-range order to a long range order or crystal structure. Nucleation occurs when a small nucleus begins to form in the liquid, the nuclei then grows as atoms from the liquid are attached to it. The crucial point is to understand it as a balance between the free energy available from the driving force (volumetric free energy, **VFE**), and the energy consumed in forming new interface (interfacial energy, **IE**).')







    with st.expander('Energetics of Ice Nucleation'):
        st.write('The nucleation activation energy barrier $\Delta G_n$ is an energetic balance between opposing contributions. When a cluster of a new phase forms, the system decreases its free energy. This is the :blue[driving force] for nucleation and is directly proportional to the volume of the cluster, or $n$:')
        st.latex(r'-\frac{4}{3} \pi r ^ 3 \Delta G_v')

        st.write('In contrast, forming an interface between the parent phase and the new cluster has an :red[energetic cost], proportional to the surface area of the cluster, or $n^{2/3}$:')
        st.latex(r'4\pi r^2 \gamma_{\text{SL}}')

        st.write('The system will follow the :green[energy barrier landscape], which can be expressed by a combination of gain and cost functions:')
        st.latex(r'\Delta G_n = -\frac{4}{3} \pi r^3 \Delta G_v + 4\pi r^2 \gamma_{SL}')

        st.subheader('Critical and equilibrium radii, $r^*$ and $r_{eq}$')
        st.markdown('- At $r < r^*$, clusters will grow and decay continuously, due to thermal fluctuations.')
        st.markdown('- When $r = r^*$, a cluster that gains a single atom will overcome the energy barrier to transition to a stable nuclei than can grow. The radius $r^*$ is the minimum size a nuclei can possess in the system.')
        st.markdown('- At $r > r^*$, we have still in non-spontaneous $\Delta G > 0$ territory. Here, the stable nuclei will grow up to a max radius of $r_{eq}$, which is when $\Delta G_n = \Delta G = 0$. $r_{eq}$ is called the equilibrium radius when it occurs when the system reaches thermodynamic equilibrium, but it is not the center point in a Boltzmann distribution of nuclei sizes. When the negative free energy landscape begins, crystallization is finally spontaneous and can proceed to bigger sizes.')
        st.write('---')


        def calculate_curves(delta_G_v, gamma_SL, r):
            InterfacialEnergy = 4 * np.pi * r ** 2 * gamma_SL
            VolumeFreeEnergy = -4 / 3 * np.pi * r ** 3 * delta_G_v
            NucleationEnergyBarrier = -4 / 3 * np.pi * r ** 3 * delta_G_v + 4 * np.pi * r ** 2 * gamma_SL
            return InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier
        def find_equilibrium_radius(r, NucleationEnergyBarrier):
            zero_crossings = np.where(np.diff(np.sign(NucleationEnergyBarrier)))[0]
            valid_zero_crossings = zero_crossings[NucleationEnergyBarrier[zero_crossings] != 0]
            if len(valid_zero_crossings) > 0:
                r_equilibrium = r[valid_zero_crossings[0]]
                return r_equilibrium
            else:
                return None
        def find_critical_radius(r, NucleationEnergyBarrier):
            peak_index = np.argmax(NucleationEnergyBarrier)
            r_critical = r[peak_index]
            return r_critical


        col1, col2 = st.columns(2)

        with col1:
            # Create sliders for the variables
            gamma_SL = st.slider("$\gamma$", min_value=0.00, max_value=1.00, value=0.90,
                                 step=0.01, key='nucleation1')

        with col2:
            delta_G_v = st.slider("$\Delta G_v$", min_value=0.000, max_value=0.400,
                                  value=0.270, step=0.001, key='nucleation2')

        # Generate random r values
        r = np.linspace(0, 100, 1000)

        # Calculate the curves
        InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier = calculate_curves(delta_G_v, gamma_SL, r)

        # Create a pandas DataFrame with r and curve values
        data = {"r": r, "Interfacial energy": InterfacialEnergy, "Volumetric free energy": VolumeFreeEnergy,
                "Nucleation barrier": NucleationEnergyBarrier}
        df = pd.DataFrame(data)

        # Use Plotly Express to create an interactive line plot
        fig = px.line(df, x="r", y=["Interfacial energy", "Volumetric free energy", "Nucleation barrier"],
                      color_discrete_map={"Interfacial energy": "red", "Volumetric free energy": "blue",
                                          "Nucleation barrier": "green"})
        # Update layout and axes ranges
        fig.update_layout(title="", xaxis_title="r", yaxis_title="&#8710;G",
                          # https://www.toptal.com/designers/htmlarrows/math/
                          yaxis_range=[-200, 200], xaxis_range=[0, 12])

        # Plot equilibrium radius
        r_equilibrium = find_equilibrium_radius(r, NucleationEnergyBarrier)
        if r_equilibrium is not None:
            fig.add_trace(go.Scatter(x=[r_equilibrium], y=[0], mode='markers', marker=dict(color='lightgreen', size=8),
                                     name='Equilibrium Radius'))
            fig.add_annotation(x=r_equilibrium, y=0, text='Equilibrium Radius', showarrow=True, arrowhead=1, ax=0,
                               ay=-10)

        # Plot critical radius
        r_critical = find_critical_radius(r, NucleationEnergyBarrier)
        fig.add_trace(
            go.Scatter(x=[r_critical], y=[NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)]], mode='markers',
                       marker=dict(color='green', size=8),
                       name='Critical Radius'))
        fig.add_annotation(x=r_critical, y=NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)],
                           text='Critical Radius', showarrow=True,
                           arrowhead=1, ax=-0, ay=-10)

        # Add a static curve based on Curve 3 with constant values
        static_curve_gamma_SL = 0.35
        static_curve_delta_G_v = 0.11
        static_curve = -4 / 3 * np.pi * r ** 3 * static_curve_delta_G_v + 4 * np.pi * r ** 2 * static_curve_gamma_SL
        fig.add_trace(go.Scatter(x=r, y=static_curve, mode='lines', line=dict(color='gray'), name='Pure water'))

        # Display the plot
        st.plotly_chart(fig, use_container_width=True)

    with st.expander("But nucleation is Heterogenous"):
        st.latex(r'\Delta G_n^{het} = \Bigg[-\frac{4}{3}\pi r^3 \Delta G_v + 4\pi r^2 \gamma_{SL}\Bigg] \Bigg[\frac{2- 3\cos(\theta) + \cos^{3}(\theta)}{4}\Bigg]')

        def calculate_curves(delta_G_v, gamma_SL, r, theta):
            InterfacialEnergy = 4 * np.pi * r ** 2 * gamma_SL
            VolumeFreeEnergy = -4 / 3 * np.pi * (r ** 3) * delta_G_v
            NucleationEnergyBarrier = -4 / 3 * np.pi * r ** 3 * delta_G_v + 4 * np.pi * r ** 2 * gamma_SL
            Heterogenous = NucleationEnergyBarrier * (2 - 3 * np.cos(np.radians(theta)) + np.cos(np.radians(theta)) ** 3) / 4
            return InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier, Heterogenous


        def calculate_critical_equilibrium_radius(r, curve):
            # Calculate the critical radius
            peak_index = np.argmax(curve)
            r_critical = r[peak_index]

            # Calculate the equilibrium radius
            zero_crossings = np.where(np.diff(np.sign(curve)))[0]
            valid_zero_crossings = zero_crossings[curve[zero_crossings] != 0]
            if len(valid_zero_crossings) > 0:
                r_equilibrium = r[valid_zero_crossings[0]]
            else:
                r_equilibrium = None

            return r_critical, r_equilibrium


        col1, col2, col3 = st.columns(3)

        with col1:
            # Create sliders for the variables
            gamma_SL = st.slider("$\gamma$", min_value=0.00, max_value=1.00, value=0.90,
                                 step=0.01, key='nucleation_eq_1_2')

        with col2:
            delta_G_v = st.slider("$\Delta G_v$", min_value=0.000, max_value=0.400,
                                  value=0.270, step=0.001, key='nucleation_eq_2_2')

        with col3:
            theta = st.slider("$\Theta$", min_value=0.0, max_value=90.0, value=90.0, step=1.0, key='nucleation_eq_3_1')

        # Generate random r values
        r = np.linspace(0, 100, 1000)

        # Calculate the curves
        InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier, Heterogenous = calculate_curves(delta_G_v, gamma_SL, r, theta)

        # Create a pandas DataFrame with r and curve values
        data = {"r": r, "Homogeneous": NucleationEnergyBarrier, "Heterogeneous": Heterogenous}
        df = pd.DataFrame(data)

        # Use Plotly Express to create an interactive line plot
        fig = px.line(df, x="r", y=["Homogeneous", "Heterogeneous"],
                      color_discrete_map={"Homogeneous": "green", "Heterogeneous": "purple"})
        # Update layout and axes ranges
        fig.update_layout(title="", xaxis_title="r", yaxis_title="ΔG",
                          yaxis_range=[-200, 200], xaxis_range=[0, 12])

        ### Calculate equilibrium radius and critical radius for Homogeneous curve
        r_critical, r_equilibrium = calculate_critical_equilibrium_radius(r, NucleationEnergyBarrier)

        ### Calculate equilibrium radius and critical radius for Heterogeneous curve
        r_critical_het, r_equilibrium_het = calculate_critical_equilibrium_radius(r, Heterogenous)

        # Add light green markers for the equilibrium radius in Curve 3
        if r_equilibrium:
            fig.add_trace(go.Scatter(x=[r_equilibrium], y=[0], mode='markers', marker=dict(color='lightgreen', size=8),
                                     name='Equilibrium Radius (Homogeneous)'))

        # Add light purple markers for the equilibrium radius in Heterogeneous curve
        if r_equilibrium_het:
            fig.add_trace(
                go.Scatter(x=[r_equilibrium_het], y=[0], mode='markers', marker=dict(color='pink', size=8),
                           name='Equilibrium Radius (Heterogeneous)'))

        # Add green marker for the critical radius in Curve 3
        fig.add_trace(
            go.Scatter(x=[r_critical], y=[NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)]], mode='markers',
                       marker=dict(color='green', size=8),
                       name='Critical Radius (Homogeneous)'))

        # Add purple marker for the critical radius in Heterogeneous curve
        fig.add_trace(
            go.Scatter(x=[r_critical_het], y=[Heterogenous[np.argmax(Heterogenous)]], mode='markers',
                       marker=dict(color='purple', size=8),
                       name='Critical Radius (Heterogeneous)'))

        # Add the Heterogeneous curve based on the equation
        fig.add_trace(go.Scatter(x=r, y=Heterogenous, mode='lines', line=dict(color='purple'), name='Heterogeneous'))

        # Add a static curve based on Curve 3 with constant values
        static_curve_gamma_SL = 0.35
        static_curve_delta_G_v = 0.11
        static_curve = -4 / 3 * np.pi * r ** 3 * static_curve_delta_G_v + 4 * np.pi * r ** 2 * static_curve_gamma_SL
        fig.add_trace(go.Scatter(x=r, y=static_curve, mode='lines', line=dict(color='gray'), name='Reference'))
        fig.update_layout(showlegend=True)

        # Display the plot
        st.plotly_chart(fig, use_container_width=True)

        #st.write('The $\$\Delta R$$ value for the homogenous curve is:')
        #st.write('The $\$\Delta R$$ value for the heterogenous curve is:')
        #st.write('The $\$\Delta R$$ ratio between both curve is:')

        #st.write('Conclusions on heterogenous nucleation:')
        #st.markdown('- It effectively reduces the energy barrier.')
        #st.markdown('- Only high contact angles preserve the anti-nucleation effect, which makes sense.')
        #st.markdown('- $r^*$ is the same, which agrees with barely unchanged average $T_n$ data')
        #st.markdown('- $r_{eq}$ is the same and $\$\Delta R$$ unchanged, which :red[does not agree] with observation. WAIT!')

    with st.expander("Zeldovich factor $Z$"):

        st.write(
            'The size interval $\$\Delta R$$ characterizes the energy profile around the critical size $r^*$. Two pieces of evidence and one inference point to a necessary reduction in $\$\Delta R$$:')
        st.markdown('- POM experiments showed crystal sizes 10x smaller.')
        st.markdown('- Isochoric experiments showed a narrowing of $\Delta T_n$.')
        st.markdown(
            '- Inferences from rheology data and gel-induced selective polymorphism point to a reduction in crystal size distribution.')
        st.write('')
        st.write(
            'Therefore, the $\$\Delta R$$ component appears highly connected to $\Delta T_n$, and should equally decrease to 1/3.')


        def calculate_curves(delta_G_v, gamma_SL, r):
            InterfacialEnergy = 4 * np.pi * r ** 2 * gamma_SL
            VolumeFreeEnergy = -4 / 3 * np.pi * r ** 3 * delta_G_v
            NucleationEnergyBarrier = -4 / 3 * np.pi * r ** 3 * delta_G_v + 4 * np.pi * r ** 2 * gamma_SL
            return InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier


        def find_equilibrium_radius(r, NucleationEnergyBarrier):
            zero_crossings = np.where(np.diff(np.sign(NucleationEnergyBarrier)))[0]
            valid_zero_crossings = zero_crossings[NucleationEnergyBarrier[zero_crossings] != 0]
            if len(valid_zero_crossings) > 0:
                r_equilibrium = r[valid_zero_crossings[0]]
                return r_equilibrium
            else:
                return None


        def find_critical_radius(r, NucleationEnergyBarrier):
            peak_index = np.argmax(NucleationEnergyBarrier)
            r_critical = r[peak_index]
            return r_critical, peak_index


        def calculate_delta_r(NucleationEnergyBarrier, k, T, kT_correction_factor):
            NucleationEnergyBarrier_y = NucleationEnergyBarrier.copy()
            y_value = NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)] - k * T * kT_correction_factor
            crossings = np.where(np.diff(np.sign(NucleationEnergyBarrier - y_value)))[0]
            deltaR_min = {"y value": y_value, "x1 value": r[crossings[0]]}
            deltaR_max = {"y value": y_value, "x2 value": r[crossings[1]]}
            deltaR = deltaR_max["x2 value"] - deltaR_min["x1 value"]
            return deltaR, deltaR_min, deltaR_max


        def calculate_kT_percentage(NucleationEnergyBarrier, k, T, kT_correction_factor):
            kT_value = k * T * kT_correction_factor
            max_energy_barrier = NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)]
            kT_percentage = (kT_value / max_energy_barrier) * 100
            return kT_percentage


        def calculate_Zeldovich(deltaR):
            Zeldovich = 2 / (np.pi ** (1 / 2) * deltaR)
            return Zeldovich


        k = 1.380649e-23  # Boltzmann constant
        T = 373.15  # Temperature in Kelvin
        kT_correction_factor = 1e21  # 1e21 is a temporary factor to relatively describe the graph

        col1, col2 = st.columns(2)

        with col1:
            # Create sliders for the variables
            gamma_SL = st.slider("$\gamma$", min_value=0.00, max_value=1.00, value=0.90,
                                 step=0.01, key='deltaR_1')

        with col2:
            delta_G_v = st.slider("$\Delta G_v$", min_value=0.000, max_value=0.400,
                                  value=0.270, step=0.001, key='deltaR_2')

        # Generate random r values
        r = np.linspace(0, 100, 1000)

        # Calculate the curves
        InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier = calculate_curves(delta_G_v, gamma_SL, r)

        # Create a pandas DataFrame with r and curve values
        data = {"r": r, "Interfacial energy": InterfacialEnergy, "Volumetric free energy": VolumeFreeEnergy,
                "Nucleation barrier": NucleationEnergyBarrier}
        df = pd.DataFrame(data)

        # Use Plotly Express to create an interactive line plot
        fig = px.line(df, x="r", y=["Interfacial energy", "Volumetric free energy", "Nucleation barrier"],
                      color_discrete_map={"Interfacial energy": "red", "Volumetric free energy": "blue",
                                          "Nucleation barrier": "green"})

        # Update layout and axes ranges
        fig.update_layout(title="", xaxis_title="r", yaxis_title="&#8710;G",
                          yaxis_range=[-200, 200], xaxis_range=[0, 12])

        # Plot equilibrium radius
        r_equilibrium = find_equilibrium_radius(r, NucleationEnergyBarrier)
        if r_equilibrium is not None:
            fig.add_trace(go.Scatter(x=[r_equilibrium], y=[0], mode='markers', marker=dict(color='lightgreen', size=8),
                                     name='Equilibrium Radius'))
            fig.add_annotation(x=r_equilibrium, y=0, text='Equilibrium Radius', showarrow=True, arrowhead=1, ax=0,
                               ay=-10)

        # Find the critical radius and its index
        r_critical, peak_index = find_critical_radius(r, NucleationEnergyBarrier)
        fig.add_trace(
            go.Scatter(x=[r_critical], y=[NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)]], mode='markers',
                       marker=dict(color='green', size=8),
                       name='Critical Radius'))
        fig.add_annotation(x=r_critical, y=NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)],
                           text='Critical Radius', showarrow=True,
                           arrowhead=1, ax=-0, ay=-10)

        # Calculate deltaR
        deltaR, deltaR_min, deltaR_max = calculate_delta_r(NucleationEnergyBarrier, k, T, kT_correction_factor)

        # Plot deltaR_min and deltaR_max as orange markers and a horizontal orange line
        fig.add_trace(go.Scatter(x=[deltaR_min["x1 value"], deltaR_max["x2 value"]],
                                 y=[deltaR_min["y value"], deltaR_max["y value"]],
                                 mode='markers', marker=dict(color='orange', size=8),
                                 name='$\Delta R$'))
        fig.add_shape(type="line",
                      x0=deltaR_min["x1 value"], y0=deltaR_min["y value"],
                      x1=deltaR_max["x2 value"], y1=deltaR_max["y value"],
                      line=dict(color='orange', width=2))

        # Static curve: Homogeneous Nucleation of pure water as reference
        static_curve_gamma_SL = 0.35
        static_curve_delta_G_v = 0.11
        static_curve = -4 / 3 * np.pi * r ** 3 * static_curve_delta_G_v + 4 * np.pi * r ** 2 * static_curve_gamma_SL
        fig.add_trace(go.Scatter(x=r, y=static_curve, mode='lines', line=dict(color='gray'), name='Pure water'))

        # Display the plot
        st.plotly_chart(fig, use_container_width=True)

        # Calculate percentage described by kT
        kT_percentage = calculate_kT_percentage(NucleationEnergyBarrier, k, T, kT_correction_factor)

        # Calculate Zeldovich factor
        Zeldovich = calculate_Zeldovich(deltaR)

        stat1, stat2, stat3 = st.columns(3)
        with stat1: st.metric("**Thermal fluctuations (%)**", round(kT_percentage, 2))
        with stat2: st.metric("$\$\Delta R$$", round(deltaR, 3))
        with stat3: st.metric("$Z$", round(Zeldovich, 2))

        st.write('In another perspective, the Zeldovich factor $Z$ controls the flatness of the energy profile. For two systems having the same free energy barriers, the system with the flatter free energy landscape near the barrier has **more diffusive nucleation dynamics** and a lower nucleation rate.')



    with st.expander("Effect of volumetric confinement: partition of $n$"):
        st.write(
            'The previous energy profiles have a relationship to the total number of atoms $n$ available in the system to migrate to the cluster.')
        st.markdown('- The volumetric free energy is proportional to $-n$.')
        st.markdown('- The interfacial energy is proportional to $n^{2/3}$.')

        import streamlit as st
        import numpy as np
        import pandas as pd
        import plotly.express as px
        import plotly.graph_objects as go


        def calculate_curves(delta_G_v, gamma_SL, r, n):
            InterfacialEnergy = 4 * np.pi * r ** 2 * gamma_SL * (n ** (2 / 3))
            VolumeFreeEnergy = -4 / 3 * np.pi * r ** 3 * delta_G_v * 1 / n
            NucleationEnergyBarrier = -4 / 3 * np.pi * r ** 3 * delta_G_v * 1 / n + 4 * np.pi * r ** 2 * gamma_SL * (
                        n ** (2 / 3))
            return InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier


        def find_equilibrium_radius(r, NucleationEnergyBarrier):
            zero_crossings = np.where(np.diff(np.sign(NucleationEnergyBarrier)))[0]
            valid_zero_crossings = zero_crossings[NucleationEnergyBarrier[zero_crossings] != 0]
            if len(valid_zero_crossings) > 0:
                r_equilibrium = r[valid_zero_crossings[0]]
                return r_equilibrium
            else:
                return None


        def find_critical_radius(r, NucleationEnergyBarrier):
            peak_index = np.argmax(NucleationEnergyBarrier)
            r_critical = r[peak_index]
            return r_critical, peak_index


        def calculate_delta_r(NucleationEnergyBarrier, k, T, kT_correction_factor):
            NucleationEnergyBarrier_y = NucleationEnergyBarrier.copy()
            y_value = NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)] - k * T * kT_correction_factor
            crossings = np.where(np.diff(np.sign(NucleationEnergyBarrier - y_value)))[0]
            deltaR_min = {"y value": y_value, "x1 value": r[crossings[0]]}
            deltaR_max = {"y value": y_value, "x2 value": r[crossings[1]]}
            deltaR = deltaR_max["x2 value"] - deltaR_min["x1 value"]
            return deltaR, deltaR_min, deltaR_max


        def calculate_kT_percentage(NucleationEnergyBarrier, k, T, kT_correction_factor):
            kT_value = k * T * kT_correction_factor
            max_energy_barrier = NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)]
            kT_percentage = (kT_value / max_energy_barrier) * 100
            return kT_percentage


        def calculate_Zeldovich(deltaR):
            Zeldovich = 2 / (np.pi ** (1 / 2) * deltaR)
            return Zeldovich


        k = 1.380649e-23  # Boltzmann constant
        T = 373.15  # Temperature in Kelvin
        kT_correction_factor = 1e21  # 1e21 is a temporary factor to relatively describe the graph

        col1, col2, col3 = st.columns(3)

        with col1:
            # Create sliders for the variables
            gamma_SL = st.slider("$\gamma$", min_value=0.00, max_value=1.00, value=0.90, step=0.01, key='meeting1')

        with col2:
            delta_G_v = st.slider("$\Delta G_v$", min_value=0.01, max_value=1.00, value=0.30, step=0.01,
                                  key='meeting2')

        with col3:
            # Create slider for the variable n
            n = st.slider("n", min_value=0.01, max_value=2.00, value=1.00, step=0.01, key='meeting3')

        # Generate random r values
        r = np.linspace(0, 100, 1000)

        # Calculate the curves
        InterfacialEnergy, VolumeFreeEnergy, NucleationEnergyBarrier = calculate_curves(delta_G_v, gamma_SL, r, n)

        # Create a pandas DataFrame with r and curve values
        data = {"r": r, "Interfacial energy": InterfacialEnergy, "Volumetric free energy": VolumeFreeEnergy,
                "Nucleation barrier": NucleationEnergyBarrier}
        df = pd.DataFrame(data)

        # Use Plotly Express to create an interactive line plot
        fig = px.line(df, x="r", y=["Interfacial energy", "Volumetric free energy", "Nucleation barrier"],
                      color_discrete_map={"Interfacial energy": "red", "Volumetric free energy": "blue",
                                          "Nucleation barrier": "green"})

        # Update layout and axes ranges
        fig.update_layout(title="", xaxis_title="r", yaxis_title="∆G", yaxis_range=[-200, 200], xaxis_range=[0, 12])

        # Plot equilibrium radius
        r_equilibrium = find_equilibrium_radius(r, NucleationEnergyBarrier)
        if r_equilibrium is not None:
            fig.add_trace(go.Scatter(x=[r_equilibrium], y=[0], mode='markers', marker=dict(color='lightgreen', size=8),
                                     name='Equilibrium Radius'))
            fig.add_annotation(x=r_equilibrium, y=0, text='Equilibrium Radius', showarrow=True, arrowhead=1, ax=0,
                               ay=-10)

        # Find the critical radius and its index
        r_critical, peak_index = find_critical_radius(r, NucleationEnergyBarrier)
        fig.add_trace(
            go.Scatter(x=[r_critical], y=[NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)]], mode='markers',
                       marker=dict(color='green', size=8), name='Critical Radius'))
        fig.add_annotation(x=r_critical, y=NucleationEnergyBarrier[np.argmax(NucleationEnergyBarrier)],
                           text='Critical Radius', showarrow=True, arrowhead=1, ax=-0, ay=-10)

        # Calculate deltaR
        deltaR, deltaR_min, deltaR_max = calculate_delta_r(NucleationEnergyBarrier, k, T, kT_correction_factor)

        # Plot deltaR_min and deltaR_max as orange markers and a horizontal orange line
        fig.add_trace(go.Scatter(x=[deltaR_min["x1 value"], deltaR_max["x2 value"]],
                                 y=[deltaR_min["y value"], deltaR_max["y value"]], mode='markers',
                                 marker=dict(color='orange', size=8), name='$\Delta R$'))
        fig.add_shape(type="line", x0=deltaR_min["x1 value"], y0=deltaR_min["y value"], x1=deltaR_max["x2 value"],
                      y1=deltaR_max["y value"], line=dict(color='orange', width=2))

        # Static curve: Homogeneous Nucleation of pure water as reference
        static_curve_gamma_SL = 0.35
        static_curve_delta_G_v = 0.11
        static_curve = -4 / 3 * np.pi * r ** 3 * static_curve_delta_G_v + 4 * np.pi * r ** 2 * static_curve_gamma_SL
        fig.add_trace(go.Scatter(x=r, y=static_curve, mode='lines', line=dict(color='gray'), name='Pure water'))

        # Calculate Zeldovich factor from deltaR
        Z = calculate_Zeldovich(deltaR)

        # Display the plot
        st.plotly_chart(fig, use_container_width=True)

        # Calculate percentage described by kT
        kT_percentage = calculate_kT_percentage(NucleationEnergyBarrier, k, T, kT_correction_factor)

        # Display metrics
        stat1, stat2, stat3 = st.columns(3)
        with stat1:
            st.metric("**Thermal fluctuations (%)**", round(kT_percentage, 2))
        with stat2:
            st.metric("∆r", round(deltaR, 3))
        with stat3:
            st.metric("Z", round(Z, 2))

    st.write('---')

    st.header('Kinetic Rationale')
    with st.expander("Zeldovich factor"):
       # st.write('- Decreasing $n$ reduces nucleation probability, hence nanoconfinement supressing nucleation. However the polymer promotes it, which :red[does not agree] with data.')
        #st.write('- Only when we consider gel pore formation reduces $\gamma$ so as to provide wettability: we promote nucleation.')

        st.subheader('Zeldovich factor')

        #st.latex(r'\$\Delta R$ = \frac {2}{\sqrt\pi}\frac{1}{Z}')
        #st.write('where $Z$ is the Zeldovich factor:')
        #st.latex(r'Z = \frac {3(\Delta G_n)^2}{4\sqrt{\pi kT}(A\gamma_{SL})^{3/2}}')

        #st.write('First, we model the nucleation events as a function of the heterogenous nucleation rate $J$:')
        #st.latex(r'J^{het} = f_0 \cdot N_s \cdot Z \cdot exp\Bigg(-\frac{\Delta G^*}{k_B T}\Bigg)')

        #st.write('where $f_0$ is the rate at which molecules attach to a nucleus, $N_s$ is the number of nucleation sites available, $Z$ is the Zeldovich factor and expresses the probability that a nucleus of size $r^*$ will form a new phase, rather than dissolve. Therefore, $Z$ is a corrective component towards the flatness of the energy profile: a narrowed curve due to higher Z implies steeper $\Delta G^*$ and reflects a pro-nucleating effect.')

        #st.write('From a kinetic perspective, Z is also:')
        #st.latex(r'Z = \Bigg(\frac{\eta}{2\pi k_B T}\Bigg)^{1/2}')
        #st.write('Given the increased viscosity of FucoPol, this would justify a higher Z and a steeper energy profile with drastically reduced $r_eq$ (proportional to $\Delta T_n$) and minimally reduced $r^*$ (proportional to $\overline T_n$).')


    with st.expander("Effect of viscosity $\eta$"):
        st.empty()

    st.write('---')