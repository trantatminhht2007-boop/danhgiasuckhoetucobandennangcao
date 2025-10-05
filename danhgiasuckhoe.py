def basic_health_assessment():
    sleep_hours = float(input("Số giờ ngủ: "))
    weight = float(input("Cân nặng (kg): "))
    height_in_meters = float(input("Chiều cao (m): "))
    calories_in = float(input("Calories nạp trong 1 ngày: "))
    calories_out = float(input("Calories tiêu thụ trong 1 ngày: "))
    meal_per_day = float(input("Số bữa ăn trong ngày: "))
    huyet_ap = input("Huyết áp (Tâm thu/Tâm trương, ví dụ: 120/80): ")
    duong_huyet = float(input("Đường huyết (mg/dL): "))
    mo_mau = input("Tình trạng mỡ máu (Lý tưởng/Biên giới/Rủi ro cao): ")
    tinh_trang_dinh_duong = input("Tình trạng Dinh dưỡng (1:Bình thường, 2:Thừa cân, 3:Béo phì, 4:Thiếu cân): ")
    suc_khoe_co_bap = input("Sức khỏe Cơ bắp (1:Xuất sắc, 2:Tốt, 3:Cần cải thiện): ")
    hieu_suat = input("Hiệu suất Học tập/Làm việc (1:Tốt, 2:Bình thường, 3:Kém): ")
    giai_tri = input("Khả năng Giải trí (1:Tốt, 2:Bình thường, 3:Kém): ")

    scores = 0

    # Giấc ngủ
    if 7 <= sleep_hours <= 9:
        scores += 7
    elif 6 <= sleep_hours < 7 or 9 < sleep_hours <= 10:
        scores += 4
    elif 5 <= sleep_hours < 6 or 10 < sleep_hours <= 11:
        scores += 2
    elif 4 <= sleep_hours < 5:
        scores += 1

    # BMI
    BMI = weight / height_in_meters ** 2
    if BMI < 18.5:
        scores += 3
    elif 18.5 <= BMI <= 24.9:
        scores += 6
    elif 25 <= BMI <= 29.9:
        scores += 1

    # CICO
    CICO = calories_in - calories_out
    if -100 <= CICO <= 100:
        scores += 7
    elif -300 <= CICO < -100 or 100 < CICO <= 300:
        scores += 5
    elif -500 <= CICO < -300 or 300 < CICO <= 500:
        scores += 3

    # Số bữa ăn
    if 3 <= meal_per_day <= 5:
        scores += 2
    elif meal_per_day <= 1:
        scores += 0

    # Huyết áp
    try:
        tam_thu, tam_truong = map(int, huyet_ap.split("/"))
        if tam_thu < 120 and tam_truong < 80:
            scores += 7
        elif 120 <= tam_thu < 130 and tam_truong < 80:
            scores += 5
        elif 130 <= tam_thu <= 139 or 80 <= tam_truong <= 89:
            scores += 3
        elif tam_thu >= 140 or tam_truong >= 90:
            scores += 0
    except:
        print("Định dạng huyết áp không hợp lệ.")

    # Đường huyết
    if 70 <= duong_huyet < 100:
        scores += 5
    elif 100 <= duong_huyet <= 125:
        scores += 2
    else:
        scores += 0

    # Mỡ máu
    if mo_mau.lower() == "lý tưởng":
        scores += 4
    elif mo_mau.lower() == "biên giới":
        scores += 2
    else:
        scores += 0

    # Sức khỏe cơ bắp
    if suc_khoe_co_bap == "1":
        scores += 3
    elif suc_khoe_co_bap == "2":
        scores += 2
    else:
        scores += 0

    # Hiệu suất học tập/làm việc
    if hieu_suat == "1":
        scores += 6
    elif hieu_suat == "2":
        scores += 4
    else:
        scores += 2

    # Giải trí
    if giai_tri == "1":
        scores += 4
    elif giai_tri == "2":
        scores += 2
    basic_health_score = scores
    return basic_health_score
print ("bạn có muốn đánh giá thêm sức khỏe nâng cao không ? (y/n): ")
    if n
        print(f"Điểm sức khỏe tổng thể: {scores}")
        if scores >= 40:
            print("🌟 Sức khỏe rất tốt!")
        elif 30 <= scores < 40:
            print("👍 Sức khỏe tốt.")
        elif 20 <= scores < 30:
            print("😐 Sức khỏe trung bình.")
        elif 10 <= scores < 20:
            print("⚠️ Sức khỏe kém.")
        else:
            print("🚨 Bạn nên đi khám bác sĩ ngay!")
    if y
        def advanced_health_assessment():
            age = int(input("Tuổi: "))
            gender = input("Điền giới tính của bạn (Nam/nữ): ").lower()
            return age, gender

        def health_criteria(age, gender):
            if gender == "nam":
                if 18 <= age < 30:
                    return ['Tiêm chủng', 'Hoạt động thể chất', 'Ăn uống lành mạnh', 'Mức độ hút thuốc', 'Sức khỏe tâm thần']
                elif 30 <= age < 50:
                    return ['Tốc độ chuyển hóa', 'Quản lý căng thẳng', 'Hoạt động thể chất']
                elif 50 <= age < 69:
                    return ['Tầm soát ung thư: Nội soi đại tràng', 'Tầm soát ung thư tiền liệt tuyến', 'Tầm soát nguy cơ tim mạch và phình động mạch chủ bụng']
                elif age >= 70:
                    return ['Thính giác', 'Thị lực', 'Mật độ xương', 'Sức khỏe tâm thần: trí nhớ, trầm cảm', 'Hành vi lành mạnh']
            elif gender == "nữ":
                if 18 <= age < 30:
                    return ['Khám phụ khoa định kỳ', 'Xét nghiệm Pap smear', 'Biện pháp tránh thai an toàn', 'Kiểm tra huyết áp', 'Quản lý stress', 'Tự kiểm tra vú hàng tháng']
                elif 30 <= age < 45:
                    return ['Tầm soát ung thư cổ tử cung (Pap + HPV)', 'Tầm soát ung thư vú', 'Bổ sung Axit Folic nếu có kế hoạch mang thai']
                elif 45 <= age < 60:
                    return ['Chụp nhũ ảnh (Mammogram)', 'Tầm soát ung thư đại tràng', 'Bổ sung Canxi và Vitamin D', 'Tập thể dục chịu trọng lượng']
                elif age >= 60:
                    return ['Kiểm tra mật độ xương (DEXA scan)', 'Tầm soát thị lực', 'Thăng bằng', 'Tầm soát suy giảm nhận thức', 'Tầm soát trầm cảm', 'Tầm soát ung thư vú và đại tràng']
            else:
                return []

        def input_health_scores(criteria_list):
            total_score = 0
            for criterion in criteria_list:
                score = float(input(f"Đánh giá tiêu chí '{criterion}' từ 1 đến 10: "))
                total_score += score
            average_score = total_score / len(criteria_list)
            advanced_health_score = average_score * 50
            total_advanced_health_score = basic_health_score + advanced_health_score     
            return total_advanced_health_score
            print(f"Điểm sức khỏe tổng thể: {scores}")
            if scores >= 80:
                print("🌟 Sức khỏe rất tốt!")
            elif 60 <= scores < 80:
                print("👍 Sức khỏe tốt.")
            elif 40 <= scores < 60:
                print("😐 Sức khỏe trung bình.")
            elif 20 <= scores < 60:
                print("⚠️ Sức khỏe kém.")
            else:
                print("🚨 Bạn nên đi khám bác sĩ ngay!")

            
