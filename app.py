import streamlit as st

# 1. CẤU HÌNH TRANG
st.set_page_config(
    page_title="Game Ga",
    page_icon="🐔"
)

st.title("🐔 Trò Chơi: Gà Qua Đường")

# 2. KHỞI TẠO ĐIỂM VÀ MÀN CHƠI
if "man" not in st.session_state:
    st.session_state.man = 1

if "thang" not in st.session_state:
    st.session_state.thang = False

man_hien_tai = st.session_state.man

# 3. CHU KỲ PHONG CẢNH NGÀY ĐÊM
chu_ky = man_hien_tai % 5

if chu_ky == 1:
    thoi_gian = "Buổi Trưa (Trời xanh gắt ☀️)"
elif chu_ky == 2:
    thoi_gian = "Hoàng Hôn (Trời cam đỏ 🌇)"
elif chu_ky == 3:
    thoi_gian = "Ban Đêm (Trời tối sẫm có Mặt Trăng 🌙)"
elif chu_ky == 4:
    thoi_gian = "Bình Minh (Trời hồng nắng sớm 🌅)"
else:
    thoi_gian = "Buổi Sáng (Trời xanh trong lành ☁️)"

# 4. KHUNG CẢNH VẬT THAY ĐỔI THEO MÀN
if man_hien_tai % 2 == 0:
    canh_vat = "Bờ cỏ có nhiều Cây Cối xanh rì 🌳"
else:
    canh_vat = "Vỉa hè có Cột Đèn Giao Thông nhấp nháy 🚦"

# 5. HIỂN THỊ GIAO DIỆN MÀN CHƠI
st.subheader(f"Màn chơi hiện tại: {man_hien_tai} / 100")
st.write(f"🏞️ Khung cảnh: {canh_vat}")
st.write(f"⏰ Thời gian: {thoi_gian}")

# 6. HIỂN THỊ ĐỒ HỌA GÀ VÀ XE (DẠNG EMOJI SIÊU ĐẸP)
st.write("---")
st.write("🏁 **ĐÍCH ĐẾN AN TOÀN** (Vạch kẻ đường màu trắng: `| | | |`) ")
st.write("=================================")

# Giả lập xe chạy nhanh dần theo màn chơi
toc_do = 1 + (man_hien_tai * 0.2)
st.write(f"🚘 Làn xe 1 (Tốc độ {toc_do:.1f}): 🚗 . . . 🚑 . . .")
st.write("---------------------------------")
st.write(f"🚘 Làn xe 2 (Tốc độ {toc_do:.1f}): . . 🛺 . . . 🚜 .")
st.write("---------------------------------")
st.write(f"🚘 Làn xe 3 (Tốc độ {toc_do:.1f}): . 🚌 . . . 🏎️ . .")

st.write("=================================")
st.write("🐔 **CHÚ GÀ CỦA BẠN** (Mào đỏ, lông đuôi vểnh)")
st.write("---")

# 7. ĐIỀU KHIỂN BẤM PHÁT MỘT ĐỂ QUA MÀN
if st.session_state.thang:
    st.balloons()
    st.success(f"🎉 QUA MÀN THÀNH CÔNG! Bạn đã vượt qua Màn {man_hien_tai}!")
    
    if st.button("Bước sang màn tiếp theo ➡️"):
        st.session_state.man += 1
        st.session_state.thang = False
        st.rerun()
else:
    st.info("🔊 *Cục tác! Cục tác!* Hãy nhấn nút bên dưới để nhảy tiến lên!")
    
    if st.button("▲ NHẢY TIẾN LÊN (BẤM PHÁT MỘT)"):
        # Giả lập tiếng gà kêu qua st.audio hoặc text
        st.toast("🐔 Cục tác! Gà vừa nhảy lên một bước!")
        st.session_state.thang = True
        st.rerun()

    if st.button("▼ NHẢY LÙI LẠI"):
        st.session_state.thang = False

