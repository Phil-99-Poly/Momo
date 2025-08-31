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
    
    .paint-canvas {
        border: 3px solid #FF6B6B;
        border-radius: 15px;
        background: white;
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
        
        # Game selection
        col1, col2, col3 = st.columns(3)
        
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

def initialize_paint_game():
    """Initialize the paint game"""
    st.session_state.paint_canvas = [[255, 255, 255] for _ in range(400)]  # 20x20 grid
    st.session_state.paint_color = [255, 0, 0]  # Default red
    st.session_state.paint_brush_size = 1

def show_paint_game():
    """Display the paint studio game"""
    st.markdown("# 🎨 Paint Studio")
    st.markdown(f"### Let your creativity shine, {st.session_state.player_name}!")
    
    # Back button
    if st.button("🏠 Back to Menu", key="back_paint"):
        st.session_state.current_game = 'menu'
        st.rerun()
    
    # Paint tools
    st.markdown("### 🖌️ Choose Your Tools")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        color_choice = st.selectbox("🎨 Color", 
            ["❤️ Red", "💙 Blue", "💚 Green", "💛 Yellow", "🧡 Orange", "💜 Purple", "🖤 Black", "🤍 White"])
        color_map = {
            "❤️ Red": [255, 0, 0], "💙 Blue": [0, 0, 255], "💚 Green": [0, 255, 0],
            "💛 Yellow": [255, 255, 0], "🧡 Orange": [255, 165, 0], "💜 Purple": [128, 0, 128],
            "🖤 Black": [0, 0, 0], "🤍 White": [255, 255, 255]
        }
        st.session_state.paint_color = color_map[color_choice]
    
    with col2:
        st.session_state.paint_brush_size = st.select_slider("🖌️ Brush Size", [1, 2, 3, 4, 5])
    
    with col3:
        if st.button("🗑️ Clear Canvas", use_container_width=True):
            st.session_state.paint_canvas = [[255, 255, 255] for _ in range(400)]
            st.rerun()
    
    with col4:
        if st.button("🌈 Random Colors", use_container_width=True):
            for i in range(400):
                st.session_state.paint_canvas[i] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            st.rerun()
    
    # Simple drawing interface (text-based for Streamlit)
    st.markdown("### ✨ Your Masterpiece")
    st.markdown("Click the buttons below to paint! Each button represents a pixel on your canvas.")
    
    # Create a simple grid for painting
    rows, cols = 20, 20
    for row in range(rows):
        columns = st.columns(cols)
        for col in range(cols):
            index = row * cols + col
            with columns[col]:
                # Create colored button
                r, g, b = st.session_state.paint_canvas[index]
                if st.button("⬜", key=f"paint_{index}", 
                           help=f"Paint pixel ({row}, {col})"):
                    # Apply brush size
                    for dr in range(-st.session_state.paint_brush_size + 1, st.session_state.paint_brush_size):
                        for dc in range(-st.session_state.paint_brush_size + 1, st.session_state.paint_brush_size):
                            new_row, new_col = row + dr, col + dc
                            if 0 <= new_row < rows and 0 <= new_col < cols:
                                new_index = new_row * cols + new_col
                                st.session_state.paint_canvas[new_index] = st.session_state.paint_color.copy()
                    st.rerun()
    
    # Art gallery
    st.markdown("---")
    with st.expander("🖼️ Save Your Art"):
        art_name = st.text_input("Name your masterpiece:", placeholder="My Beautiful Painting")
        if st.button("💾 Save to Gallery") and art_name:
            if 'art_gallery' not in st.session_state:
                st.session_state.art_gallery = []
            st.session_state.art_gallery.append({
                'name': art_name,
                'artist': st.session_state.player_name,
                'canvas': st.session_state.paint_canvas.copy()
            })
            st.success(f"🎨 '{art_name}' saved to your gallery!")
    
    # Show gallery if exists
    if 'art_gallery' in st.session_state and st.session_state.art_gallery:
        with st.expander(f"🏛️ {st.session_state.player_name}'s Art Gallery"):
            for i, artwork in enumerate(st.session_state.art_gallery):
                st.markdown(f"**{artwork['name']}** by {artwork['artist']}")

# Main app logic
def main():
    if st.session_state.current_game == 'menu':
        show_main_menu()
    elif st.session_state.current_game == 'memory':
        show_memory_game()
    elif st.session_state.current_game == 'math':
        show_math_game()
    elif st.session_state.current_game == 'paint':
        show_paint_game()

if __name__ == "__main__":
    main()



