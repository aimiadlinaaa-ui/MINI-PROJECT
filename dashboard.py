import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F5F5DC;
    }
    </style>
    """,
    unsafe_allow_html=True
)


#st.image(r'C:\Users\welcome\Desktop\BSMS1306\streamlit\Header.png')
st.image('polka.jpg', width=1500)

st.title("AI Usage Among Students Dashboard")
st.write("Analysis of AI usage, academic perfomance and career confidence among students.")

#lagu
audio_file = open('Jennifer Lopez - On The Floor ft. Pitbull.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')


#df = pd.read_csv(r"C:\Users\welcome\Desktop\BSMS1306\streamlit\Tips.csv")
df=pd.read_csv("AI_Impact_Student_Life_2026.csv")
#df = pd.read_csv(upload_file)

df =df.rename(columns={'Student_ID':'Student ID'})
df =df.rename(columns={'Primary_AI_Tool':'Primary AI Tool'})
df =df.rename(columns={'Task_Frequency_Daily':'Task Frequency Daily'})
df =df.rename(columns={'Main_Usage_Case':'Main Usage Case'})
df =df.rename(columns={'GPA_Baseline':'GPA Baseline'})
df =df.rename(columns={'GPA_Post_AI':'GPA Post AI'})
df =df.rename(columns={'Time_Saved_Hours_Weekly':'Time Saved Hours Weekly'})
df =df.rename(columns={'AI_Ethics_Concern':'AI Ethics Concern'})
df =df.rename(columns={'Career_Confidence_Score':'Career Confidence Score'})


#pie chart
st.subheader("Main Usage Case Distribution")

usage_counts = df['Main Usage Case'].value_counts()
fig, ax = plt.subplots()

colors = ['#8C85C7','#A7C1EB','#F2DAE8','#F2BAD8','#F2A5D2']

plt.figure(figsize=(8,5))

ax.pie(
    usage_counts,
    labels=usage_counts.index,
    autopct='%1.1f%%',
    colors=colors
)

plt.title('Distribution of Main Usage Cases')

plt.show()
st.pyplot(fig)


#bar chart
st.subheader("Most Popular AI Tool")

tool_counts = df['Primary AI Tool'].value_counts()
fig, ax = plt.subplots()
ax.bar(tool_counts.index, tool_counts.values)
plt.figure(figsize=(5,5))

ax.bar(
    tool_counts.index,
    tool_counts.values,
    color=['#E5EBD7','#FCF3F0','#D4EEE3','#F6E8DE','#F7D7D7']
)

plt.title('Most Popular AI Tools')
plt.xlabel('AI Tool')
plt.ylabel('Number of Students')

plt.show()
st.pyplot(fig)


#bar chart 2
st.subheader("Average Weekly Time Saved by AI Tool")
fig, ax = plt.subplots(figsize=(8,5))
tool_time = (
    df.groupby('Primary AI Tool')
    ['Time Saved Hours Weekly']
    .mean()
    .sort_values(ascending=False)
)

bars = ax.bar(
    tool_time.index,
    tool_time.values,
    color=['#D4EEE3','#FCF3F0','#E5EBD7','#F7D7D7','#F6E8DE']
)

ax.set_xlabel('AI Tool')
ax.set_ylabel('Hours Saved')

st.pyplot(fig)


#boxplot
box = plt.boxplot(
    [df['GPA Baseline'],df['GPA Post AI']],
    patch_artist=True,
    tick_labels=['Before AI','After AI']
)

colors = ['#FFDFC9','#DFBBBB']

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
