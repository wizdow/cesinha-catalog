function edit(id) {
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.onreadystatechange = function() {
        if(this.readyState == XMLHttpRequest.DONE){
            var response = JSON.parse(this.responseText);
            var title = response.data.type ? `Ano` : `Título`;

            var edit = document.getElementById("edit");
            var close = document.createElement("a");
            var update = document.createElement("a");

            close.innerHTML = `<div class="col" style="float: right; position: relative" onclick="closeElement('edit');">
                                <a href="#" data-target="slide-out" class="btn-sidenav btn-floating btn-small  red darken-3">
                                  <i class="material-icons">close</i>
                                </a>
                              </div>`;
            update.innerHTML = `<div class="col" style="float: right; position: relative" onclick="update(`+id+`,`+ response.data.type + `)">
                                <a href="#" data-target="slide-out" class="btn-sidenav btn-floating btn-small orange darken-3">
                                  <i class="material-icons">done</i>
                                </a>
                              </div>`;

            edit.classList.add("row");
            edit.innerHTML = '';

            edit.innerHTML = `<div class="column orange lighten-4" style="padding: 20px 10px;">
                                <div class="form-group">
                                    <label for="id"><h5><strong>Autor:</strong></h5></label>
                                    <input value="` + response.data.assigned + `" id="assigned-input">
                                </div>
                            </div>
                            <div class="column orange lighten-4" style="padding: 20px 10px;">
                                <div class="form-group">
                                    <label for="id"><h5><strong>Cadeira:</strong></h5></label>
                                    <input value="` + response.data.course + `" id="course-input">
                                </div>
                            </div>
                            <div class="column orange lighten-4" style="padding: 20px 10px;">
                                <div class="form-group">
                                    <label for="id"><h5><strong>` + title + `:</strong></h5></label>
                                    <input value="` + response.data.title + `" id="title-input">
                                </div>
                            </div>
                            <div class="column orange lighten-4" style="padding: 20px 10px;">
                                <div class="form-group">
                                    <label for="id"><h5><strong>Preço (R$):</strong></h5></label>
                                    <input value="` + response.data.price + `" id="price-input">
                                </div>
                            </div>`;


            edit.appendChild(close)
            edit.appendChild(update)
        }
    }

    var url = location.origin + "/xerox/edit/" + id;
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
            }, 600);
        }
    }

    var url = location.origin + "/xerox/delete/" + id;
    xmlHttp.open("DELETE", url);
    xmlHttp.setRequestHeader("Content-Type", "application/json");
    xmlHttp.send();
}

function create(id) {
    var data;

    if(id == "#bookbtn"){
        data = {
            type: 0,
            assigned: $("#author").val(),
            course: $("#disciplineBook").val(),
            title: $("#book").val(),
            price: $("#priceBook").val()
        };
    }else if(id == "#scholarExerciseBtn"){
        data = {
            type: 1,
            assigned: $("#professor").val(),
            course: $("#disciplineScholarExercise").val(),
            title: $("#period").val(),
            price: $("#priceScholarExercise").val()
        };
    }

    var xmlHttp = new XMLHttpRequest();

    xmlHttp.onreadystatechange = function() {
        if(this.readyState == XMLHttpRequest.DONE){
            var response = JSON.parse(this.responseText);
            alert(response.message)
            setTimeout(function() {
              location.reload();
            }, 600);
        }
    }
    var url = location.origin + "/xerox/create";
    xmlHttp.open("POST", url);
    xmlHttp.setRequestHeader("Content-Type", "application/json");
    xmlHttp.send(JSON.stringify(data));
}


function update(id, type) {
   var data = {
        type: type,
        assigned: $("#assigned-input").val(),
        course: $("#course-input").val(),
        title: $("#title-input").val(),
        price: $("#price-input").val()
    };

    var xmlHttp = new XMLHttpRequest();

    xmlHttp.onreadystatechange = function() {
        if(this.readyState == XMLHttpRequest.DONE){
            var response = JSON.parse(this.responseText);
            alert(response.message)
            setTimeout(function() {
              location.reload();
            }, 600);
        }
    }
    var url = location.origin + "/xerox/update/" + id;
    xmlHttp.open("PUT", url);
    xmlHttp.setRequestHeader("Content-Type", "application/json");
    xmlHttp.send(JSON.stringify(data));
    xmlHttp.send(JSON.stringify(data));
}


function showForm(){
    fadeOutElement("#examesAndBooks");
    fadeOutElement("#exames-table");
    fadeOutElement("#books-table");
    fadeOutElement("#edit");

    fadeInElement("#selectType");
    fadeInElement("#formBook");

    $('input[type="radio"]').on('change', function(e) {
        var type = $('input[name=chooseType]:checked').val();
        changeForm(type);
    });
}

function showStart(){
    fadeInElement("#examesAndBooks");
    fadeInElement("#exames-table");
    fadeInElement("#books-table");
    fadeInElement("#edit");

    fadeOutElement("#selectType");
    fadeOutElement("#formBook");
}

function changeForm(type){
    if(type == 1){
        fadeInElement("#formBook");
        fadeOutElement("#formExame");
    }else if(type == 2){
        fadeInElement("#formExame");
        fadeOutElement("#formBook");
    }
}

function fadeOutElement(id){
    $(id).fadeOut(500);
}

function fadeInElement(id){
    $(id).fadeIn(500);
}

function closeElement(id){
    var element = document.getElementById(id);
    element.innerHTML = ''
}