// wwwroot/js/site.js
document.getElementById('uploadForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Ngăn form gửi đi theo cách thông thường

    const fileInput = document.getElementById('imageUpload');
    const file = fileInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        // Gọi API xử lý ảnh
        fetch('/Home/ProcessImage', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                // Hiển thị ảnh kết quả
                const processedImage = document.getElementById('processedImage');
                processedImage.src = data.processedImageUrl;
                processedImage.style.display = 'block';
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while processing the image.');
            });
    } else {
        alert('Please select an image to upload.');
    }
});