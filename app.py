import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# 페이지 설정
st.set_page_config(
    page_title="DEEP BLUE - Generative Poster",
    layout="centered"
)

# 헤더 및 캡션
st.title("🌊 DEEP BLUE")
st.caption("Arts and Advanced Big Data | Generative Poster Study")

# 사이드바 컨트롤러
st.sidebar.header("Controls")

layers = st.sidebar.slider(
    "Layers",
    min_value=3,
    max_value=16,
    value=7,
    step=1
)

wobble = st.sidebar.slider(
    "Wobble",
    min_value=0.02,
    max_value=0.35,
    value=0.12,
    step=0.01
)

palette_mode = st.sidebar.selectbox(
    "Palette mode",
    ["Deep Ocean", "Calm Shore", "Abyssal Navy"]
)

seed = st.sidebar.slider(
    "Seed",
    min_value=0,
    max_value=9999,
    value=42,
    step=1
)

def draw_poster(n_layers, wobble_val, mode, seed_val):
    rng = np.random.default_rng(seed_val)
    
    if mode == "Deep Ocean":
        palette = ['#0F2537', '#1D4E89', '#00B4D8', '#90E0EF', '#D8B168']
    elif mode == "Calm Shore":
        palette = ['#2A6F97', '#468FAF', '#61A5C2', '#89C2D9', '#A9D6E5']
    else:
        palette = ['#03045E', '#023E8A', '#0077B6', '#0096C7', '#48CAE4']

    bg_color = '#F4F7F6'
    
    fig, ax = plt.subplots(figsize=(6, 8), dpi=150)
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    ax.set(xlim=(0, 1), ylim=(0, 1), aspect='equal')
    ax.axis("off")

    ax.text(0.08, 0.93, 'DEEP BLUE', fontsize=24, weight='bold', va='top', color='#0A192F')
    ax.text(0.085, 0.86, f'ORGANIC CURRENT • {mode.upper()}', fontsize=7, color='#4A5568')
    ax.plot([0.085, 0.915], [0.82, 0.82], color='#CBD5E1', lw=0.8)
    ax.text(0.085, 0.08, 'AN EXPLORATION OF DEPTH, FLUIDITY, AND LAYERS', fontsize=7, color='#64748B')

    theta = np.linspace(0, 2 * np.pi, 250, endpoint=False)
    for i in range(n_layers):
        ang = i * 2.39996
        cx, cy = 0.5 + 0.12 * np.cos(ang), 0.46 + 0.12 * np.sin(ang)
        p, q = rng.uniform(0, 2 * np.pi, 2)
        r = rng.uniform(0.16, 0.25) * (1 + wobble_val * (0.6 * np.sin(3 * theta + p) + 0.4 * np.sin(5 * theta + q)))
        pts = np.c_[cx + r * np.cos(theta), cy + r * np.sin(theta)]
        ax.add_patch(Polygon(pts, facecolor=palette[i % len(palette)], edgecolor='none', alpha=0.55))

    plt.tight_layout()
    return fig

fig = draw_poster(layers, wobble, palette_mode, seed)
st.pyplot(fig)
