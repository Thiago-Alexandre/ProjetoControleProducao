$(document).ready(function(){
    
    $(function(){
        carregar();
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

    function carregar(){
        var url = "http://localhost:5000/listarTiposProcesso";
        $.get(url,function(data,status){
            if (data.length === 0){
                $("#listaTiposProcesso").html("<tr><td colspan=2>Nenhum Tipo de Processo encontrado!</td></tr>");
            } else{
                var table = "";
                for(x in data){
                    table += "<tr><td>" + data[x].nome + "</td><td>" + data[x].descricao + "</td></tr>";
                }
                $("#listaTiposProcesso").html(table);

                var tabela = document.getElementById("listaTiposProcesso");
                var linhas = tabela.getElementsByTagName("tr");
                for(var i = 0; i < linhas.length; i++){
                    linhas[i].addEventListener("click", function(){
                        var dados = this.getElementsByTagName("td");
                        $("#nome").val(dados[0].innerHTML);
                        $("#descricao").val(dados[1].innerHTML);
                    });
                }
            }
        });
    };
});