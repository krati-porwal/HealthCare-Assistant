import streamlit as st
from groq import Groq
import os


# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🧠 AI Healthcare Assistant")
st.write("Get structured healthcare information")

topic = st.text_input("Enter a medical topic (e.g., Diabetes)")

if st.button("Generate"):

    if topic:

        # Step 1: Define plan (Agent thinking)
        tasks = [
            "Explain the disease in simple terms",
            "List causes of the disease",
            "List symptoms",
            "Give precautions",
            "Suggest basic treatment"
        ]

        final_output = ""

        # Step 2: Execute each task
        for task in tasks:

            prompt = f"""
            Topic: {topic}

            Task: {task}

            Give clear and concise answer.
            """

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            result = response.choices[0].message.content

            # Step 3: Combine results
            final_output += f"### {task}\n{result}\n\n"

        # Step 4: Display
        sections = final_output.split("### ")
        for section in sections:
            if section.strip() != "":
                title, content = section.split("\n", 1)

                with st.expander(title):
                    st.write(content)

    else:
        st.warning("Please enter a topic")