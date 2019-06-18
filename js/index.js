function edit(id) {
    var xmlHttp = new XMLHttpRequest();
    var url = "http://10.1.1.105:4000/xerox/edit/" + id;
    xmlHttp.open("GET", url);
    xmlHttp.send();
}

function deleted(id) {
    var xmlHttp = new XMLHttpRequest();
    var url = "http://10.1.1.105:4000/xerox/delete/" + id;
    xmlHttp.open("DELETE", url);
    xmlHttp.send();
}

function create() {
    var xmlHttp = new XMLHttpRequest();
    var url = "http://10.1.1.105:4000/xerox/created";
    xmlHttp.open("POST", url);
    xmlHttp.send();
}