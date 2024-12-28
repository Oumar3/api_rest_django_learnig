let nom = document.querySelector("#id_name");
let form = document.querySelector("#form");

form.addEventListener("submit",function(e){
    e.preventDefault();
    if(nom.value == ""){
        alert("Le nom est vide");
        return;
    }
})

nom.addEventListener("",function(){
    console.log(nom.value);
    
})