import streamlit as st
from streamlit_option_menu import option_menu
from app_utils import switch_page
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import json

def load_lottiefile(filepath: str):

    '''Load lottie animation file'''

    with open(filepath, "r") as f:
        return json.load(f)

st_lottie(load_lottiefile("images/hello.json"), speed=1, reverse=False, loop=True, quality="high", height=300)

# im = Image.open("icon.png")
# st.set_page_config(page_title = "AI Interviewer", layout = "centered",page_icon=im)

lan = st.selectbox("#### Language", ["English","French (Soon...)","More Language..."])

if lan == "English":
    home_title = "AI Interviewer"
    home_introduction = "Welcome to AI Interviewer, empowering your interview preparation with generative AI."
    with st.sidebar:
        st.markdown('AI Interviewer')
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )
    # st.image("https://media.giphy.com/media/71iKnqJZmQjPpwfTt8/giphy.gif", width=400)
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5></font></span>""",unsafe_allow_html=True)
    st.markdown("""\n""")
    #st.markdown("#### Greetings")
    st.markdown("Welcome to AI Interviewer! 👏 AI Interviewer is your personal interviewer powered by generative AI that conducts mock interviews."
                "You can upload your resume and enter job descriptions, and AI Interviewer will ask you customized questions. Additionally, you can configure your own Interviewer!")
    st.markdown("""\n""")
    st.markdown("""\n""")
    st.markdown("#### Get started!")
    st.markdown("Select one of the following screens to start your interview!")
    selected = option_menu(
            menu_title= None,
            options=["Professional", "Resume", "Behavioral"],
            icons = ["cast", "cloud-upload", "cast"],
            default_index=0,
            orientation="horizontal",
        )
    if selected == 'Professional':
        st.info("""
            📚In this session, the AI Interviewer will assess your technical skills as they relate to the job description.
            Note: The maximum length of your answer is 4097 tokens!
            - Each Interview will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Choose your favorite interaction style (chat/voice)
            - Start introduce yourself and enjoy！ """)
        if st.button("Start Interview!"):
            switch_page("Professional Screen")
    if selected == 'Resume':
        st.info("""
        📚In this session, the AI Interviewer will review your resume and discuss your past experiences.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Choose your favorite interaction style (chat/voice)
        - Start introduce yourself and enjoy！ """
        )
        if st.button("Start Interview!"):
            switch_page("Resume Screen")
    if selected == 'Behavioral':
        st.info("""
        📚In this session, the AI Interviewer will assess your soft skills as they relate to the job description.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Choose your favorite interaction style (chat/voice)
        - Start introduce yourself and enjoy！ 
        """)
        if st.button("Start Interview!"):
            switch_page("Behavioral Screen")
    st.markdown("""\n""")

if lan == "French (Soon...)":
    home_title = "Entretien avec l'IA - Soon..."
    home_introduction = "Bienvenue sur AI Interviewer, renforçant votre préparation aux entretiens grâce à l'intelligence artificielle générative."
    with st.sidebar:
        st.markdown('Entretien avec L\' IA - Soon...')
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )
    st.image("https://media.giphy.com/media/71iKnqJZmQjPpwfTt8/giphy.gif", width=400)
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5></font></span>""",unsafe_allow_html=True)
    st.markdown("""\n""")
    #st.markdown("#### Greetings")
    st.markdown("Bienvenue sur AI Interviewer ! 👏 AI Interviewer est votre intervieweur personnel alimenté par l'intelligence artificielle générative qui réalise des entretiens simulés."
                "Vous pouvez télécharger votre CV et entrer des descriptions de poste, et AI Interviewer vous posera des questions personnalisées. De plus, vous pouvez configurer votre propre intervieweur !")
    st.markdown("""\n""")
    st.markdown("""\n""")
    st.markdown("#### Commencez !")
    st.markdown("Sélectionnez l'un des écrans suivants pour commencer votre entretien !")
    selected = option_menu(
            menu_title= None,
            options=["Professionnel", "CV", "Comportemental"],
            icons = ["cast", "cloud-upload", "cast"],
            default_index=0,
            orientation="horizontal",
        )
    if selected == 'Professionnel':
        st.info("""
            📚Dans cette session, l'AI Interviewer évaluera vos compétences techniques en lien avec la description du poste. 
            Note : La longueur maximale de votre réponse est de 4097 jetons !
            - Chaque entretien durera de 10 à 15 minutes.
            - Pour commencer une nouvelle session, rafraîchissez simplement la page.
            - Choisissez votre style d'interaction préféré (chat/voix).
            - Commencez par vous présenter et profitez de l'entretien ! """)
        if st.button("Commencez l'entretien !"):
            switch_page("Professional Screen")
    if selected == 'CV':
        st.info("""
        📚Au cours de cette session, l'AI Interviewer examinera votre curriculum vitae et discutera de vos expériences passées.
         Note : La longueur maximale de votre réponse est de 4097 jetons !
        - Chaque entretien durera de 10 à 15 minutes.
        - Pour commencer une nouvelle session, rafraîchissez simplement la page.
        - Choisissez votre style d'interaction préféré (chat/voix).
        - Commencez par vous présenter et profitez de l'entretien ! """)
        if st.button("Commencez l'entretien !"):
            switch_page("Resume Screen")
    if selected == 'Comportemental':
        st.info("""
        📚Au cours de cette session, l'AI Interviewer évaluera vos compétences relationnelles (soft skills) en relation avec la description du poste.
         Note : La longueur maximale de votre réponse est de 4097 jetons !
        - Chaque entretien durera de 10 à 15 minutes.
        - Pour commencer une nouvelle session, rafraîchissez simplement la page.
        - Choisissez votre style d'interaction préféré (chat/voix).
        - Commencez par vous présenter et profitez de l'entretien ! """)
        if st.button("Commencez l'entretien !"):
            switch_page("Behavioral Screen")
    st.markdown("""\n""")

if lan == "More Language...":
    home_title = "Coming Soon..."
    with st.sidebar:
        st.markdown('Coming Soon...')
        st.markdown('\n')
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5></font></span>""",unsafe_allow_html=True)
    giphy_link = "https://media.giphy.com/media/5PBZfvqqtIqSz1ZQKj/giphy.gif"
    st.image(giphy_link, width=600)