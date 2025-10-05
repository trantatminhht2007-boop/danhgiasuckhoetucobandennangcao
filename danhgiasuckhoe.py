import streamlit as st

# ================== HÀM ĐÁNH GIÁ SỨC KHỎE CƠ BẢN ==================
def basic_health_assessment(sleep_hours, weight, height_in_meters, calories_in, calories_out,
                            meal_per_day, huyet_ap, duong_huyet, mo_mau, tinh_trang_dinh_duong,
                            suc_khoe_co_bap, hieu_suat, giai_tri):
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
    except:
        tam_thu, tam_truong = 120, 80
    if tam_thu < 120 and tam_truong < 80:
        basic_scores += 7
    elif 120 <= tam_thu < 130 and tam_truong < 80:
        basic_scores += 5
    elif 130 <= tam_thu <= 139 or 80 <= tam_truong <= 89:
        basic_scores += 3

    # Đường huyết
    if 70 <= duong_huyet < 100:
        basic_scores += 5
    elif 100 <= duong_huyet <= 125:
        basic_scores += 2

    # Mỡ máu
    if mo_mau == "1":
        basic_scores += 4
    elif mo_mau == "2":
        basic_scores += 2

    # Sức khỏe cơ bắp
    if suc_khoe_co_bap == "1":
        basic_scores += 3
    elif suc_khoe_co_bap == "2":
        basic_scores += 2

    # Hiệu suất học tập/làm việc
    if hieu_suat == "1":
        basic_scores += 6
    elif hieu_suat == "2":
        basic_scores += 4
    else:
        basic_scores += 2

    # Giải trí
    if giai_tri == "1":
        basic_scores += 4
    elif giai_tri == "2":
        basic_scores += 2

    return basic_scores, BMI, CICO


# ================== HÀM ĐÁNH GIÁ TRẺ EM ==================
def child_health_assessment(age):
    if age <= 5:
        criteria = ['Tiêm chủng đầy đủ', 'Tăng trưởng & phát triển', 'Ngủ nghỉ hợp lý', 'Phát triển vận động/ngôn ngữ']
    elif age <= 12:
        criteria = ['Hoạt động thể chất', 'Ăn uống lành mạnh', 'Sức khỏe răng miệng', 'Ngủ đủ 9–11 giờ/ngày']
    elif age <= 18:
        criteria = ['Phát triển thể chất', 'Tập thể dục', 'Quản lý stress học tập',
                    'Thói quen sinh hoạt', 'Chế độ ăn cân bằng', 'Ngủ đủ 8–10 giờ/ngày']
    else:
        return 0

    total = 0
    for c in criteria:
        score = st.slider(f"Đánh giá '{c}'", 1, 10, 5)
        total += score
    return total / len(criteria)


# ================== HÀM ĐÁNH GIÁ NGƯỜI LỚN ==================
def adult_health_assessment(age, gender):
    if gender == "Nam":
        if 18 <= age < 30:
            criteria = ['Tiêm chủng', 'Hoạt động thể chất', 'Ăn uống lành mạnh', 'Mức độ hút thuốc', 'Sức khỏe tâm thần']
        elif 30 <= age < 50:
            criteria = ['Tốc độ chuyển hóa', 'Quản lý căng thẳng', 'Hoạt động thể chất']
        elif 50 <= age < 69:
            criteria = ['Tầm soát ung thư đại tràng', 'Tầm soát tiền liệt tuyến', 'Tầm soát tim mạch']
        else:
            criteria = ['Thính giác', 'Thị lực', 'Mật độ xương', 'Trí nhớ', 'Trầm cảm']
    elif gender == "Nữ":
        if 18 <= age < 30:
            criteria = ['Khám phụ khoa', 'Pap smear', 'Tránh thai an toàn',
                        'Kiểm tra huyết áp', 'Quản lý stress', 'Tự kiểm tra vú']
        elif 30 <= age < 45:
            criteria = ['Tầm soát cổ tử cung', 'Tầm soát ung thư vú', 'Bổ sung Axit Folic']
        elif 45 <= age < 60:
            criteria = ['Chụp nhũ ảnh', 'Tầm soát đại tràng', 'Bổ sung Canxi và Vitamin D']
        else:
            criteria = ['DEXA scan', 'Thị lực', 'Thăng bằng', 'Suy giảm nhận thức', 'Trầm cảm']
    else:
        st.error("Giới tính không hợp lệ.")
        return 0

    total = 0
    for c in criteria:
        score = st.slider(f"Đánh giá '{c}'", 1, 10, 5)
        total += score
    return total / len(criteria)


