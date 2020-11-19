$(document).ready(function(){
    
    $(function(){
        carregar();
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

    function carregar(){
        var url = "http://localhost:5000/listarCargos";
        $.get(url,function(data,status){
            if (data.length === 0){
                $("#listaCargos").html("<tr><td colspan=1>Nenhum Cargo encontrado!</td></tr>");
            } else{
                var table = "";
                for(x in data){
                    table += "<tr class='linha'><td>" + data[x].nome + "</td></tr>";
                }
                $("#listaCargos").html(table);

                var tabela = document.getElementById("listaCargos");
                var linhas = tabela.getElementsByTagName("tr");
                for(var i = 0; i < linhas.length; i++){
                    linhas[i].addEventListener("click", function(){
                        var dados = this.getElementsByTagName("td");
                        $("#nome").val(dados[0].innerHTML);
                    });
                }
            }
        });
    };
});