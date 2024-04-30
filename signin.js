function validateForm() {
    var email = document.getElementById('user_email').value;
    var password = document.getElementById('user_pw').value;
    if (email == "" || password == "") {
        alert('Both email and password are required to log in.');
        return false;
    }
    return true;
}