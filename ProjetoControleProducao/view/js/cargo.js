$(document).ready(function(){
    $(function(){
        $("#listaCargos").html("<tr><td colspan=1>Nenhum Cargo encontrado!</td></tr>");
    })

    $("#cancelar").click(function(){
        limpar();
    });

    $("#salvar").click(function(){
    	if($("#nome").val() === ""){
            alert("Campo vazio!");
            $("#nome").focus();
        }
    });

    function limpar(){
        $("#nome").val("");
        $("#nome").focus();
    }
});