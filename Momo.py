import streamlit as st
import random
import time
import math
import hashlib
import json

# Configure the page
st.set_page_config(
    page_title="🎮 Kids Fun Games",
    page_icon="🎮",
    layout="wide"
)

# Custom CSS for kid-friendly styling (same as before)
st.markdown("""
<style>
    /* Global body styling */
    .stApp {
        background: linear-gradient(45deg, #FFB6C1, #87CEEB, #98FB98, #F0E68C, #DDA0DD, #FFE4B5);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
        min-height: 100vh;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        25% { background-position: 100% 50%; }
        50% { background-position: 100% 100%; }
        75% { background-position: 0% 100%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Floating elements animation */
    .floating-elements {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    .floating-star {
        position: absolute;
        font-size: 30px;
        animation: float 6s ease-in-out infinite;
        opacity: 0.7;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }
    
    /* Main header styling */
    .main-header {
        background: linear-gradient(135deg, #FF69B4, #FF1493, #FF6347, #FFD700, #ADFF2F, #00CED1, #FF69B4);
        background-size: 400% 400%;
        animation: rainbowPulse 4s ease-in-out infinite;
        padding: 3rem;
        border-radius: 30px;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border: 5px solid #FFF;
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: "⭐🌈⭐🎈⭐🌈⭐🎈⭐🌈⭐🎈⭐🌈⭐🎈⭐🌈⭐🎈⭐🌈⭐🎈";
        position: absolute;
        top: 10px;
        left: 0;
        right: 0;
        font-size: 20px;
        animation: sparkleMove 3s linear infinite;
        white-space: nowrap;
    }
    
    @keyframes rainbowPulse {
        0%, 100% { 
            background-position: 0% 50%;
            transform: scale(1);
        }
        25% { 
            background-position: 100% 50%;
            transform: scale(1.02);
        }
        50% { 
            background-position: 100% 100%;
            transform: scale(1);
        }
        75% { 
            background-position: 0% 100%;
            transform: scale(1.02);
        }
    }
    
    @keyframes sparkleMove {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    .main-header h1 {
        font-size: 3.5rem !important;
        color: white;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        margin: 1rem 0 !important;
        animation: bounce 2s ease-in-out infinite;
    }
    
    .main-header h3 {
        font-size: 1.8rem !important;
        color: #FFF;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-top: 1rem !important;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    /* Login screen styling */
    .login-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        border: 3px solid #FFF;
    }
    
    .login-header h1 {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 0.5rem !important;
    }
    
    .login-header h3 {
        color: #F8F8FF !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .login-form {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        border: 2px solid #E6E6FA;
        margin: 1rem 0;
    }
    
    /* Game cards styling */
    .game-card {
        background: linear-gradient(145deg, #FF69B4, #FF1493, #FFD700, #32CD32, #00CED1);
        background-size: 300% 300%;
        animation: cardPulse 5s ease-in-out infinite;
        padding: 2.5rem;
        border-radius: 25px;
        text-align: center;
        color: white;
        margin: 1.5rem 0;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        border: 4px solid #FFF;
        transform: scale(1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .game-card::before {
        content: "✨";
        position: absolute;
        top: 10px;
        right: 10px;
        font-size: 25px;
        animation: twinkle 2s ease-in-out infinite;
    }
    
    @keyframes cardPulse {
        0%, 100% { 
            background-position: 0% 50%;
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        }
        50% { 
            background-position: 100% 50%;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }
    }
    
    @keyframes twinkle {
        0%, 100% { opacity: 1; transform: scale(1) rotate(0deg); }
        50% { opacity: 0.5; transform: scale(1.2) rotate(180deg); }
    }
    
    .game-card:hover {
        transform: scale(1.05) rotate(1deg);
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
    }
    
    .game-card h2 {
        font-size: 2rem !important;
        margin-bottom: 1rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .game-card h3 {
        font-size: 2.5rem !important;
        margin: 1rem 0 !important;
        animation: wiggle 3s ease-in-out infinite;
    }
    
    @keyframes wiggle {
        0%, 100% { transform: rotate(0deg); }
        25% { transform: rotate(5deg); }
        75% { transform: rotate(-5deg); }
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #FF69B4, #FFD700, #32CD32, #00CED1) !important;
        background-size: 300% 300% !important;
        animation: buttonShine 3s ease-in-out infinite !important;
        color: white !important;
        border: 3px solid #FFF !important;
        border-radius: 25px !important;
        padding: 1rem 2.5rem !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3) !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2) !important;
    }
    
    @keyframes buttonShine {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .stButton > button:hover {
        transform: scale(1.1) !important;
        box-shadow: 0 12px 24px rgba(0,0,0,0.3) !important;
        border-color: #FFD700 !important;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        border: 3px solid #FF69B4 !important;
        border-radius: 15px !important;
        padding: 15px !important;
        font-size: 1.2rem !important;
        background: rgba(255,255,255,0.9) !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1) !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #FFD700 !important;
        box-shadow: 0 8px 20px rgba(255,215,0,0.3) !important;
    }
    
    /* Metrics styling */
    .metric-container div {
        background: linear-gradient(135deg, #FFB6C1, #87CEEB) !important;
        border-radius: 15px !important;
        padding: 10px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1) !important;
        border: 2px solid #FFF !important;
    }
    
    /* Paint canvas styling */
    .paint-canvas-container {
        background: white;
        padding: 25px;
        border-radius: 20px;
        border: 5px solid #FF69B4;
        text-align: center;
        overflow: auto;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        animation: canvasPulse 4s ease-in-out infinite;
    }
    
    @keyframes canvasPulse {
        0%, 100% { border-color: #FF69B4; }
        25% { border-color: #FFD700; }
        50% { border-color: #32CD32; }
        75% { border-color: #00CED1; }
    }
    
    /* Happy decorative elements */
    .happy-decoration {
        position: fixed;
        font-size: 40px;
        animation: happyFloat 8s ease-in-out infinite;
        pointer-events: none;
        z-index: 1000;
    }
    
    @keyframes happyFloat {
        0%, 100% { 
            transform: translateY(0px) rotate(0deg);
            opacity: 0.8;
        }
        25% { 
            transform: translateY(-30px) rotate(90deg);
            opacity: 1;
        }
        50% { 
            transform: translateY(-20px) rotate(180deg);
            opacity: 0.6;
        }
        75% { 
            transform: translateY(-35px) rotate(270deg);
            opacity: 1;
        }
    }
    
    /* Page title styling */
    h1, h2, h3 {
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1) !important;
    }
    
    /* Success/Info messages styling */
    .stSuccess, .stInfo {
        border-radius: 15px !important;
        border: 3px solid #32CD32 !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

# ======= AUTHENTICATION FUNCTIONS =======
def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def initialize_auth_system():
    """Initialize the authentication system"""
    if 'users_db' not in st.session_state:
        st.session_state.users_db = {}
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None
    if 'auth_mode' not in st.session_state:
        st.session_state.auth_mode = 'login'  # 'login' or 'register'

def register_user(username, password, parent_email, child_name):
    """Register a new user (parent)"""
    if username in st.session_state.users_db:
        return False, "Username already exists!"
    
    st.session_state.users_db[username] = {
        'password': hash_password(password),
        'parent_email': parent_email,
        'child_name': child_name,
        'created_date': time.time()
    }
    return True, "Registration successful!"

def login_user(username, password):
    """Login user"""
    if username not in st.session_state.users_db:
        return False, "Username not found!"
    
    if st.session_state.users_db[username]['password'] != hash_password(password):
        return False, "Incorrect password!"
    
    st.session_state.logged_in = True
    st.session_state.current_user = username
    st.session_state.player_name = st.session_state.users_db[username]['child_name']
    return True, "Login successful!"

def logout_user():
    """Logout current user"""
    st.session_state.logged_in = False
    st.session_state.current_user = None
    st.session_state.player_name = ''
    st.session_state.current_game = 'menu'

def show_login_screen():
    """Display the login/registration screen"""
    st.markdown("""
    <div class="login-header">
        <h1>🔐 Parent Access Portal</h1>
        <h3>Secure login to keep your child safe while playing!</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Toggle between login and registration
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔑 Login", key="switch_to_login", use_container_width=True):
            st.session_state.auth_mode = 'login'
            st.rerun()
    
    with col2:
        if st.button("📝 Register New Account", key="switch_to_register", use_container_width=True):
            st.session_state.auth_mode = 'register'
            st.rerun()
    
    st.markdown("---")
    
    if st.session_state.auth_mode == 'login':
        show_login_form()
    else:
        show_registration_form()

def show_login_form():
    """Display the login form"""
    st.markdown("""
    <div class="login-form">
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔑 Parent Login")
    st.markdown("Please enter your credentials to allow your child to access the games.")
    
    with st.form("login_form"):
        username = st.text_input("👤 Username", placeholder="Enter your username")
        password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
        
        submitted = st.form_submit_button("🚀 Login & Start Playing", use_container_width=True)
        
        if submitted:
            if username and password:
                success, message = login_user(username, password)
                if success:
                    st.success(f"✅ {message}")
                    st.balloons()
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(f"❌ {message}")
            else:
                st.warning("⚠️ Please fill in all fields!")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Demo account info
    st.info("💡 **Demo Account**: Username: `demo` | Password: `demo123` (Child: Alex)")

def show_registration_form():
    """Display the registration form"""
    st.markdown("""
    <div class="login-form">
    """, unsafe_allow_html=True)
    
    st.markdown("### 📝 Parent Registration")
    st.markdown("Create a secure account to manage your child's game access.")
    
    with st.form("registration_form"):
        username = st.text_input("👤 Choose Username", placeholder="Enter desired username")
        password = st.text_input("🔒 Choose Password", type="password", placeholder="Enter a secure password")
        confirm_password = st.text_input("🔒 Confirm Password", type="password", placeholder="Confirm your password")
        parent_email = st.text_input("📧 Parent Email", placeholder="your.email@example.com")
        child_name = st.text_input("👶 Child's Name", placeholder="Your child's first name")
        
        # Terms checkbox
        accept_terms = st.checkbox("✅ I agree to supervise my child's use of these games")
        
        submitted = st.form_submit_button("🎉 Create Account", use_container_width=True)
        
        if submitted:
            if username and password and confirm_password and parent_email and child_name and accept_terms:
                if password != confirm_password:
                    st.error("❌ Passwords don't match!")
                elif len(password) < 6:
                    st.error("❌ Password must be at least 6 characters long!")
                else:
                    success, message = register_user(username, password, parent_email, child_name)
                    if success:
                        st.success(f"✅ {message}")
                        st.info(f"🎮 Account created for {child_name}! You can now login to access the games.")
                        st.balloons()
                    else:
                        st.error(f"❌ {message}")
            else:
                st.warning("⚠️ Please fill in all fields and accept the terms!")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Initialize session state for both auth and games
def initialize_session_state():
    """Initialize all session state variables"""
    initialize_auth_system()
    
    # Add demo account for testing
    if 'demo' not in st.session_state.users_db:
        st.session_state.users_db['demo'] = {
            'password': hash_password('demo123'),
            'parent_email': 'demo@example.com',
            'child_name': 'Alex',
            'created_date': time.time()
        }
    
    # Game session state
    if 'current_game' not in st.session_state:
        st.session_state.current_game = 'menu'
    if 'player_name' not in st.session_state:
        st.session_state.player_name = ''

def show_main_menu():
    """Display the main menu with game selection"""
    # Header with logout option
    col1, col2 = st.columns([4, 1])
    with col1:
        current_child = st.session_state.users_db[st.session_state.current_user]['child_name']
        st.markdown(f"### 👋 Welcome back, **{st.session_state.current_user}** (Parent of {current_child})")
    with col2:
        if st.button("🚪 Logout", key="logout_button"):
            logout_user()
            st.rerun()
    
    st.markdown("""
    <div class="main-header">
        <h1>🎮 Welcome to Kids Fun Games! 🎮</h1>
        <h3>Choose your adventure and let's play!</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"### Hello {st.session_state.player_name}! 👋 Ready to have some fun?")
    
    # Game selection - 4 games
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="game-card">
            <h2>🧩 Memory Match</h2>
            <p>Find matching pairs of cute animals and objects!</p>
            <h3>🐶 🐱 🦋 🌟</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎯 Play Memory Match", key="memory", use_container_width=True):
            st.session_state.current_game = 'memory'
            initialize_memory_game()
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="game-card">
            <h2>🔢 Math Adventure</h2>
            <p>Solve fun math problems and become a math hero!</p>
            <h3>➕ ➖ ✖️ ➗</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Play Math Adventure", key="math", use_container_width=True):
            st.session_state.current_game = 'math'
            initialize_math_game()
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="game-card">
            <h2>🎨 Paint Studio</h2>
            <p>Create beautiful artwork with colors and shapes!</p>
            <h3>🖌️ 🎨 🌈 ✨</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎨 Open Paint Studio", key="paint", use_container_width=True):
            st.session_state.current_game = 'paint'
            initialize_paint_game()
            st.rerun()

    with col4:
        st.markdown("""
        <div class="game-card">
            <h2>📐 Shape Explorer</h2>
            <p>Learn about shapes and become a geometry hero!</p>
            <h3>🔴 🔷 🔺 ⭐</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔍 Explore Shapes", key="shapes", use_container_width=True):
            st.session_state.current_game = 'shapes'
            initialize_shape_game()
            st.rerun()

# ======= MEMORY GAME FUNCTIONS =======
def initialize_memory_game():
    """Initialize the memory matching game"""
    emojis = ["🐶", "🐱", "🐸", "🦋", "🌟", "🎈", "🍎", "🎯"]
    cards = emojis * 2
    random.shuffle(cards)
    
    st.session_state.memory_cards = cards
    st.session_state.memory_revealed = [False] * len(cards)
    st.session_state.memory_matched = [False] * len(cards)
    st.session_state.memory_first_card = None
    st.session_state.memory_second_card = None
    st.session_state.memory_moves = 0
    st.session_state.memory_pairs_found = 0
    st.session_state.memory_game_completed = False
    st.session_state.memory_start_time = time.time()

def show_memory_game():
    """Display the memory matching game"""
    st.markdown("# 🧩 Memory Match Game")
    st.markdown(f"### Welcome back, {st.session_state.player_name}! Find all the matching pairs!")
    
    # Back button
    if st.button("🏠 Back to Menu", key="back_memory"):
        st.session_state.current_game = 'menu'
        st.rerun()
    
    # Game stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🎯 Moves", st.session_state.memory_moves)
    with col2:
        st.metric("✅ Pairs Found", st.session_state.memory_pairs_found)
    with col3:
        pairs_remaining = len(st.session_state.memory_cards) // 2 - st.session_state.memory_pairs_found
        st.metric("📝 Pairs Left", pairs_remaining)
    with col4:
        if st.session_state.memory_game_completed:
            elapsed_time = int(time.time() - st.session_state.memory_start_time)
            st.metric("⏱️ Time", f"{elapsed_time}s")
        else:
            st.metric("⏱️ Time", "Playing...")
    
    # Game completion
    if st.session_state.memory_game_completed:
        st.balloons()
        st.success(f"🎉 Amazing job, {st.session_state.player_name}! You found all pairs!")
        elapsed_time = int(time.time() - st.session_state.memory_start_time)
        st.info(f"🏆 Completed in {st.session_state.memory_moves} moves and {elapsed_time} seconds!")
        
        if st.button("🎮 Play Again", key="memory_again"):
            initialize_memory_game()
            st.rerun()
    
    # Game grid
    rows, cols = 4, 4
    for row in range(rows):
        columns = st.columns(cols)
        for col in range(cols):
            index = row * cols + col
            with columns[col]:
                if st.session_state.memory_matched[index]:
                    st.markdown(f"""
                    <div style='background-color: #90EE90; border: 2px solid #32CD32; border-radius: 15px; 
                    text-align: center; padding: 20px; font-size: 40px; height: 100px; 
                    display: flex; align-items: center; justify-content: center;'>
                        {st.session_state.memory_cards[index]}
                    </div>""", unsafe_allow_html=True)
                elif st.session_state.memory_revealed[index]:
                    st.markdown(f"""
                    <div style='background-color: #FFE4B5; border: 2px solid #DEB887; border-radius: 15px; 
                    text-align: center; padding: 20px; font-size: 40px; height: 100px; 
                    display: flex; align-items: center; justify-content: center;'>
                        {st.session_state.memory_cards[index]}
                    </div>""", unsafe_allow_html=True)
                else:
                    if st.button("❓", key=f"card_{index}", use_container_width=True):
                        handle_memory_card_click(index)
                        st.rerun()

def handle_memory_card_click(index):
    """Handle memory game card clicks"""
    if st.session_state.memory_matched[index] or st.session_state.memory_revealed[index]:
        return
    
    if st.session_state.memory_first_card is None:
        st.session_state.memory_first_card = index
        st.session_state.memory_revealed[index] = True
    elif st.session_state.memory_second_card is None and index != st.session_state.memory_first_card:
        st.session_state.memory_second_card = index
        st.session_state.memory_revealed[index] = True
        check_memory_match()

def check_memory_match():
    """Check if memory cards match"""
    if st.session_state.memory_first_card is not None and st.session_state.memory_second_card is not None:
        idx1, idx2 = st.session_state.memory_first_card, st.session_state.memory_second_card
        
        if st.session_state.memory_cards[idx1] == st.session_state.memory_cards[idx2]:
            st.session_state.memory_matched[idx1] = True
            st.session_state.memory_matched[idx2] = True
            st.session_state.memory_pairs_found += 1
            
            if st.session_state.memory_pairs_found == len(st.session_state.memory_cards) // 2:
                st.session_state.memory_game_completed = True
        else:
            time.sleep(0.5)
            st.session_state.memory_revealed[idx1] = False
            st.session_state.memory_revealed[idx2] = False
        
        st.session_state.memory_first_card = None
        st.session_state.memory_second_card = None
        st.session_state.memory_moves += 1

# ======= MATH GAME FUNCTIONS =======
def initialize_math_game():
    """Initialize the math game"""
    st.session_state.math_score = 0
    st.session_state.math_questions_answered = 0
    st.session_state.math_level = 1
    st.session_state.math_streak = 0
