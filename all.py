import streamlit as st
import smtplib
from email.message import EmailMessage

# App Title & Layout
st.set_page_config(page_title="SafeRoute System", layout="wide")

# Sidebar Navigation (Dropdown on Right)
st.sidebar.title("🍃CareVault SOS Hub")
page = st.sidebar.selectbox("Select an option", ["📄 Add Travel Details", "📍 Track Location", "🚨 Emergency SOS System"])

# Language Change Option in Sidebar (Simple Meta Refresh)
st.sidebar.markdown("### Change Language")
if st.sidebar.button("हिंदी"):
    st.markdown(
        "<meta http-equiv='refresh' content='0; url=https://all-hindi-sos-djtowaesuuca9upbcpxvxh.streamlit.app/' />", 
        unsafe_allow_html=True
    )

# ------------------------ Add Travel Details Page -----------------------
if page == "📄 Add Travel Details":
    st.title("🚖 SafeRoute Emergency Reporting System")

    # Hardcoded Receiver Emails (Editable)
    default_receivers = "siddhantpatil1543@gmail.com, siddhantpatil1540@gmail.com, maitreyeeb2004@gmail.com"
    receiver_emails = st.text_area("📥 Enter Receiver Emails (editable)", default_receivers)

    # Vehicle and driver details
    vehicle_number = st.text_input("🚗 Vehicle Number", placeholder="Enter vehicle number (e.g., MH12AB1234)")
    vehicle_type = st.selectbox("🚘 Vehicle Type", ["Car", "Bike", "Auto", "Other"])
    vehicle_color = st.text_input("🎨 Vehicle Color", placeholder="Enter vehicle color (e.g., White, Black, Red)")
    driver_name = st.text_input("🧑‍✈️ Driver's Name (Uber/Ola)", placeholder="Enter the driver's name")
    location = st.text_area("📍 Location Details", placeholder="Enter your current location or share a Google Maps link")
    message = st.text_area("📝 Additional Message (Optional)", placeholder="Describe your emergency situation")

    # File uploader for image attachments
    uploaded_file = st.file_uploader("📷 Upload an image of the vehicle/driver (optional)", type=["png", "jpg", "jpeg"])

    # Predefined sender credentials
    SENDER_EMAIL = "tensortitans2612@gmail.com"
    SENDER_PASSWORD = "hjcy lblh gwhv jmzk"

    # Send email button
    if st.button("🚀 Send Emergency Report"):
        if receiver_emails and vehicle_number and vehicle_color and driver_name and location:
            email_list = [email.strip() for email in receiver_emails.split(",")]

            # Construct email content
            email_body = f"""
            🚨 *Emergency Alert from SafeRoute System* 🚨
            
            📌 *Vehicle Details:*
            - Vehicle Number: {vehicle_number}
            - Vehicle Type: {vehicle_type}
            - Vehicle Color: {vehicle_color}
            
            👤 *Driver Details:*
            - Driver Name: {driver_name}
            
            📍 *Location:*
            {location}
            
            📝 *Additional Message:*
            {message if message else "No additional information provided."}
            """

            # Create the email
            msg = EmailMessage()
            msg["From"] = SENDER_EMAIL
            msg["To"] = ", ".join(email_list)
            msg["Subject"] = "🚨 SafeRoute Emergency Alert"
            msg.set_content(email_body)

            # Attach the uploaded image (if any)
            if uploaded_file is not None:
                file_data = uploaded_file.read()
                file_name = uploaded_file.name
                msg.add_attachment(file_data, maintype="image", subtype=file_name.split(".")[-1], filename=file_name)

            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)
                server.quit()
                
                st.success(f"✅ Emergency Report sent successfully to: {', '.join(email_list)}")
            except Exception as e:
                st.error(f"❌ Failed to send email: {e}")
        else:
            st.warning("⚠️ Please fill in all required fields before sending.")

# ------------------------ Track Location Page ------------------------
elif page == "📍 Track Location":
    st.title("📍 Track Location of a Loved One")

    user_email = st.text_input("📧 Your Email", placeholder="Enter your email")
    user_password = st.text_input("🔑 Your Email Password", type="password", placeholder="Enter your password")

    # Button to track location (Redirects to tracking page)
    if st.button("🚀 Track Location of Loved One"):
        st.markdown("[🔗 Click here to Track Location](https://1543siddhant.github.io/Map-Live-Tracking/)", unsafe_allow_html=True)

# ------------------------ Emergency SOS System ------------------------
elif page == "🚨 Emergency SOS System":
    st.title("🚨 Emergency SOS System")
    st.markdown("### ⚠️ **Immediate Assistance Required?** Send an emergency email with your location and details.")

    # Default receiver emails
    DEFAULT_RECEIVERS = [
        "siddhantpatil1543@gmail.com",
        "siddhantpatil1540@gmail.com"
    ]

    # Default email subject & message
    DEFAULT_SUBJECT = "🚨 URGENT: Emergency Assistance Needed!"
    DEFAULT_MESSAGE = "I am in an emergency and require urgent help! Please assist immediately."

    # Receiver emails input (Editable)
    receiver_emails = st.text_area("📥 Receiver Emails (comma-separated)", ", ".join(DEFAULT_RECEIVERS))

    # Subject (Not editable)
    st.text_input("📌 Subject", DEFAULT_SUBJECT, disabled=True)

    # Message (Editable)
    message = st.text_area("📝 Message", DEFAULT_MESSAGE)

    # File uploader for image attachment
    uploaded_file = st.file_uploader("📷 Upload an image (optional)", type=["png", "jpg", "jpeg"])

    # Emergency Call & Location Sharing
    st.markdown("📞 **Need to make an Emergency Call?**")
    st.markdown("[📲 Call Emergency Services (India)](tel:112)")

    st.markdown("📍 **Share Your Location Instantly:**")
    if st.button("📡 Share Live Location"):
        st.markdown("[🔗 Click here to Share Location](https://1543siddhant.github.io/Map-Live-Tracking/)", unsafe_allow_html=True)

    # Send email button
    if st.button("🚀 Send Emergency Email"):
        if receiver_emails and message:
            email_list = [email.strip() for email in receiver_emails.split(",")]
            
            # Create the email
            msg = EmailMessage()
            msg["From"] = SENDER_EMAIL
            msg["To"] = ", ".join(email_list)
            msg["Subject"] = DEFAULT_SUBJECT
            msg.set_content(message)

            # Attach the uploaded image (if any)
            if uploaded_file is not None:
                file_data = uploaded_file.read()
                file_name = uploaded_file.name
                msg.add_attachment(file_data, maintype="image", subtype=file_name.split(".")[-1], filename=file_name)

            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)
                server.quit()
                
                st.success(f"✅ Emergency Email sent successfully to: {', '.join(email_list)}")
            except Exception as e:
                st.error(f"❌ Failed to send email: {e}")
        else:
            st.warning("⚠️ Please ensure all fields are filled before sending.")
