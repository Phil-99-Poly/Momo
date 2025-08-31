import streamlit as st
import random
import time
import math

# Configure the page
st.set_page_config(
    page_title="🎮 Kids Fun Games",
    page_icon="🎮",
    layout="wide"
)

# Custom CSS for kid-friendly styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        animation: rainbow 3s ease-in-out infinite alternate;
    }
    
    .game-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .paint-pixel {
        width: 25px;
        height: 25px;
        border: 1px solid #ccc;
        display: inline-block;
        margin: 1px;
        cursor: pointer;
        border-radius: 3px;
    }
    
    .paint-canvas-container {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border: 3px solid #FF6B6B;
        text-align: center;
        overflow: auto;
    }
    
    @keyframes rainbow {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-size: 18px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .color-palette {
        display: flex;
        gap: 10px;
        justify-content: center;
        margin: 20px 0;
        flex-wrap: wrap;
    }
    
    .color-btn {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        border: 3px solid white;
        cursor: pointer;
        transition: transform 0.2s;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
    }
    
    .color-btn:hover {
        transform: scale(1.1);
    }
    
    .color-btn.selected {
        border: 4px solid #333;
        transform: scale(1.2);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_game' not in st.session_state:
    st.session_state.current_game = 'menu'
if 'player_name' not in st.session_state:
    st.session_state.player_name = ''

def show_main_menu():
    """Display the main menu with game selection"""
    st.markdown("""
    <div class="main-header">
        <h1>🎮 Welcome to Kids Fun Games! 🎮</h1>
        <h3>Choose your adventure and let's play!</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Player name input
    if not st.session_state.player_name:
        st.session_state.player_name = st.text_input("🌟 What's your name, young adventurer?", placeholder="Enter your name here...")
    
    if st.session_state.player_name:
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
    generate_math_problem()

def generate_math_problem():
    """Generate a new math problem based on level"""
    level = st.session_state.math_level
    
    if level <= 2:  # Addition and subtraction
        a = random.randint(1, 10 * level)
        b = random.randint(1, 10 * level)
        operation = random.choice(['+', '-'])
        
        if operation == '+':
            st.session_state.math_question = f"{a} + {b}"
            st.session_state.math_answer = a + b
        else:
            if a < b:  # Keep result positive
                a, b = b, a
            st.session_state.math_question = f"{a} - {b}"
            st.session_state.math_answer = a - b
    
    else:  # Multiplication and division
        a = random.randint(1, min(12, level + 5))
        b = random.randint(1, min(12, level + 5))
        operation = random.choice(['×', '÷'])
        
        if operation == '×':
            st.session_state.math_question = f"{a} × {b}"
            st.session_state.math_answer = a * b
        else:
            result = a * b  # Make sure division is exact
            st.session_state.math_question = f"{result} ÷ {a}"
            st.session_state.math_answer = b

def show_math_game():
    """Display the math adventure game"""
    st.markdown("# 🔢 Math Adventure")
    st.markdown(f"### Great job, {st.session_state.player_name}! Let's solve some math problems!")
    
    # Back button
    if st.button("🏠 Back to Menu", key="back_math"):
        st.session_state.current_game = 'menu'
        st.rerun()
    
    # Game stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("⭐ Score", st.session_state.math_score)
    with col2:
        st.metric("📚 Questions", st.session_state.math_questions_answered)
    with col3:
        st.metric("🚀 Level", st.session_state.math_level)
    with col4:
        st.metric("🔥 Streak", st.session_state.math_streak)
    
    # Current problem
    st.markdown("---")
    st.markdown(f"### 🧮 Solve this problem:")
    st.markdown(f"# {st.session_state.math_question} = ?")
    
    # Answer input
    user_answer = st.number_input("Your answer:", value=0, step=1, key="math_answer_input")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✅ Submit Answer", key="submit_math", use_container_width=True):
            check_math_answer(user_answer)
            st.rerun()
    
    with col2:
        if st.button("⏭️ Skip Question", key="skip_math", use_container_width=True):
            st.session_state.math_streak = 0
            generate_math_problem()
            st.rerun()
    
    with col3:
        if st.button("🎮 New Game", key="new_math", use_container_width=True):
            initialize_math_game()
            st.rerun()
    
    # Progress and encouragement
    if st.session_state.math_questions_answered > 0:
        accuracy = (st.session_state.math_score / st.session_state.math_questions_answered) * 100
        st.progress(accuracy / 100)
        st.markdown(f"**Accuracy: {accuracy:.1f}%**")
        
        if st.session_state.math_streak >= 5:
            st.markdown("🔥 **You're on fire! Amazing streak!**")
        elif st.session_state.math_streak >= 3:
            st.markdown("⭐ **Great job! Keep it up!**")

def check_math_answer(user_answer):
    """Check if the math answer is correct"""
    correct = user_answer == st.session_state.math_answer
    st.session_state.math_questions_answered += 1
    
    if correct:
        st.session_state.math_score += 1
        st.session_state.math_streak += 1
        st.success(f"🎉 Correct! {st.session_state.math_question} = {st.session_state.math_answer}")
        
        # Level up every 5 correct answers
        if st.session_state.math_score % 5 == 0:
            st.session_state.math_level += 1
            st.balloons()
            st.info(f"🚀 Level Up! Welcome to Level {st.session_state.math_level}!")
    else:
        st.session_state.math_streak = 0
        st.error(f"❌ Not quite! {st.session_state.math_question} = {st.session_state.math_answer}")
    
    time.sleep(1)
    generate_math_problem()

# ======= SHAPE GAME FUNCTIONS =======
def initialize_shape_game():
    """Initialize the shape recognition game"""
    # Define shapes with their SVG code, name, and fun facts
    shapes = {
        "circle": {
            "svg": '<svg width="200" height="200" viewBox="0 0 200 200"><circle cx="100" cy="100" r="80" fill="#FF6B6B" stroke="#333" stroke-width="3"/></svg>',
            "emoji": "🔴",
            "fun_fact": "A circle is perfectly round like a ball!"
        },
        "square": {
            "svg": '<svg width="200" height="200" viewBox="0 0 200 200"><rect x="40" y="40" width="120" height="120" fill="#4ECDC4" stroke="#333" stroke-width="3"/></svg>',
            "emoji": "🟩",
            "fun_fact": "A square has 4 equal sides and 4 corners!"
        },
        "triangle": {
            "svg": '<svg width="200" height="200" viewBox="0 0 200 200"><polygon points="100,30 30,170 170,170" fill="#45B7D1" stroke="#333" stroke-width="3"/></svg>',
            "emoji": "🔺",
            "fun_fact": "A triangle has 3 sides and 3 corners!"
        },
        "rectangle": {
            "svg": '<svg width="200" height="200" viewBox="0 0 200 200"><rect x="30" y="60" width="140" height="80" fill="#96CEB4" stroke="#333" stroke-width="3"/></svg>',
            "emoji": "🟨",
            "fun_fact": "A rectangle has 4 sides - 2 long and 2 short!"
        },
        "star": {
            "svg": '<svg width="200" height="200" viewBox="0 0 200 200"><polygon points="100,20 120,70 175,70 135,105 150,160 100,130 50,160 65,105 25,70 80,70" fill="#FFEAA7" stroke="#333" stroke-width="3"/></svg>',
            "emoji": "⭐",
            "fun_fact": "A star has 5 points and shines bright!"
        },
        "diamond": {
            "svg": '<svg width="200" height="200" viewBox="0 0 200 200"><polygon points="100,30 170,100 100,170 30,100" fill="#DDA0DD" stroke="#333" stroke-width="3"/></svg>',
            "emoji": "💎",
            "fun_fact": "A diamond is like a square turned sideways!"
        },
        "oval": {
            "svg": '<svg width="200" height="200" viewBox="0 0 200 200"><ellipse cx="100" cy="100" rx="90" ry="60" fill="#FFB6C1" stroke="#333" stroke-width="3"/></svg>',
            "emoji": "🥚",
            "fun_fact": "An oval is like a stretched circle, like an egg!"
        },
        "heart": {
            "svg": '<svg width="200" height="200" viewBox="0 0 200 200"><path d="M100,180 C100,180 20,120 20,80 C20,50 40,30 70,30 C85,30 100,40 100,40 C100,40 115,30 130,30 C160,30 180,50 180,80 C180,120 100,180 100,180 Z" fill="#FF69B4" stroke="#333" stroke-width="3"/></svg>',
            "emoji": "💖",
            "fun_fact": "A heart shape shows love and kindness!"
        }
    }
    
    st.session_state.shapes_data = shapes
    st.session_state.shapes_score = 0
    st.session_state.shapes_total_questions = 0
    st.session_state.shapes_streak = 0
    st.session_state.shapes_level = 1
    st.session_state.shapes_encouragement = ""
    generate_new_shape()

def generate_new_shape():
    """Generate a new shape for the quiz"""
    shapes_list = list(st.session_state.shapes_data.keys())
    st.session_state.current_shape = random.choice(shapes_list)
    st.session_state.user_shape_answer = ""

def show_shape_game():
    """Display the shape recognition game"""
    st.markdown("# 📐 Shape Explorer Game")
    st.markdown(f"### Hello {st.session_state.player_name}! Let's learn about shapes together! 🌟")
    
    # Back button
    if st.button("🏠 Back to Menu", key="back_shapes"):
        st.session_state.current_game = 'menu'
        st.rerun()
    
    # Game stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("⭐ Score", st.session_state.shapes_score)
    with col2:
        st.metric("📝 Questions", st.session_state.shapes_total_questions)
    with col3:
        accuracy = (st.session_state.shapes_score / max(1, st.session_state.shapes_total_questions)) * 100
        st.metric("🎯 Accuracy", f"{accuracy:.0f}%")
    with col4:
        st.metric("🔥 Streak", st.session_state.shapes_streak)
    
    # Encouragement message
    if st.session_state.shapes_encouragement:
        st.success(st.session_state.shapes_encouragement)
    
    st.markdown("---")
    
    # Current shape display
    current_shape_data = st.session_state.shapes_data[st.session_state.current_shape]
    
    st.markdown("### 🔍 What shape is this?")
    
    # Display the shape in a centered container
    st.markdown(f"""
    <div style="text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
    padding: 30px; border-radius: 20px; margin: 20px 0;">
        <div style="background: white; border-radius: 15px; padding: 20px; display: inline-block; 
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);">
            {current_shape_data['svg']}
        </div>
        <div style="color: white; font-size: 24px; margin-top: 15px; font-weight: bold;">
            Can you name this shape? {current_shape_data['emoji']}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Answer options (multiple choice for kindergarteners)
    st.markdown("### 🤔 Choose the correct answer:")
    
    # Create multiple choice options
    shape_names = list(st.session_state.shapes_data.keys())
    correct_answer = st.session_state.current_shape
    
    # Generate 3 wrong answers
    wrong_answers = [name for name in shape_names if name != correct_answer]
    selected_wrong = random.sample(wrong_answers, min(3, len(wrong_answers)))
    
    # Combine and shuffle options
    all_options = [correct_answer] + selected_wrong
    random.shuffle(all_options)
    
    # Create answer buttons in a 2x2 grid
    cols = st.columns(2)
    for i, option in enumerate(all_options):
        with cols[i % 2]:
            option_emoji = st.session_state.shapes_data[option]['emoji']
            button_label = f"{option_emoji} {option.title()}"
            
            if st.button(button_label, key=f"shape_option_{i}", use_container_width=True):
                check_shape_answer(option)
                st.rerun()
    
    # Fun fact about current shape
    st.markdown("---")
    st.info(f"💡 **Fun Fact:** {current_shape_data['fun_fact']}")
    
    # Skip button for if kids get stuck
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("⏭️ Show Me a New Shape", key="skip_shape", use_container_width=True):
            generate_new_shape()
            st.session_state.shapes_encouragement = "That's okay! Let's try a different shape! 🌈"
            st.rerun()
    
    # Progress and achievements
    if st.session_state.shapes_total_questions > 0:
        st.markdown("---")
        st.markdown("### 🏆 Your Progress")
        
        progress_value = min(100, (st.session_state.shapes_score / max(1, st.session_state.shapes_total_questions)) * 100)
        st.progress(progress_value / 100)
        
        # Achievement badges
        achievements = []
        if st.session_state.shapes_score >= 1:
            achievements.append("🌟 First Shape!")
        if st.session_state.shapes_score >= 5:
            achievements.append("🎯 Shape Detective!")
        if st.session_state.shapes_score >= 10:
            achievements.append("👑 Shape Master!")
        if st.session_state.shapes_streak >= 3:
            achievements.append("🔥 On Fire!")
        if accuracy >= 80:
            achievements.append("🎖️ Super Accurate!")
        
        if achievements:
            st.markdown("**🏅 Achievements Unlocked:** " + " ".join(achievements))

def check_shape_answer(selected_answer):
    """Check if the shape answer is correct"""
    correct_answer = st.session_state.current_shape
    st.session_state.shapes_total_questions += 1
    
    if selected_answer == correct_answer:
        st.session_state.shapes_score += 1
        st.session_state.shapes_streak += 1
        
        # Encouraging messages based on streak
        if st.session_state.shapes_streak >= 5:
            st.session_state.shapes_encouragement = f"🎉 AMAZING! You got {selected_answer} right! You're on a {st.session_state.shapes_streak} shape streak! ⭐⭐⭐"
        elif st.session_state.shapes_streak >= 3:
            st.session_state.shapes_encouragement = f"🌟 Fantastic! {selected_answer.title()} is correct! You're doing great! 🎯"
        else:
            encouraging_phrases = [
                f"🎉 Yes! That's a {selected_answer}! Great job!",
                f"⭐ Perfect! You found the {selected_answer}!",
                f"🌈 Wonderful! {selected_answer.title()} is right!",
                f"🎊 Super! You know your {selected_answer}s!"
            ]
            st.session_state.shapes_encouragement = random.choice(encouraging_phrases)
        
        # Show balloons for milestones
        if st.session_state.shapes_score % 5 == 0:
            st.balloons()
    else:
        st.session_state.shapes_streak = 0
        current_shape_emoji = st.session_state.shapes_data[correct_answer]['emoji']
        st.session_state.shapes_encouragement = f"That's okay! This shape is a {correct_answer} {current_shape_emoji}. Let's try another one! 🌟"
    
    # Generate new shape for next question
    generate_new_shape()

# ======= PAINT GAME FUNCTIONS =======
def initialize_paint_game():
    """Initialize the paint game"""
    # Create a smaller, more manageable canvas (12x12)
    st.session_state.paint_canvas = {}
    st.session_state.paint_selected_color = "#FF0000"  # Default red
    st.session_state.paint_canvas_size = 12
    st.session_state.paint_drawing_mode = True
    
    # Initialize with white canvas
    for i in range(st.session_state.paint_canvas_size):
        for j in range(st.session_state.paint_canvas_size):
            st.session_state.paint_canvas[f"{i}_{j}"] = "#FFFFFF"

def show_paint_game():
    """Display the paint studio game"""
    st.markdown("# 🎨 Paint Studio")
    st.markdown(f"### Let your creativity shine, {st.session_state.player_name}!")
    
    # Back button
    if st.button("🏠 Back to Menu", key="back_paint"):
        st.session_state.current_game = 'menu'
        st.rerun()
    
    # Color palette
    st.markdown("### 🌈 Choose Your Color")
    colors = [
        ("❤️ Red", "#FF0000"),
        ("💙 Blue", "#0000FF"),
        ("💚 Green", "#00FF00"),
        ("💛 Yellow", "#FFFF00"),
        ("🧡 Orange", "#FFA500"),
        ("💜 Purple", "#800080"),
        ("🤎 Brown", "#8B4513"),
        ("🖤 Black", "#000000"),
        ("🤍 White", "#FFFFFF"),
        ("🩷 Pink", "#FFC0CB")
    ]
    
    # Create color selection in rows
    for i in range(0, len(colors), 5):
        cols = st.columns(5)
        for j, (color_name, color_code) in enumerate(colors[i:i+5]):
            with cols[j]:
                if st.button(color_name, key=f"color_{color_code}", use_container_width=True):
                    st.session_state.paint_selected_color = color_code
                    st.rerun()
    
    # Show current color
    st.markdown(f"**Current Color:** {st.session_state.paint_selected_color}")
    st.markdown(f'<div style="width: 50px; height: 50px; background-color: {st.session_state.paint_selected_color}; border: 2px solid black; border-radius: 5px; display: inline-block;"></div>', 
                unsafe_allow_html=True)
    
    # Tool buttons
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🗑️ Clear Canvas", key="clear_canvas", use_container_width=True):
            for i in range(st.session_state.paint_canvas_size):
                for j in range(st.session_state.paint_canvas_size):
                    st.session_state.paint_canvas[f"{i}_{j}"] = "#FFFFFF"
            st.rerun()
    
    with col2:
        if st.button("🌈 Rainbow Fill", key="rainbow_fill", use_container_width=True):
            rainbow_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"]
            for i in range(st.session_state.paint_canvas_size):
                for j in range(st.session_state.paint_canvas_size):
                    st.session_state.paint_canvas[f"{i}_{j}"] = random.choice(rainbow_colors)
            st.rerun()
    
    with col3:
        if st.button("🎯 Fill All", key="fill_all", use_container_width=True):
            for i in range(st.session_state.paint_canvas_size):
                for j in range(st.session_state.paint_canvas_size):
                    st.session_state.paint_canvas[f"{i}_{j}"] = st.session_state.paint_selected_color
            st.rerun()
    
    with col4:
        if st.button("✨ Sparkle", key="sparkle", use_container_width=True):
            # Add random sparkles
            for _ in range(20):
                i = random.randint(0, st.session_state.paint_canvas_size - 1)
                j = random.randint(0, st.session_state.paint_canvas_size - 1)
                sparkle_colors = ["#FFD700", "#FFFF00", "#FFF8DC", "#F0E68C"]
                st.session_state.paint_canvas[f"{i}_{j}"] = random.choice(sparkle_colors)
            st.rerun()
    
    # Canvas display and interaction
    st.markdown("### ✨ Your Canvas")
    st.markdown("Click on any square below to paint it with your selected color!")
    
    # Create the painting canvas
    canvas_html = '<div class="paint-canvas-container"><table style="border-collapse: collapse; margin: auto;">'
    
    for i in range(st.session_state.paint_canvas_size):
        canvas_html += '<tr>'
        for j in range(st.session_state.paint_canvas_size):
            color = st.session_state.paint_canvas.get(f"{i}_{j}", "#FFFFFF")
            canvas_html += f'<td style="width: 30px; height: 30px; background-color: {color}; border: 1px solid #ccc; cursor: pointer;" onclick=""></td>'
        canvas_html += '</tr>'
    
    canvas_html += '</table></div>'
    st.markdown(canvas_html, unsafe_allow_html=True)
    
    # Interactive painting using buttons (simplified approach)
    st.markdown("**Click the buttons below to paint:**")
    
    # Create painting interface with smaller grid for better performance
    for i in range(st.session_state.paint_canvas_size):
        cols = st.columns(st.session_state.paint_canvas_size)
        for j in range(st.session_state.paint_canvas_size):
            with cols[j]:
                current_color = st.session_state.paint_canvas.get(f"{i}_{j}", "#FFFFFF")
                # Show colored button
                button_style = f"background-color: {current_color}; width: 25px; height: 25px; border: 1px solid #333;"
                if st.button("⬜", key=f"pixel_{i}_{j}", help=f"Paint ({i},{j})"):
                    st.session_state.paint_canvas[f"{i}_{j}"] = st.session_state.paint_selected_color
                    st.rerun()
    
    # Art gallery
    st.markdown("---")
    st.markdown("### 🏛️ Art Gallery")
    
    with st.expander("💾 Save Your Masterpiece"):
        art_name = st.text_input("Name your artwork:", placeholder="My Beautiful Creation", key="art_name_input")
        if st.button("🎨 Save to Gallery", key="save_art") and art_name:
            if 'art_gallery' not in st.session_state:
                st.session_state.art_gallery = []
            
            st.session_state.art_gallery.append({
                'name': art_name,
                'artist': st.session_state.player_name,
                'canvas': st.session_state.paint_canvas.copy(),
                'timestamp': time.time()
            })
            st.success(f"🎉 '{art_name}' has been saved to your gallery!")
    
    # Display gallery
    if 'art_gallery' in st.session_state and st.session_state.art_gallery:
        with st.expander(f"🖼️ {st.session_state.player_name}'s Art Collection ({len(st.session_state.art_gallery)} artworks)"):
            for idx, artwork in enumerate(st.session_state.art_gallery):
                st.markdown(f"**🎨 {artwork['name']}** by {artwork['artist']}")
                
                # Display a mini version of the artwork
                mini_canvas = '<div style="margin: 10px 0;"><table style="border-collapse: collapse;">'
                for i in range(st.session_state.paint_canvas_size):
                    mini_canvas += '<tr>'
                    for j in range(st.session_state.paint_canvas_size):
                        color = artwork['canvas'].get(f"{i}_{j}", "#FFFFFF")
                        mini_canvas += f'<td style="width: 15px; height: 15px; background-color: {color}; border: 1px solid #ddd;"></td>'
                    mini_canvas += '</tr>'
                mini_canvas += '</table></div>'
                st.markdown(mini_canvas, unsafe_allow_html=True)
                
                # Option to load artwork back to canvas
                if st.button(f"📥 Load '{artwork['name']}'", key=f"load_art_{idx}"):
                    st.session_state.paint_canvas = artwork['canvas'].copy()
                    st.success(f"Loaded '{artwork['name']}' to canvas!")
                    st.rerun()
                
                st.markdown("---")

# ======= MAIN APPLICATION =======
def main():
    """Main application logic"""
    if st.session_state.current_game == 'menu':
        show_main_menu()
    elif st.session_state.current_game == 'memory':
        show_memory_game()
    elif st.session_state.current_game == 'math':
        show_math_game()
    elif st.session_state.current_game == 'shapes':
        show_shape_game()
    elif st.session_state.current_game == 'paint':
        show_paint_game()

if __name__ == "__main__":
    main()