# ================== HÀM ĐÁNH GIÁ NÂNG CAO ==================
def advanced_health_assessment():
    age = st.number_input("Tuổi", min_value=1, max_value=120, step=1)
    if age < 18:
        return child_health_assessment(age)
    else:
        gender = st.radio("Giới tính", ["Nam", "Nữ"])
        return adult_health_assessment(age, gender)


# ================== GIAO DIỆN STREAMLIT ==================
st.set_page_config(page_title="Ứng dụng Đánh giá Sức khỏe", layout="wide")
st.title("🩺 Ứng dụng Đánh giá Sức khỏe Toàn diện (Theo thang điểm) ")

tab1, tab2 = st.tabs(["Đánh giá Cơ bản", "Đánh giá Nâng cao"])

# TAB 1: ĐÁNH GIÁ CƠ BẢN
with tab1:
    st.header("📊 Đánh giá sức khỏe cơ bản")

    sleep_hours = st.number_input("Số giờ ngủ", 0.0, 24.0, 7.0)
    weight = st.number_input("Cân nặng (kg)", 10.0, 200.0, 60.0)
    height_in_meters = st.number_input("Chiều cao (m)", 0.5, 2.5, 1.7)
    calories_in = st.number_input("Calories nạp trong 1 ngày", 0.0, 10000.0, 2000.0)
    calories_out = st.number_input("Calories tiêu thụ trong 1 ngày", 0.0, 10000.0, 2000.0)
    meal_per_day = st.number_input("Số bữa ăn trong ngày", 1.0, 10.0, 3.0)
    huyet_ap = st.text_input("Huyết áp (ví dụ: 120/80)", "120/80")
    duong_huyet = st.number_input("Đường huyết (mg/dL)", 50.0, 300.0, 90.0)
    mo_mau = st.radio("Tình trạng mỡ máu", ["1", "2", "3"])
    tinh_trang_dinh_duong = st.radio("Tình trạng Dinh dưỡng", ["1", "2", "3", "4"])
    suc_khoe_co_bap = st.radio("Sức khỏe Cơ bắp", ["1", "2", "3"])
    hieu_suat = st.radio("Hiệu suất Học tập/Làm việc", ["1", "2", "3"])
    giai_tri = st.radio("Khả năng Giải trí", ["1", "2", "3"])

    if st.button("Đánh giá Cơ bản"):
        basic_score, BMI, CICO = basic_health_assessment(
            sleep_hours, weight, height_in_meters, calories_in, calories_out,
            meal_per_day, huyet_ap, duong_huyet, mo_mau,
            tinh_trang_dinh_duong, suc_khoe_co_bap, hieu_suat, giai_tri
        )
        st.success(f"Điểm sức khỏe cơ bản (thang 10): {round(basic_score/5,2)}")
        st.write(f"- **BMI:** {round(BMI,2)}")
        st.write(f"- **Cân bằng năng lượng (CICO):** {CICO} kcal")

# TAB 2: ĐÁNH GIÁ NÂNG CAO
with tab2:
    st.header("🔍 Đánh giá sức khỏe nâng cao")
    adv_score = advanced_health_assessment()

    if st.button("Đánh giá Nâng cao"):
        st.success(f"Điểm nâng cao (thang 10): {round(adv_score,2)}")
