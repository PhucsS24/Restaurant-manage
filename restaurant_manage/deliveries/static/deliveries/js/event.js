//đi đến vị trí book trang event
function bookformevent() {
    // Lấy ra phần tử form-event
    var formElement = document.getElementById("form-book-events");
    // Cuộn trang đến vị trí của form với hiệu ứng mượt (smooth)
    formElement.scrollIntoView({ behavior: 'smooth' });
}