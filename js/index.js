function edit(id) {
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.onreadystatechange = function() {
        if(this.readyState == XMLHttpRequest.DONE){
            var response = JSON.parse(this.responseText);
            var title = response.data.type ? `Ano` : `Título`;

            var edit = document.getElementById("edit");
            edit.classList.add("row");
            edit.innerHTML = '';

            edit.innerHTML = `<div class="column orange lighten-4" style="padding: 20px 10px;">
                                <div class="form-group">
                                    <label for="id"><h5><strong>Autor:</strong></h5></label>` + response.data.assigned + `
                                </div>
                            </div>
                            <div class="column orange lighten-4" style="padding: 20px 10px;">
                                <div class="form-group">
                                    <label for="id"><h5><strong>Cadeira:</strong></h5></label>` + response.data.course + `
                                </div>
                            </div>
                            <div class="column orange lighten-4" style="padding: 20px 10px;">
                                <div class="form-group">
                                    <label for="id"><h5><strong>` + title + `:</strong></h5></label>` + response.data.title + `
                                </div>
                            </div>
                            <div class="column orange lighten-4" style="padding: 20px 10px;">
                                <div class="form-group">
                                    <label for="id"><h5><strong>Preço:</strong></h5></label>R$ ` + response.data.price + `
                                </div>
                            </div>`;
        }
    }

    var url = "http://10.1.1.105:4000/xerox/edit/" + id;
    xmlHttp.open("GET", url);
    xmlHttp.setRequestHeader("Content-Type", "application/json");
    xmlHttp.send();
}

function deleted(id) {
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.onreadystatechange = function() {
        if(this.readyState == XMLHttpRequest.DONE){
            var response = JSON.parse(this.responseText);
            alert(response.message)
            setTimeout(function() {
              location.reload();
            }, 720);
        }
    }

    var url = "http://10.1.1.105:4000/xerox/delete/" + id;
    xmlHttp.open("DELETE", url);
    xmlHttp.setRequestHeader("Content-Type", "application/json");
    xmlHttp.send();
}

function create(id) {
//    var course = "Redes 1";
//    var author = "Edison";
//    var title = "2019.2";
//    var price = "451.6";
//    var type = 1;
//
//    data = {
//        type: type,
//        assigned: author,
//        course: course,
//        title: title,
//        price: price
//    };

    var course = "";
    var author = "";
    var title = "";
    var price = 0;
    var type = 0;
    var object = [];

    if(id == "#bookbtn"){
        type = 0;
        course = $("#disciplineBook").val();
        author = $("#author").val();
        title = $("#book").val();
        price = $("#priceBook").val();
    }else if(id == "#scholarExerciseBtn"){
        type = 1;
        course = $("#disciplineScholarExercise").val();
        author = $("#professor").val();
        title = $("#period").val();
        price = $("#priceScholarExercise").val();
    }

    data = {
        type: type,
        assigned: author,
        course: course,
        title: title,
        price: price
    };

    var xmlHttp = new XMLHttpRequest();

    xmlHttp.onreadystatechange = function() {
        if(this.readyState == XMLHttpRequest.DONE){
            var response = JSON.parse(this.responseText);
            alert(response.message)
            setTimeout(function() {
              location.reload();
            }, 720);
        }
    }
    var url = "http://10.1.1.105:4000/xerox/create";
    xmlHttp.open("POST", url);
    xmlHttp.setRequestHeader("Content-Type", "application/json");
    xmlHttp.send(JSON.stringify(data));
}


function update(id) {
    var course = "Redes 1";
    var author = "Edison";
    var title = "2019.2";
    var price = "451.6";
    var type = 1;

    data = {
        type: type,
        assigned: author,
        course: course,
        title: title,
        price: price
    };

    var xmlHttp = new XMLHttpRequest();

    xmlHttp.onreadystatechange = function() {
        if(this.readyState == XMLHttpRequest.DONE){
            var response = JSON.parse(this.responseText);
            alert(response.message)
            setTimeout(function() {
              location.reload();
            }, 720);
        }
    }
    var url = "http://10.1.1.105:4000/xerox/update/" + id;
    xmlHttp.open("PUT", url);
    xmlHttp.setRequestHeader("Content-Type", "application/json");
    xmlHttp.send(JSON.stringify(data));
    xmlHttp.send(JSON.stringify(data));
}


function showForm(){
    hideElement("#examesAndBooks");
    hideElement("#exames-table");
    hideElement("#books-table");
    showElement("#selectType");
    showElement("#formBook");

    $('input[type="radio"]').on('change', function(e) {
        var type = $('input[name=chooseType]:checked').val();
        changeForm(type);
    });
}

function changeForm(type){
    if(type == 1){
        $("#formBook").prop("hidden",false);
        $("#formExame").prop("hidden",true);
    }else if(type == 2){
        $("#formExame").prop("hidden",false);
        $("#formBook").prop("hidden",true);
    }
}

function hideElement(id){
    $(id).prop("hidden", true);
}

function showElement(id){
    $(id).prop("hidden", false);
}