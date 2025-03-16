# process_image.py
import cv2
import mediapipe as mp
import sys
import json

# Khởi tạo Mediapipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)

def overlay_clothing(image_path, clothing_path):
    # Đọc ảnh người và ảnh quần áo
    image = cv2.imread(image_path)
    clothing = cv2.imread(clothing_path, cv2.IMREAD_UNCHANGED)

    # Chuyển ảnh sang RGB để xử lý với Mediapipe
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Nhận diện các điểm trên cơ thể người
    results = pose.process(image_rgb)

    # Nếu nhận diện được cơ thể người
    if results.pose_landmarks:
        # Lấy kích thước ảnh
        h, w, _ = image.shape

        # Ví dụ: Overlay quần áo lên vùng ngực
        # (Bạn cần thêm logic xử lý ảnh ở đây)
        # Giả sử quần áo có kích thước 200x200 và đặt ở vị trí (x, y) = (100, 100)
        x, y = 100, 100
        clothing_resized = cv2.resize(clothing, (200, 200))

        # Overlay quần áo lên ảnh người
        for i in range(clothing_resized.shape[0]):
            for j in range(clothing_resized.shape[1]):
                if clothing_resized[i, j, 3] != 0:  # Kiểm tra alpha channel
                    image[y + i, x + j] = clothing_resized[i, j, :3]

    # Lưu ảnh đã xử lý
    output_path = "processed_image.png"
    cv2.imwrite(output_path, image)
    return output_path

if __name__ == "__main__":
    # Đọc đường dẫn ảnh từ command line
    image_path = sys.argv[1]
    clothing_path = sys.argv[2]

    # Overlay quần áo lên ảnh người
    output_path = overlay_clothing(image_path, clothing_path)

    # Trả về đường dẫn ảnh đã xử lý dưới dạng JSON
    print(json.dumps({"processedImageUrl": output_path}))