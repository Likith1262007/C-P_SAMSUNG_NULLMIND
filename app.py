import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="CampusConnect AI | Dashboard",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

    :root {
        --navy: #172554;
        --purple: #6d5ce8;
        --muted: #718096;
        --line: #e8ebf3;
    }

    .stApp {
        background: #f7f8fc;
        color: #1c2541;
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e8ebf3;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.25rem;
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] > div {
        gap: 0.3rem;
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] label {
        border-radius: 10px;
        padding: 0.55rem 0.7rem;
        color: #64708a;
        font-size: 0.94rem;
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {
        background: #f0efff;
        color: #5143c5;
        font-weight: 700;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin: 0.25rem 0 1.6rem;
    }

    .brand-mark {
        display: grid;
        place-items: center;
        width: 42px;
        height: 42px;
        border-radius: 13px;
        background: linear-gradient(140deg, #263c84, #705ce7);
        color: white;
        font: 800 0.95rem 'Manrope', sans-serif;
        letter-spacing: -0.06em;
        box-shadow: 0 6px 15px rgba(73, 72, 179, 0.22);
    }

    .brand-name {
        color: #172554;
        font: 800 1rem 'Manrope', sans-serif;
        line-height: 1.2;
    }

    .brand-caption {
        color: #8992a6;
        font-size: 0.72rem;
        margin-top: 0.2rem;
    }

    .sidebar-label {
        color: #a0a7b6;
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.13em;
        margin: 0 0 0.6rem 0.65rem;
        text-transform: uppercase;
    }

    .welcome-kicker {
        color: #6d5ce8;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        margin-bottom: 0.45rem;
        text-transform: uppercase;
    }

    .welcome-title {
        color: #172554;
        font: 800 clamp(1.7rem, 3vw, 2.25rem) 'Manrope', sans-serif;
        letter-spacing: -0.045em;
        line-height: 1.2;
        margin: 0;
    }

    .welcome-subtitle {
        color: #79849a;
        font-size: 1rem;
        margin: 0.45rem 0 0;
    }

    .live-pill {
        background: #eefaf4;
        border: 1px solid #d5f1e1;
        border-radius: 999px;
        color: #278454;
        display: inline-block;
        font-size: 0.78rem;
        font-weight: 600;
        padding: 0.45rem 0.75rem;
        white-space: nowrap;
    }

    .section-heading {
        color: #202b49;
        font: 700 1.05rem 'Manrope', sans-serif;
        letter-spacing: -0.02em;
        margin: 0 0 0.25rem;
    }

    .section-caption {
        color: #8992a6;
        font-size: 0.82rem;
        margin: 0 0 0.9rem;
    }

    .metric-card {
        background: #ffffff;
        border: 1px solid #edf0f6;
        border-radius: 16px;
        box-shadow: 0 5px 18px rgba(27, 39, 78, 0.045);
        min-height: 145px;
        padding: 1.05rem 1.15rem;
    }

    .metric-top {
        align-items: center;
        display: flex;
        justify-content: space-between;
    }

    .metric-icon {
        align-items: center;
        border-radius: 11px;
        display: flex;
        font-size: 1.05rem;
        height: 38px;
        justify-content: center;
        width: 38px;
    }

    .metric-label {
        color: #7a849a;
        font-size: 0.84rem;
        font-weight: 500;
        margin-top: 0.85rem;
    }

    .metric-value {
        color: #182547;
        font: 800 1.8rem 'Manrope', sans-serif;
        letter-spacing: -0.045em;
        line-height: 1.15;
        margin-top: 0.15rem;
    }

    .metric-note {
        color: #9aa2b2;
        font-size: 0.73rem;
        margin-top: 0.35rem;
    }

    .panel-title {
        color: #202b49;
        font: 700 0.98rem 'Manrope', sans-serif;
        margin: 0.2rem 0 0;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff;
        border-color: #edf0f6;
        border-radius: 16px;
        box-shadow: 0 5px 18px rgba(27, 39, 78, 0.04);
    }

    div[data-testid="stDataFrame"] {
        border: 1px solid #edf0f6;
        border-radius: 12px;
        overflow: hidden;
    }

    footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)


navigation = {
    "▦  Dashboard": "Dashboard",
    "◉  Student Portal": "Student Portal",
    "◈  Faculty Portal": "Faculty Portal",
    "▤  Admin Dashboard": "Admin Dashboard",
    "⌂  Maintenance Portal": "Maintenance Portal",
    "▥  Analytics": "Analytics",
    "▧  Campus Notices": "Campus Notices",
}


with st.sidebar:
    st.markdown(
        """
        <div class="brand">
            <div class="brand-mark">CC</div>
            <div>
                <div class="brand-name">CampusConnect AI</div>
                <div class="brand-caption">Smart campus, connected</div>
            </div>
        </div>
        <div class="sidebar-label">Workspace</div>
        """,
        unsafe_allow_html=True,
    )
    selected_item = st.radio(
        "Campus navigation",
        options=list(navigation.keys()),
        index=0,
        label_visibility="collapsed",
    )
    selected_page = navigation[selected_item]
    st.markdown(
        """
        <div style="border-top:1px solid #edf0f6; margin-top:1.2rem; padding:1rem 0.5rem 0;">
            <div style="color:#8b95a9;font-size:0.75rem;">Campus Issue Management</div>
            <div style="color:#b0b7c5;font-size:0.7rem;margin-top:0.3rem;">Initial dashboard preview</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if selected_page != "Dashboard":
    st.markdown(
        f"""
        <div class="welcome-kicker">CampusConnect AI</div>
        <h1 class="welcome-title">{selected_page}</h1>
        <p class="welcome-subtitle">This area is reserved for a future CampusConnect AI module.</p>
        """,
        unsafe_allow_html=True,
    )
    st.info("The current build is focused on the dashboard. Other modules will be added after approval.")
    st.stop()


st.markdown(
    """
    <div class="welcome-kicker">Campus overview</div>
    <h1 class="welcome-title">Welcome to CampusConnect AI</h1>
    <p class="welcome-subtitle">Smart solutions for a better campus.</p>
    """,
    unsafe_allow_html=True,
)
st.write("")

stats = [
    ("Total Complaints", "120", "All reported campus issues", "▤", "#eeefff", "#5d50d6"),
    ("Pending Complaints", "35", "Awaiting resolution", "◷", "#fff5e8", "#d88920"),
    ("Resolved Complaints", "70", "Successfully addressed", "✓", "#eaf8f1", "#279265"),
    ("High Priority Complaints", "15", "Require prompt attention", "!", "#fff0f1", "#d84e62"),
]

metric_columns = st.columns(4, gap="medium")
for column, (label, value, note, icon, icon_bg, icon_color) in zip(metric_columns, stats):
    with column:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-top">
                    <div class="metric-icon" style="background:{icon_bg};color:{icon_color};">{icon}</div>
                </div>
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-note">{note}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
chart_column, status_column = st.columns([1, 1], gap="medium")

category_data = pd.DataFrame(
    {
        "Category": ["Electrical", "Water", "Internet", "Sanitation", "Infrastructure"],
        "Complaints": [32, 24, 21, 18, 25],
    }
)
category_colors = ["#5145cd", "#7869e8", "#a69bf1", "#c5bef7", "#263c84"]
category_chart = px.pie(
    category_data,
    names="Category",
    values="Complaints",
    hole=0.62,
    color="Category",
    color_discrete_sequence=category_colors,
)
category_chart.update_traces(
    textposition="outside",
    textinfo="label+percent",
    hovertemplate="%{label}: %{value} complaints<extra></extra>",
    marker_line_color="#ffffff",
    marker_line_width=3,
)
category_chart.update_layout(
    height=320,
    margin=dict(t=16, b=14, l=12, r=12),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans, sans-serif", color="#64708a", size=11),
    showlegend=False,
    annotations=[
        dict(
            text="<b>120</b><br><span style='font-size:11px'>complaints</span>",
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=19, color="#172554"),
        )
    ],
)

status_data = pd.DataFrame(
    {
        "Status": ["Submitted", "Assigned", "In Progress", "Resolved"],
        "Complaints": [10, 10, 15, 70],
    }
)
status_chart = px.bar(
    status_data,
    x="Status",
    y="Complaints",
    color="Status",
    color_discrete_map={
        "Submitted": "#9d91ee",
        "Assigned": "#7769e7",
        "In Progress": "#5145cd",
        "Resolved": "#263c84",
    },
)
status_chart.update_traces(
    hovertemplate="%{x}: %{y} complaints<extra></extra>",
    marker_line_width=0,
)
status_chart.update_layout(
    height=320,
    margin=dict(t=16, b=12, l=8, r=8),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans, sans-serif", color="#64708a", size=11),
    showlegend=False,
    xaxis=dict(title=None, showgrid=False, linecolor="#e8ebf3"),
    yaxis=dict(title=None, showgrid=True, gridcolor="#edf0f6", zeroline=False),
    bargap=0.42,
)

with chart_column:
    with st.container(border=True):
        st.markdown('<div class="panel-title">Complaints by category</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">Reported issues across campus services</div>', unsafe_allow_html=True)
        st.plotly_chart(category_chart, width="stretch", config={"displayModeBar": False})

with status_column:
    with st.container(border=True):
        st.markdown('<div class="panel-title">Complaints by status</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-caption">Status breakdown · 15 archived records not shown</div>',
            unsafe_allow_html=True,
        )
        st.plotly_chart(status_chart, width="stretch", config={"displayModeBar": False})

st.write("")
st.markdown('<div class="section-heading">Recent complaints</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-caption">A snapshot of the latest issues reported by the campus community</div>',
    unsafe_allow_html=True,
)

recent_complaints = pd.DataFrame(
    [
        ["CC-0120", "Lights out in east corridor", "Electrical", "Science Block · Floor 2", "High", "Submitted"],
        ["CC-0119", "Water cooler not dispensing", "Water", "Library · Ground Floor", "Medium", "Assigned"],
        ["CC-0118", "Wi-Fi drops in lecture hall", "Internet", "Engineering Block · Room 204", "High", "In Progress"],
        ["CC-0117", "Overflowing bin near cafeteria", "Sanitation", "Student Center · Cafeteria", "Low", "Resolved"],
        ["CC-0116", "Cracked paving near main gate", "Infrastructure", "North Gate · Walkway", "Medium", "Resolved"],
    ],
    columns=["Complaint ID", "Complaint Title", "Category", "Location", "Priority", "Status"],
)

st.dataframe(
    recent_complaints,
    width="stretch",
    hide_index=True,
    height=245,
    column_config={
        "Complaint ID": st.column_config.TextColumn("Complaint ID", width="small"),
        "Complaint Title": st.column_config.TextColumn("Complaint Title", width="large"),
        "Category": st.column_config.TextColumn("Category", width="medium"),
        "Location": st.column_config.TextColumn("Location", width="large"),
        "Priority": st.column_config.TextColumn("Priority", width="small"),
        "Status": st.column_config.TextColumn("Status", width="medium"),
    },
)
