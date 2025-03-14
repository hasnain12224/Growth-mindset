import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", layout="wide")

st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio("Navigate", ["Home", "Tips", "Quiz"])

st.title("🌱 Growth Mindset Challenge")

if menu == "Home":
    st.markdown("""
    ### 🌟 Welcome to the **Growth Mindset Challenge**!
    🚀 Ready to grow? Click on **Tips** to learn more or take a **Quiz** to test your knowledge.
    """)
    if st.button("Click to Learn More"):
        st.markdown("""
        **What is a Growth Mindset?**
        - A belief that abilities can be developed through dedication and hard work.
        - A passion for learning and resilience.
        - The ability to embrace challenges and learn from failures.
        """)

elif menu == "Tips":
    st.subheader("📝 Growth Mindset Tips")
    tips = [
        "✅ Embrace challenges.",
        "✅ Learn from mistakes.",
        "✅ Stay persistent & keep trying.",
        "✅ Seek feedback and improve.",
        "✅ Celebrate efforts, not just results."
    ]
    for tip in tips:
        st.write(tip)

elif menu == "Quiz":
    st.subheader("🎯 Quick Growth Mindset Quiz")
    
    if 'score' not in st.session_state or st.button("Reset Score"):
        st.session_state.score = 0
    
    questions = [
        ("What is the key to growth mindset?", ["Fixed Intelligence", "Hard Work & Learning", "Avoiding Challenges"], "Hard Work & Learning"),
        ("Which one is important for growth mindset?", ["Giving Up", "Effort & process", "Perfection"], "Effort & process"),
        ("How should you see challenges?", ["Avoid them", "Face them & learn", "Ignore them"], "Face them & learn"),
        ("What should be your focus?", ["Only results", "Learning & effort", "Luck"], "Learning & effort"),
        ("What helps in improvement?", ["Criticism", "Feedback & practice", "Doing nothing"], "Feedback & practice")
    ]
    
    with st.form("quiz_form"):
        for i, (question, options, correct_answer) in enumerate(questions):
            st.write(f"**{question}**")
            st.radio("Select an answer:", options, key=f"q{i}")
        
        submitted = st.form_submit_button("Submit Answers")
        
        if submitted:
            st.session_state.score = sum(1 for i, (_, _, correct_answer) in enumerate(questions) 
                                         if st.session_state.get(f"q{i}") == correct_answer)
            st.write(f"## Your Total Score: {st.session_state.score}/5")















