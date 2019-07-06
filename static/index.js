function copy_password() {
    var pw = document.getElementById("password")
    pw.select();
    document.execCommand("copy")
}

function copy_mail() {
    var pw = document.getElementById("fakemail")
    pw.select();
    document.execCommand("copy")
}
