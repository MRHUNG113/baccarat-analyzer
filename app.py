
import streamlit as st
import os
import pandas as pd
from datetime import datetime
from image_processor import extract_big_road, extract_secondary_patterns
from analyzer import analyze_streaks, summarize_patterns, predict_next_move
import matplotlib.pyplot as plt

st.set_page_config(page_title="Baccarat Pattern Analyzer", layout="wide")
st.title("🎲 Phân tích cầu Baccarat từ ảnh")

uploaded_file = st.file_uploader("📤 Tải ảnh bàn Baccarat (PNG/JPG)...", type=["png", "jpg", "jpeg"])

if uploaded_file:
    os.makedirs("uploaded_images", exist_ok=True)
    file_path = f"uploaded_images/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.image(file_path, caption="Ảnh vừa tải lên", use_column_width=True)

    results = extract_big_road(file_path)
    patterns = analyze_streaks(results)
    summary = summarize_patterns(patterns)

    st.subheader("📋 Kết quả trích xuất:")
    st.write("Chuỗi:", " ".join(results))
    st.write("Mẫu cầu:", patterns)

    st.subheader("📊 Phân tích xu hướng:")
    st.json(summary)

    prediction = predict_next_move(results)
    st.subheader("🔮 Dự đoán xu hướng tiếp theo:")
    st.info(prediction)

    st.subheader("👁️ Biểu đồ phụ (Big Eye, Small Road, Cockroach Pig)")
    eye = extract_secondary_patterns(file_path, (0, 40, 320, 715))
    small = extract_secondary_patterns(file_path, (40, 80, 320, 715))
    cockroach = extract_secondary_patterns(file_path, (80, 130, 320, 715))
    st.write("🔴 Big Eye:", eye[-10:])
    st.write("🔵 Small Road:", small[-10:])
    st.write("🐛 Cockroach Pig:", cockroach[-10:])

    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame({'Result': results})
    save_name = f"data/{datetime.today().strftime('%Y-%m-%d')}.csv"
    df.to_csv(save_name, index=False)
    st.success(f"✅ Dữ liệu đã lưu vào {save_name}")

    # Biểu đồ tần suất
    labels = ['Banker', 'Player']
    counts = [results.count('B'), results.count('P')]
    fig, ax = plt.subplots()
    ax.bar(labels, counts, color=['red', 'blue'])
    ax.set_title("Tần suất Banker vs Player")
    st.pyplot(fig)

    # Biểu đồ chuỗi
    lengths = [p[1] for p in patterns]
    fig2, ax2 = plt.subplots()
    ax2.hist(lengths, bins=range(1, max(lengths)+2), color='green', rwidth=0.8)
    ax2.set_title("Biểu đồ độ dài chuỗi")
    ax2.set_xlabel("Độ dài")
    ax2.set_ylabel("Số lần")
    st.pyplot(fig2)
