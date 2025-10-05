import streamlit as st

def basic_health_assessment():
    st.header("Đánh giá Sức khỏe Cơ bản")

    sleep_hours = st.number_input("Số giờ ngủ", min_value=0.0, max_value=24.0)
    weight = st.number_input("Cân nặng (kg)", min_value=1.0)
    height_in_meters = st.number_input("Chiều cao (m)", min_value=0.5)
    calories_in = st.number_input("Calories nạp trong 1 ngày")
    calories_out = st.number_input("Calories tiêu thụ trong 1 ngày")
    meal_per_day = st.number_input("Số bữa ăn trong ngày", min_value=1.0)
    huyet_ap = st.text_input("Huyết áp (Tâm thu/Tâm trương, ví dụ: 120/80)")
    duong_huyet = st.number_input("Đường huyết (mg/dL)")
    mo_mau = st.selectbox("Tình trạng mỡ máu", ["1:Lý tưởng", "2:Biên giới", "3:Rủi ro cao"])
    tinh_trang_dinh_duong = st.selectbox("Tình trạng Dinh dưỡng", ["1:Bình thường", "2:Thừa cân", "3:Béo phì", "4:Thiếu cân"])
    suc_khoe_co_bap = st.selectbox("Sức khỏe Cơ bắp", ["1:Xuất sắc", "2:Tốt", "3:Cần cải thiện"])
    hieu_suat = st.selectbox("Hiệu suất Học tập/Làm việc", ["1:Tốt", "2:Bình thường", "3:Kém"])
    giai_tri = st.selectbox("Khả năng Giải trí", ["1:Tốt", "2:Bình thường", "3:Kém"])

    basic_scores = 0

    # Giấc ngủ
    if 7 <= sleep_hours <= 9:
        basic_scores += 7
    elif 6 <= sleep_hours < 7 or 9 < sleep_hours <= 10:
        basic_scores += 4
    elif 5 <= sleep_hours < 6 or 10 < sleep_hours <= 11:
        basic_scores += 2
    elif 4 <= sleep_hours < 5:
        basic_scores += 1

    # BMI
    BMI = weight / height_in_meters ** 2
    st.metric("Chỉ số BMI", round(BMI, 2))
    if BMI < 18.5:
        basic_scores += 3
    elif 18.5 <= BMI <= 24.9:
        basic_scores += 6
    elif 25 <= BMI <= 29.9:
        basic_scores += 1

    # CICO
    CICO = calories_in - calories_out
    if -100 <= CICO <= 100:
        basic_scores += 7
    elif -300 <= CICO < -100 or 100 < CICO <= 300:
        basic_scores += 5
    elif -500 <= CICO < -300 or 300 < CICO <= 500:
        basic_scores += 3

    # Số bữa ăn
    if 3 <= meal_per_day <= 5:
        basic_scores += 2

    # Huyết áp
    try:
        tam_thu, tam_truong = map(int, huyet_ap.split("/"))
        if tam_thu < 120 and tam_truong < 80:
            basic_scores += 7
        elif 120 <= tam_thu < 130 and 60 <= tam_truong <= 80:
            basic_scores += 5
        elif 130 <= tam_thu <= 139 or 80 <= tam_truong <= 89:
            basic_scores += 3
    except:
        st.warning("Huyết áp không hợp lệ")

    # Đường huyết
    if 70 <= duong_huyet < 100:
        basic_scores += 5
    elif 100 <= duong_huyet <= 125:
        basic_scores += 2

    # Mỡ máu
    if mo_mau.startswith("1"):
        basic_scores += 4
    elif mo_mau.startswith("2"):
        basic_scores += 2

    # Sức khỏe cơ bắp
    if suc_khoe_co_bap.startswith("1"):
        basic_scores += 3
    elif suc_khoe_co_bap.startswith("2"):
        basic_scores += 2

    # Hiệu suất
    if hieu_suat.startswith("1"):
        basic_scores += 6
    elif hieu_suat.startswith("2"):
        basic_scores += 4
    else:
        basic_scores += 2

    # Giải trí
    if giai_tri.startswith("1"):
        basic_scores += 4
    elif giai_tri.startswith("2"):
        basic_scores += 2

    return basic_scores

def advanced_health_assessment():
    st.header("Đánh giá Sức khỏe Nâng cao")
    age = st.number_input("Tuổi", min_value=0)
    if age < 18:
        if age <= 5:
            criteria = ['Tiêm chủng đầy đủ', 'Tăng trưởng & phát triển', 'Ngủ nghỉ hợp lý', 'Phát triển vận động/ngôn ngữ']
        elif age <= 12:
            criteria = ['Hoạt động thể chất', 'Ăn uống lành mạnh', 'Sức khỏe răng miệng', 'Ngủ đủ 9–11 giờ/ngày']
        else:
            criteria = ['Phát triển thể chất', 'Tập thể dục', 'Quản lý stress học tập', 'Thói quen sinh hoạt', 'Chế độ ăn cân bằng', 'Ngủ đủ 8–10 giờ/ngày']
    else:
        gender = st.selectbox("Giới tính", ["Nam", "Nữ"])
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
                criteria = ['Khám phụ khoa', 'Pap smear', 'Tránh thai an toàn', 'Kiểm tra huyết áp', 'Quản lý stress', 'Tự kiểm tra vú']
            elif 30 <= age < 45:
                criteria = ['Tầm soát cổ tử cung', 'Tầm soát ung thư vú', 'Bổ sung Axit Folic']
            elif 45 <= age < 60:
                criteria = ['Chụp nhũ ảnh', 'Tầm soát đại tràng', 'Bổ sung Canxi và Vitamin D']
            else:
                criteria = ['DEXA scan', 'Thị lực', 'Thăng bằng', 'Suy giảm nhận thức', 'Trầm cảm']

    total = 0
    for c in criteria:
        score = st.slider(f"Đánh giá '{c}'", 0.0, 10.0, 5.0)
        total += score
    return total / len(criteria)

# Main App
st.title("Ứng dụng Đánh giá Sức khỏe")

basic_score = basic_health_assessment()
st.subheader(f"Điểm sức khỏe cơ bản (thang 10): {round(basic_score/5, 2)}")

if st.checkbox("Đánh giá thêm sức khỏe nâng cao"):
    advanced_score = advanced_health_assessment()
    total_score = basic_score + advanced_score * 5
    st.subheader(f"Điểm sức khỏe tổng thể (thang 100): {round(total_score, 2)}")

    if total_score >= 90:
        st.success("💪 Sức khỏe rất tốt!")
    elif 70 <= total_score < 90:
        st.info("🙂 Sức khỏe tốt.")
    elif 50 <= total_score < 70:
        st.warning("😐 Sức khỏe trung bình.")
    elif 30 <= total_score < 50:
        st.error("⚠️ Sức khỏe kém.")
    else:
        st.error("🚨 Bạn nên đi khám bác sĩ ngay!")
else:
    if basic_score >= 40:
        st.success("💪 Sức khỏe rất tốt!")
    elif 30 <= basic_score < 40:
        st.info("🙂 Sức khỏe tốt.")
    elif 20 <= basic_score < 30:
        st.warning("😐 Sức khỏe trung bình.")
    elif 10 <= basic_score < 20:
        st.error("⚠️ Sức khỏe kém.")
    else:
        st.error("🚨 Bạn nên đi khám bác sĩ ngay!")
