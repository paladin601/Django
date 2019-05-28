function del(self) {
    let hola = $(".btn-delete")
    hola[0].id = self.id;
}

function edit(event){
    location.href="/update/"+event.id;
}