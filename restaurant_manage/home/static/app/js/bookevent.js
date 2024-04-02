
//đi đến vị trí book trang event
function bookformevent() {
    // Lấy ra phần tử form-event
    var formElement = document.getElementById("form-book-events");
    // Cuộn trang đến vị trí của form với hiệu ứng mượt (smooth)
    formElement.scrollIntoView({ behavior: 'smooth' });
}


//book in home - display form submit
function display_submit() {
    // Ẩn nút "Book Now"
    document.getElementById("booknowbtn").style.display = "none";
    // Hiển thị nút "Submit"
    document.getElementById("submitbtn").style.display = "block";
}

// chuyển hướng về btn book ở home
function bookformhome() {
    // Chuyển hướng (redirect) đến trang home.html và cuộn đến phần tử có id là "slider"
    
    var formElement = document.getElementById("reserver");
    window.location.href = "home1.html#slider";
}

// chuyển hướng về btn book ở event
function bookformevent() {
    // Chuyển hướng (redirect) đến trang home.html và cuộn đến phần tử có id là "slider"
    
    var formElement = document.getElementById("plan-event");
    window.location.href = "event.html#form-book-events";
}



