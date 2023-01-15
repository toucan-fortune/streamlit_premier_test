import streamlit as st

# dans le requirements.txt
# ne pas installer time (ou autre module)
# qui est un module standard à Python

# local run
# streamlit run base.py

##################################################
# Configurer la page
# wide, centered
# auto or expanded
#menu_items={'Get Help': 'https://www.extremelycoolapp.com/help',
#            'Report a bug': "https://www.extremelycoolapp.com/bug",
#            'About': "# This is a header. This is an *extremely* cool app!"}
st.set_page_config(page_title="Tableau de bord",
                   page_icon="img/favicon-32x32b.png",
                   layout="centered",  # wide
                   initial_sidebar_state="auto")  # expanded

##################################################
st.title ("title: Tableau de base")

st.header("header: Markdown")

st.subheader("subheader: texte simple")

st.markdown("Markdown simple")

st.subheader("subheader: texte avec balises")

#import pkg_resources
#from subprocess import call

#packages = [dist.project_name for dist in pkg_resources.working_set]
#call("pip install --upgrade " + ' '.join(packages), #shell=True)

chaine = \
    """
    
    ## Lorem
    
    [Lorem Ipsum](https://lipsum.com/)
    
    *ipsum* **dolor** sit amet
    
    ### consectetur adipiscing elit
    
    - sed
    - do
    - eiusmod
    
    tempor incididunt ut labore et dolore magna aliqua.
    
    1. Ut
    1. enim
    1. ad
    
    ### minim
    
    > veniam, quis nostrud exercitation ullamco
    
    laboris nisi `x=2` ut aliquip ex ea commodo consequat.
    
    "Duis aute irure dolor in reprehenderit in voluptate velit esse 
    cillum dolore eu fugiat nulla pariatur."
     
    «Excepteur sint occaecat cupidatat non proident, 
    sunt in culpa qui officia deserunt mollit anim id est laborum.»
    
    """

st.markdown(chaine)

st.text('texte pur')

# LaTeX
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.markdown('---')
st.header("header: Texte et code; médias")

# Comme un print()
st.write("texte ou code à imprimer (résultat)")
st.write("""texte ou code à imprimer (résultat)""")
st.write(r"""texte ou code à imprimer (résultat)""")

# Code
st.code("x=2021")

st.markdown('---')
st.header("header: Médias")

st.image("img/dashboard.png")
st.caption("caption de l'image")

st.markdown('et audio, video...')

#st.audio("Audio.mp3")
#st.video("video.mp4")
