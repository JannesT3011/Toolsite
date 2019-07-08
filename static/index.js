function copy_password() {
    var pw = document.getElementById("password");
    pw.select();
    document.execCommand("copy")
}

function copy_mail() {
    var mail = document.getElementById("fakemail");
    mail.select();
    document.execCommand("copy")
}