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

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cd0469b9-2f6e-4ee3-806d-b4f04eb85123",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\phili\\anaconda3\\lib\\site-packages (1.45.1)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: blinker<2,>=1.5.0 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (1.9.0)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (5.5.1)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (8.1.8)\n",
      "Requirement already satisfied: numpy<3,>=1.23 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (2.1.3)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (24.2)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (2.2.3)\n",
      "Requirement already satisfied: pillow<12,>=7.1.0 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (11.1.0)\n",
      "Requirement already satisfied: protobuf<7,>=3.20 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (5.29.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (19.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (9.0.0)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.4.0 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (4.0.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from streamlit) (6.5.1)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.6)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: narwhals>=1.14.2 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (1.31.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\phili\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.3.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2025.8.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.3.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.22.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\phili\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "94b8eaef-ff68-4b35-957b-18c5cde0e41c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import random\n",
    "import time\n",
    "from typing import List, Tuple\n",
    "\n",
    "# Page configuration\n",
    "st.set_page_config(\n",
    "    page_title=\"Memory Matching Game\",\n",
    "    page_icon=\"🧠\",\n",
    "    layout=\"wide\"\n",
    ")\n",
    "\n",
    "def initialize_game(grid_size: int = 4) -> None:\n",
    "    \"\"\"Initialize the game state\"\"\"\n",
    "    # Create pairs of emojis\n",
    "    emojis = ['🐱', '🐶', '🐼', '🦊', '🐸', '🐯', '🦁', '🐵', \n",
    "              '🐷', '🐭', '🐹', '🐰', '🐻', '🐨', '🐺', '🦝']\n",
    "    \n",
    "    # Calculate number of pairs needed\n",
    "    total_cards = grid_size * grid_size\n",
    "    pairs_needed = total_cards // 2\n",
    "    \n",
    "    # Select random emojis and create pairs\n",
    "    selected_emojis = random.sample(emojis, pairs_needed)\n",
    "    card_values = selected_emojis * 2\n",
    "    random.shuffle(card_values)\n",
    "    \n",
    "    # Initialize session state\n",
    "    st.session_state.cards = card_values\n",
    "    st.session_state.revealed = [False] * total_cards\n",
    "    st.session_state.matched = [False] * total_cards\n",
    "    st.session_state.selected = []\n",
    "    st.session_state.moves = 0\n",
    "    st.session_state.matches = 0\n",
    "    st.session_state.game_complete = False\n",
    "    st.session_state.start_time = time.time()\n",
    "    st.session_state.grid_size = grid_size\n",
    "\n",
    "def handle_card_click(index: int) -> None:\n",
    "    \"\"\"Handle card click logic\"\"\"\n",
    "    if (st.session_state.matched[index] or \n",
    "        st.session_state.revealed[index] or \n",
    "        len(st.session_state.selected) >= 2):\n",
    "        return\n",
    "    \n",
    "    # Reveal the card\n",
    "    st.session_state.revealed[index] = True\n",
    "    st.session_state.selected.append(index)\n",
    "    \n",
    "    # Check if two cards are selected\n",
    "    if len(st.session_state.selected) == 2:\n",
    "        st.session_state.moves += 1\n",
    "        card1_idx, card2_idx = st.session_state.selected\n",
    "        \n",
    "        # Check for match\n",
    "        if st.session_state.cards[card1_idx] == st.session_state.cards[card2_idx]:\n",
    "            st.session_state.matched[card1_idx] = True\n",
    "            st.session_state.matched[card2_idx] = True\n",
    "            st.session_state.matches += 1\n",
    "            st.session_state.selected = []\n",
    "            \n",
    "            # Check if game is complete\n",
    "            if st.session_state.matches == len(st.session_state.cards) // 2:\n",
    "                st.session_state.game_complete = True\n",
    "        else:\n",
    "            # Cards don't match - they'll be hidden after rerun\n",
    "            time.sleep(0.5)  # Brief pause to show the second card\n",
    "\n",
    "def reset_non_matched_cards() -> None:\n",
    "    \"\"\"Reset non-matched cards to hidden state\"\"\"\n",
    "    if len(st.session_state.selected) == 2:\n",
    "        card1_idx, card2_idx = st.session_state.selected\n",
    "        if not st.session_state.matched[card1_idx]:\n",
    "            st.session_state.revealed[card1_idx] = False\n",
    "            st.session_state.revealed[card2_idx] = False\n",
    "        st.session_state.selected = []\n",
    "\n",
    "def get_game_time() -> float:\n",
    "    \"\"\"Calculate elapsed game time\"\"\"\n",
    "    if st.session_state.game_complete:\n",
    "        return getattr(st.session_state, 'final_time', 0)\n",
    "    else:\n",
    "        return time.time() - st.session_state.start_time\n",
    "\n",
    "# Initialize session state\n",
    "if 'cards' not in st.session_state:\n",
    "    initialize_game()\n",
    "\n",
    "# Reset non-matched cards if needed\n",
    "if len(st.session_state.selected) == 2 and not all(st.session_state.matched[i] for i in st.session_state.selected):\n",
    "    reset_non_matched_cards()\n",
    "\n",
    "# Main UI\n",
    "st.title(\"🧠 Memory Matching Game\")\n",
    "st.markdown(\"---\")\n",
    "\n",
    "# Game controls and stats\n",
    "col1, col2, col3, col4 = st.columns(4)\n",
    "\n",
    "with col1:\n",
    "    if st.button(\"🎮 New Game (4x4)\", use_container_width=True):\n",
    "        initialize_game(4)\n",
    "        st.rerun()\n",
    "\n",
    "with col2:\n",
    "    if st.button(\"🎯 New Game (6x6)\", use_container_width=True):\n",
    "        initialize_game(6)\n",
    "        st.rerun()\n",
    "\n",
    "with col3:\n",
    "    st.metric(\"Moves\", st.session_state.moves)\n",
    "\n",
    "with col4:\n",
    "    st.metric(\"Time\", f\"{get_game_time():.1f}s\")\n",
    "\n",
    "# Game completion check\n",
    "if st.session_state.game_complete and not hasattr(st.session_state, 'final_time'):\n",
    "    st.session_state.final_time = get_game_time()\n",
    "\n",
    "# Display game completion message\n",
    "if st.session_state.game_complete:\n",
    "    st.success(f\"🎉 Congratulations! You completed the game in {st.session_state.moves} moves and {st.session_state.final_time:.1f} seconds!\")\n",
    "\n",
    "# Game board\n",
    "st.markdown(\"### Game Board\")\n",
    "\n",
    "# Create the grid\n",
    "grid_size = st.session_state.grid_size\n",
    "cols_per_row = grid_size\n",
    "\n",
    "# Display cards in grid format\n",
    "for row in range(grid_size):\n",
    "    cols = st.columns(cols_per_row)\n",
    "    for col_idx in range(cols_per_row):\n",
    "        card_index = row * cols_per_row + col_idx\n",
    "        \n",
    "        with cols[col_idx]:\n",
    "            # Determine what to show on the card\n",
    "            if st.session_state.revealed[card_index] or st.session_state.matched[card_index]:\n",
    "                card_content = st.session_state.cards[card_index]\n",
    "                if st.session_state.matched[card_index]:\n",
    "                    button_type = \"secondary\"  # Matched cards\n",
    "                else:\n",
    "                    button_type = \"primary\"    # Revealed but not yet matched\n",
    "            else:\n",
    "                card_content = \"❓\"\n",
    "                button_type = \"primary\"\n",
    "            \n",
    "            # Create button for the card\n",
    "            if st.button(\n",
    "                card_content,\n",
    "                key=f\"card_{card_index}\",\n",
    "                use_container_width=True,\n",
    "                type=button_type,\n",
    "                disabled=st.session_state.game_complete\n",
    "            ):\n",
    "                handle_card_click(card_index)\n",
    "                st.rerun()\n",
    "\n",
    "# Instructions\n",
    "st.markdown(\"---\")\n",
    "with st.expander(\"📋 How to Play\"):\n",
    "    st.markdown(\"\"\"\n",
    "    **Objective:** Match all pairs of identical emojis!\n",
    "    \n",
    "    **Rules:**\n",
    "    1. Click on cards to reveal them\n",
    "    2. Try to find matching pairs\n",
    "    3. When two cards match, they stay revealed\n",
    "    4. When cards don't match, they flip back over\n",
    "    5. Complete the game by matching all pairs\n",
    "    \n",
    "    **Scoring:**\n",
    "    - Try to complete the game in as few moves as possible\n",
    "    - Beat your best time!\n",
    "    \n",
    "    **Tips:**\n",
    "    - Remember the positions of cards you've seen\n",
    "    - Start by exploring different areas of the board\n",
    "    - Focus on finding matches for cards you remember\n",
    "    \"\"\")\n",
    "\n",
    "# Game statistics\n",
    "st.markdown(\"---\")\n",
    "st.markdown(\"### 📊 Game Stats\")\n",
    "progress = st.session_state.matches / (len(st.session_state.cards) // 2)\n",
    "st.progress(progress, text=f\"Progress: {st.session_state.matches}/{len(st.session_state.cards) // 2} pairs matched\")\n",
    "\n",
    "# Additional info\n",
    "st.markdown(f\"\"\"\n",
    "**Current Game:** {st.session_state.grid_size}x{st.session_state.grid_size} grid ({len(st.session_state.cards)} cards, {len(st.session_state.cards) // 2} pairs)\n",
    "\"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "18162849-d6b1-4f7b-ad5e-ffc797f288f5",
   "metadata": {},
   "outputs": [
    {
     "ename": "OSError",
     "evalue": "Background processes not supported.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m get_ipython()\u001b[38;5;241m.\u001b[39msystem(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mstreamlit run Momo.py &\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\ipykernel\\zmqshell.py:641\u001b[0m, in \u001b[0;36mZMQInteractiveShell.system_piped\u001b[1;34m(self, cmd)\u001b[0m\n\u001b[0;32m    634\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m cmd\u001b[38;5;241m.\u001b[39mrstrip()\u001b[38;5;241m.\u001b[39mendswith(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m&\u001b[39m\u001b[38;5;124m\"\u001b[39m):\n\u001b[0;32m    635\u001b[0m     \u001b[38;5;66;03m# this is *far* from a rigorous test\u001b[39;00m\n\u001b[0;32m    636\u001b[0m     \u001b[38;5;66;03m# We do not support backgrounding processes because we either use\u001b[39;00m\n\u001b[0;32m    637\u001b[0m     \u001b[38;5;66;03m# pexpect or pipes to read from.  Users can always just call\u001b[39;00m\n\u001b[0;32m    638\u001b[0m     \u001b[38;5;66;03m# os.system() or use ip.system=ip.system_raw\u001b[39;00m\n\u001b[0;32m    639\u001b[0m     \u001b[38;5;66;03m# if they really want a background process.\u001b[39;00m\n\u001b[0;32m    640\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mBackground processes not supported.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m--> 641\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mOSError\u001b[39;00m(msg)\n\u001b[0;32m    643\u001b[0m \u001b[38;5;66;03m# we explicitly do NOT return the subprocess status code, because\u001b[39;00m\n\u001b[0;32m    644\u001b[0m \u001b[38;5;66;03m# a non-None value would trigger :func:`sys.displayhook` calls.\u001b[39;00m\n\u001b[0;32m    645\u001b[0m \u001b[38;5;66;03m# Instead, we store the exit_code in user_ns.\u001b[39;00m\n\u001b[0;32m    646\u001b[0m \u001b[38;5;66;03m# Also, protect system call from UNC paths on Windows here too\u001b[39;00m\n\u001b[0;32m    647\u001b[0m \u001b[38;5;66;03m# as is done in InteractiveShell.system_raw\u001b[39;00m\n\u001b[0;32m    648\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m sys\u001b[38;5;241m.\u001b[39mplatform \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mwin32\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n",
      "\u001b[1;31mOSError\u001b[0m: Background processes not supported."
     ]
    }
   ],
   "source": [
    "!streamlit run Momo.py &"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "620c5f4e-5bdb-4492-a5ac-66324b4ae0da",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
