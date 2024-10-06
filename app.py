import streamlit as st
import string

def check_password_strength(password):
    lower_alpha_count = upper_alpha_count = number_count = whitespace_count = special_char_count = 0
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_alpha_count += 1
        elif char in string.ascii_uppercase:
            upper_alpha_count += 1
        elif char in string.digits:
            number_count += 1
        elif char == ' ':
            whitespace_count += 1
        else:
            special_char_count += 1
    
    strength = 0
    remarks = ''
    
    # Calculate strength
    if lower_alpha_count >= 1:
        strength += 1
    if upper_alpha_count >= 1:
        strength += 1
    if number_count >= 1:
        strength += 1
    if whitespace_count >= 1:
        strength += 1
    if special_char_count >= 1:
        strength += 1

    # Set remarks based on strength
    if strength == 1:
        remarks = "That's a very weak password. Try to change it as soon as possible."
    elif strength == 2:
        remarks = "That's not a great password. You should consider making a stronger password."
    elif strength == 3:
        remarks = "Your password is okay, but it could be improved a lot."
    elif strength == 4:
        remarks = "Your password is hard to guess. But you can make it even more secure."
    elif strength == 5:
        remarks = "Now that's a very strong password! Hackers do not have a chance of guessing that password."

    return {
        "lowercase": lower_alpha_count,
        "uppercase": upper_alpha_count,
        "digits": number_count,
        "whitespaces": whitespace_count,
        "special_chars": special_char_count,
        "strength": strength,
        "remarks": remarks
    }

# Streamlit App

st.title("Password Strength Checker")

# Input
password = st.text_input("Enter your password", type="password")

if st.button("Check Strength"):
    if password:
        # Call the check_password_strength function
        result = check_password_strength(password)

        # Display the results
        st.write("Your password has:")
        st.write(f"- {result['lowercase']} lowercase letters")
        st.write(f"- {result['uppercase']} uppercase letters")
        st.write(f"- {result['digits']} digits")
        st.write(f"- {result['whitespaces']} whitespaces")
        st.write(f"- {result['special_chars']} special characters")
        st.write(f"**Password score:** {result['strength']}/5")
        st.write(f"**Remarks:** {result['remarks']}")
    else:
        st.warning("Please enter a password.")


st.markdown("---")
st.markdown(
    """
    <p style="text-align: center;">Developed by <strong>Aviral Bansal</strong></p>
    <p style="text-align: center;">
        <a href="https://github.com/Aviral1611" target="_blank">
            <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png"/>
        </a>
    </p>
    """, unsafe_allow_html=True
)