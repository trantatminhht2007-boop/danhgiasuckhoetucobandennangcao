import streamlit as st

# ---------- Hàm đánh giá sức khỏe cơ bản ----------
def basic_health_assessment():
    st.subheader("Đánh giá sức khỏe cơ bản")

    sleep_hours = st.slider("Số giờ ngủ (giờ)", 0.0, 12.0, 7.0, 0.5)
    weight = st.number_input("Cân nặng (kg)", 30.0, 200.0, 60.0)
    height_in_meters = st.number_input("Chiều cao (m)", 1.2, 2.2, 1.7)
    calories_in = st.number_input("Calories nạp trong ngày", 500.0, 6000.0, 2000.0)
    calories_out = st.number_input("Calories tiêu hao trong ngày", 500.0, 6000.0, 2000.0)
    meal_per_day = st.slider("Số bữa ăn trong ngày", 1, 7, 3)

    huyet_ap = st.text_input("Huyết áp (Tâm thu/Tâm trương, ví dụ: 120/80)", "120/80")
    duong_huyet = st.number_input("Đường huyết (mg/dL)", 50.0, 300.0, 90.0)

    mo_mau = st.selectbox("Tình trạng mỡ máu", ["1: Lý tưởng", "2: Biên giới", "3: Rủi ro cao"])
    tinh_trang_dinh_duong = st.selectbox("Tình trạng dinh dưỡng", ["1: Bình thường", "2: Thừa cân", "3: Béo phì", "4: Thiếu cân"])
    suc_khoe_co_bap = st.selectbox("Sức khỏe cơ bắp", ["1: Xuất sắc", "2: Tốt", "3: Cần cải thiện"])
    hieu_suat = st.selectbox("Hiệu suất học tập/làm việc", ["1: Tốt", "2: Bình thường", "3: Kém"])
    giai_tri = st.selectbox("Khả năng giải trí", ["1: Tốt", "2: Bình thường", "3: Kém"])

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
    BMI = weight / (height_in_meters ** 2)
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
        elif 120 <= tam_thu < 130 and tam_truong < 80:
            basic_scores += 5
        elif 130 <= tam_thu <= 139 or 80 <= tam_truong <= 89:
            basic_scores += 3
    except:
        st.warning("⚠️ Dữ liệu huyết áp không hợp lệ")

    # Đường huyết
    if duong_huyet < 100:
        basic_scores += 5
    elif 100 <= duong_huyet <= 125:
        basic_scores += 2

    # Mỡ máu
    if "1" in mo_mau:
        basic_scores += 4
    elif "2" in mo_mau:
        basic_scores += 2

    # Cơ bắp
    if "1" in suc_khoe_co_bap:
        basic_scores += 3
    elif "2" in suc_khoe_co_bap:
        basic_scores += 2

    # Hiệu suất
    if "1" in hieu_suat:
        basic_scores += 6
    elif "2" in hieu_suat:
        basic_scores += 4
    else:
        basic_scores += 2

    # Giải trí
    if "1" in giai_tri:
        basic_scores += 4
    elif "2" in giai_tri:
        basic_scores += 2

    return basic_scores, BMI


# ---------- Hàm đánh giá nâng cao ----------
def advanced_health_assessment():
    st.subheader("Đánh giá sức khỏe nâng cao cho người trên 18 tuổi")

    age = st.number_input("Tuổi", 10, 100, 25)
    gender = st.radio("Giới tính", ["Nam", "Nữ"])
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
            criteria = ['Khám phụ khoa', 'Pap smear', 'Tránh thai an toàn', 'Kiểm tra huyết áp', 'Quản lý stress', 'Tự kiểm tra vú']
        elif 30 <= age < 45:
            criteria = ['Tầm soát cổ tử cung', 'Tầm soát ung thư vú', 'Bổ sung Axit Folic']
        elif 45 <= age < 60:
            criteria = ['Chụp nhũ ảnh', 'Tầm soát đại tràng', 'Bổ sung Canxi và Vitamin D']
        else:
            criteria = ['DEXA scan', 'Thị lực', 'Thăng bằng', 'Suy giảm nhận thức', 'Trầm cảm']

    total = 0
    for c in criteria:
        score = st.slider(f"Đánh giá {c}", 1, 10, 5)
        total += score

    average = total / len(criteria) if criteria else 0
    return average


# ---------- Ứng dụng chính ----------
st.title("Ứng dụng đánh giá sức khỏe")

basic_score, BMI = basic_health_assessment()
st.write("---")
st.metric("Điểm sức khỏe cơ bản (thang 10)", round(basic_score/5, 1))
st.metric("Chỉ số BMI", round(BMI, 1))

if st.checkbox("Thực hiện đánh giá nâng cao"):
    advanced_score = advanced_health_assessment()
    total_score = basic_score + advanced_score * 5

    st.write("---")
    st.subheader("Kết quả tổng hợp")
    st.metric("Điểm sức khỏe tổng quát (thang 100)", round(total_score, 1))

    if total_score >= 90:
        st.success("Sức khỏe rất tốt")
    elif 70 <= total_score < 90:
        st.info("Sức khỏe tốt")
    elif 50 <= total_score < 70:
        st.warning("Sức khỏe trung bình")
    elif 30 <= total_score < 50:
        st.error("Sức khỏe kém")
    else:
        st.error("Bạn nên đi khám bác sĩ ngay")
