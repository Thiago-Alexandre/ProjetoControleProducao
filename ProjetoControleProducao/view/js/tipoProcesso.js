$(document).ready(function(){
    $(function(){
        $("#listaTiposProcesso").html("<tr><td colspan=1>Nenhum Tipo de Processo encontrado!</td></tr>");
    })

    $("#cancelar").click(function(){
        limpar();
    });

    $("#salvar").click(function(){
    	if($("#nome").val() === "" || $("#descricao").val() === ""){
            alert("Campos vazios!");
            $("#nome").focus();
        }
    });

    function limpar(){
        $("#nome").val("");
        $("#descricao").val("");
        $("#nome").focus();
    }
});