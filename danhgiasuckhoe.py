import streamlit as st

def basic_health_assessment():
    st.header("🔍 Đánh giá sức khỏe cơ bản")
    scores = 0

    with st.expander("🛌 Thói quen sinh hoạt"):
        sleep_hours = st.number_input("Số giờ ngủ mỗi ngày", min_value=0.0, max_value=24.0, step=0.5)
        meal_per_day = st.number_input("Số bữa ăn trong ngày", min_value=0.0)

    with st.expander("⚖️ Thông tin thể chất"):
        weight = st.number_input("Cân nặng (kg)", min_value=0.0)
        height = st.number_input("Chiều cao (m)", min_value=0.0)
        calories_in = st.number_input("Calories nạp mỗi ngày", min_value=0.0)
        calories_out = st.number_input("Calories tiêu thụ mỗi ngày", min_value=0.0)

    with st.expander("🩺 Chỉ số sức khỏe"):
        huyet_ap = st.text_input("Huyết áp (Tâm thu/Tâm trương, ví dụ: 120/80)")
        duong_huyet = st.number_input("Đường huyết (mg/dL)", min_value=0.0)
        mo_mau = st.selectbox("Tình trạng mỡ máu", ["1:Lý tưởng", "2:Biên giới", "3:Rủi ro cao"])
        tinh_trang_dinh_duong = st.selectbox("Tình trạng Dinh dưỡng", ["1:Bình thường", "2:Thừa cân", "3:Béo phì", "4:Thiếu cân"])

    with st.expander("💪 Hiệu suất & Cơ bắp"):
        suc_khoe_co_bap = st.selectbox("Sức khỏe Cơ bắp", ["1:Xuất sắc", "2:Tốt", "3:Cần cải thiện"])
        hieu_suat = st.selectbox("Hiệu suất Học tập/Làm việc", ["1:Tốt", "2:Bình thường", "3:Kém"])
        giai_tri = st.selectbox("Khả năng Giải trí", ["1:Tốt", "2:Bình thường", "3:Kém"])

    # Giấc ngủ
    if 7 <= sleep_hours <= 9: scores += 7
    elif 6 <= sleep_hours < 7 or 9 < sleep_hours <= 10: scores += 4
    elif 5 <= sleep_hours < 6 or 10 < sleep_hours <= 11: scores += 2
    elif 4 <= sleep_hours < 5: scores += 1

    # BMI
    if height > 0:
        BMI = weight / height ** 2
        st.write(f"📊 Chỉ số BMI: {BMI:.2f}")
        if BMI < 18.5: scores += 3
        elif 18.5 <= BMI <= 24.9: scores += 6
        elif 25 <= BMI <= 29.9: scores += 1

    # CICO
    CICO = calories_in - calories_out
    st.write(f"⚖️ Cân bằng năng lượng (CICO): {CICO:.0f} kcal")
    if -100 <= CICO <= 100: scores += 7
    elif -300 <= CICO < -100 or 100 < CICO <= 300: scores += 5
    elif -500 <= CICO < -300 or 300 < CICO <= 500: scores += 3

    # Bữa ăn
    if 3 <= meal_per_day <= 5: scores += 2

    # Huyết áp
    try:
        tam_thu, tam_truong = map(int, huyet_ap.split("/"))
        if tam_thu < 120 and tam_truong < 80: scores += 7
        elif 120 <= tam_thu < 130 and tam_truong < 80: scores += 5
        elif 130 <= tam_thu <= 139 or 80 <= tam_truong <= 89: scores += 3
        elif tam_thu >= 140 or tam_truong >= 90: scores += 0
    except:
        st.warning("⚠️ Định dạng huyết áp không hợp lệ.")

    # Đường huyết
    if duong_huyet < 100: scores += 5
    elif 100 <= duong_huyet <= 125: scores += 2

    # Mỡ máu
    if mo_mau.startswith("1"): scores += 4
    elif mo_mau.startswith("2"): scores += 2

    # Cơ bắp
    if suc_khoe_co_bap.startswith("1"): scores += 3
    elif suc_khoe_co_bap.startswith("2"): scores += 2

    # Hiệu suất
    if hieu_suat.startswith("1"): scores += 6
    elif hieu_suat.startswith("2"): scores += 4
    else: scores += 2

    # Giải trí
    if giai_tri.startswith("1"): scores += 4
    elif giai_tri.startswith("2"): scores += 2

    return scores


def advanced_health_assessment():
    st.header("📈 Đánh giá sức khỏe nâng cao")
    age = st.number_input("Tuổi", min_value=0)
    gender = st.selectbox("Giới tính", ["Nam", "Nữ"])
    criteria = []

    if gender == "Nam":
        if 18 <= age < 30:
            criteria = ['Tiêm chủng', 'Hoạt động thể chất', 'Ăn uống lành mạnh', 'Mức độ hút thuốc', 'Sức khỏe tâm thần']
        elif 30 <= age < 50:
            criteria = ['Tốc độ chuyển hóa', 'Quản lý căng thẳng', 'Hoạt động thể chất']
        elif 50 <= age < 69:
            criteria = ['Tầm soát ung thư đại tràng', 'Tầm soát tiền liệt tuyến', 'Tầm soát tim mạch']
        else:
            criteria = ['Thính giác', 'Thị lực', 'Mật độ xương', 'Trí nhớ', 'Trầm cảm']
    else:
        if 18 <= age < 30:
            criteria = ['Khám phụ khoa', 'Pap smear', 'Tránh thai an toàn', 'Quản lý stress', 'Tự kiểm tra vú']
        elif 30 <= age < 45:
            criteria = ['Tầm soát cổ tử cung', 'Tầm soát ung thư vú', 'Bổ sung Axit Folic']
        elif 45 <= age < 60:
            criteria = ['Chụp nhũ ảnh', 'Tầm soát đại tràng', 'Bổ sung Canxi và Vitamin D']
        else:
            criteria = ['DEXA scan', 'Thị lực', 'Thăng bằng', 'Suy giảm nhận thức', 'Trầm cảm']

    total = 0
    for c in criteria:
        score = st.slider(f"Đánh giá '{c}' từ 1 đến 10", 1, 10)
        total += score

    average = total / len(criteria) if criteria else 0
    return average * 5


# Main App
st.title("🩺 Ứng dụng Đánh giá Sức khỏe Toàn diện")

basic_score = basic_health_assessment()
st.metric("✅ Điểm sức khỏe cơ bản", f"{basic_score / 5:.2f}/10")
st.progress(int(basic_score / 5 * 10))

if st.checkbox("👉 Thực hiện đánh giá nâng cao"):
    advanced_score = advanced_health_assessment()
    total_score = basic_score + advanced_score
    st.subheader(f"🌟 Tổng điểm sức khỏe (thang 100): {total_score:.2f}")

    if total_score >= 90:
        st.success("💪 Sức khỏe rất tốt!")
    elif 70 <= total_score < 90:
        st.info("😊 Sức khỏe tốt.")
    elif 50 <= total_score < 70:
        st.warning("😐 Sức khỏe trung bình.")
    elif 30 <= total_score < 50:
        st.error("😟 Sức khỏe kém.")
    else:
        st.error("🚨 Bạn nên đi khám bác sĩ ngay!")