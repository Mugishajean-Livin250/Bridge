import streamlit as st

# Page config
st.set_page_config(page_title="Bridge University Explorer", layout="centered", page_icon="C:/Users/Hp/OneDrive/Desktop/Edrawmax/python game design/Dissertation/education.png")

# Navigation
st.title("Bridge University Explorer")
nav = st.selectbox("Navigate", ["Home", "Search University", "Compare Universities", "Marks Calculator"], index=0)

# University Data
university_data = [
    {
        "name": "University of Rwanda",
        "image_url": "un1.jpg",
        "academic_info": "Wide range of programs from engineering to busines related courses, strong reputation in research ranked as the top public university in Rwanda.",
        "financial_info": "Affordable with government Income share Agreement(the govenment will pay all your tuition fees you will be paying a certain percentage depending on yourincome ) paying personally is not really Affordale.",
        "residential_info": "On-campus accommodation available.",
        "job_opportunities": "Strong links to government & private employers.",
        "location": "Kigali",
        "campus_map_url": "http://map.university_of_rwanda.com",
        "min_required_marks": 54
    },
    {
        "name": "African Leadership University (ALU)",
        "image_url": "un2.jpg",
        "academic_info": "Leadership-focused programs, entrepreneurial mindset, software engineering.",
        "financial_info": "Private tuition, scholarships for top achievers.",
        "residential_info": "Modern student housing available.",
        "job_opportunities": "Global career placement and internships.",
        "location": "Kigali",
        "campus_map_url": "http://map.alu.com",
        "min_required_marks": 45
    },
    {
        "name": "University of Global Health Equity (UGHE)",
        "image_url": "un3.jpg",
        "academic_info": "Specialized in public health and equity, basically health related courses a top tier and highly competitive school considered as Havard medical school of Rwanda.",
        "financial_info": "Scholarships and full sponsorships available which pays for everything from your education to helping you secure best internship.",
        "residential_info": "High-end student residence in Butaro.",
        "job_opportunities": "Partnerships with WHO, Doctors Without Borders.",
        "location": "Butaro",
        "campus_map_url": "http://map.ughe.com",
        "min_required_marks": 57
    },
    {
        "name": "Kigali Independent University (ULK)",
        "image_url": "un4.jpg",
        "academic_info": "Strong in business and law programs a higly proficient university in bussines related courses considering it's maarket of students who are passionate with what they are studying.",
        "financial_info": "Flexible fees and private scholarships.",
        "residential_info": "Hostel services and rentals nearby.",
        "job_opportunities": "Good connections with local businesses.",
        "location": "Kigali",
        "campus_map_url": "http://ulk.rw",
        "min_required_marks": 42
    },
    {
        "name": "Adventist University of Central Africa (AUCA)",
        "image_url": "un5.jpg",
        "academic_info": "Christian-based education with diverse programs.",
        "financial_info": "Moderate tuition fees with aid options payement is flexible as it there don't give out sholaships easily.",
        "residential_info": "Modern hostels within campus.",
        "job_opportunities": "Graduate placements in church institutions.",
        "location": "Masoro, Kigali",
        "campus_map_url": "http://auca.ac.rw",
        "min_required_marks": 55
    },
    {
        "name": "Institut d’Enseignement Supérieur de Ruhengeri (INES)",
        "image_url": "un6.jpg",
        "academic_info": "Known for applied sciences and engineering known as the hub of future architects and courses ranging form engineerin, nursing, computer sciences, busissness and Economy.",
        "financial_info": "Low tuition fees, Chancen international Income share Agreement to those who want to study and pay later basing on their income.",
        "residential_info": " Shcool hostels to all students and at good fair price meals included Affordable student accommodations.",
        "job_opportunities": "Links with local companies and projects.",
        "location": "Musanze",
        "campus_map_url": "http://ines.ac.rw",
        "min_required_marks": 55
    }
]

# ---------------- HOME ----------------
if nav == "Home":
    st.markdown("## Welcome to Bridge — Your Gateway to Universities in Rwanda 🇷🇼")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("pic2.jpg", caption="Explore Your Future", use_container_width=True)
    with col2:
        st.markdown("### Objectives")
        st.markdown("- Search for universities")
        st.markdown("- Compare academic/financial info")
        st.markdown("- Estimate your admission chance")
        st.markdown("- Discover campus & career details")

    st.image("pic1.jpg", caption="Your Journey Begins Here", use_container_width=True)

    st.markdown("### 💡 Why Bridge?")
    st.write("Personalized Guidance, discover programs tailored to your strengths and interests. Access to Top Universities. Explore verified institutions across the region. Real Student Reviews. Hear from students who’ve walked the path before you. Smart Comparison Tools Compare universities based on fees, programs, and more.  Career-Driven Insights. Get recommendations that align with your future goals.")

# ---------------- SEARCH UNIVERSITY ----------------
elif nav == "Search University":
    st.header("🔍 Search University Info")
    selected = st.selectbox("Choose a university", [u['name'] for u in university_data])

    if selected:
        uni = next(u for u in university_data if u["name"] == selected)
        st.image(uni["image_url"], use_container_width=True)
        st.subheader(uni["name"])

        st.markdown(f"**Academic Info:** {uni['academic_info']}")
        st.markdown(f"**Financial Info:** {uni['financial_info']}")
        st.markdown(f"** Campus Life:** {uni['residential_info']}")
        st.markdown(f"** Career Links:** {uni['job_opportunities']}")
        st.markdown(f"** Location:** {uni['location']}")
        st.markdown(f"[Campus Map]({uni['campus_map_url']})")

# ---------------- COMPARE UNIVERSITIES ----------------
elif nav == "Compare Universities":
    st.header("📊 Compare Up to 3 Universities Side by Side")

    names = [""] + [u["name"] for u in university_data]

    col1, col2, col3 = st.columns(3)
    with col1:
        u1 = st.selectbox("University 1", names, key="u1")
    with col2:
        u2 = st.selectbox("University 2", names, key="u2")
    with col3:
        u3 = st.selectbox("University 3", names, key="u3")

    selected = [name for name in [u1, u2, u3] if name != ""]

    if len(selected) >= 2:
        st.markdown("### Comparison Table")
        comparison_data = [next(u for u in university_data if u["name"] == name) for name in selected]

        for label in ["Academic Info", "Financial Info", "Campus Life", "Career Opportunities", "Location", "Minimum Marks"]:
            cols = st.columns(len(comparison_data))
            for idx, uni in enumerate(comparison_data):
                with cols[idx]:
                    if label == "Academic Info":
                        st.markdown(f"** {uni['academic_info']}**")
                    elif label == "Financial Info":
                        st.markdown(f" {uni['financial_info']}")
                    elif label == "Campus Life":
                        st.markdown(f"{uni['residential_info']}")
                    elif label == "Career Opportunities":
                        st.markdown(f"{uni['job_opportunities']}")
                    elif label == "Location":
                        st.markdown(f"{uni['location']}")
                    elif label == "Minimum Marks":
                        st.markdown(f" {uni['min_required_marks']}% required")

# ---------------- MARKS CALCULATOR ----------------
elif nav == "Marks Calculator":
    st.header("Admission Chance Estimator")

    user_marks = st.slider("Enter your average national exam score (%)", 0, 100, 60)

    eligible_unis = [u for u in university_data if user_marks >= u["min_required_marks"]]

    if eligible_unis:
        st.success(f"You are eligible for the following universities:")
        for uni in eligible_unis:
            st.markdown(f"- 🎓 **{uni['name']}** (Required: {uni['min_required_marks']}%)")
    else:
        st.error("Sorry, no universities match your current marks. Try again or explore scholarship programs.")

