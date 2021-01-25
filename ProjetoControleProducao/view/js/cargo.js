$(document).ready(function(){
    
    $(function(){
        carregar();
    })

    $("#pesquisar").click(function(){
        alert("Pesquisa em manutenção!");
        $("#nome").val("");
    });

    function carregar(){
        var url = "http://localhost:5000/listarCargos";
        $.get(url,function(data,status){
            if (data.length === 0){
                $("#listaCargos").html("<tr><td colspan=1>Nenhum Cargo encontrado!</td></tr>");
            } else{
                var table = "";
                for(x in data){
                    table += "<tr class='linha'><td>" + data[x].id + "</td><td>" + data[x].nome + "</td></tr>";
                }
                $("#listaCargos").html(table);
                /* 
                var tabela = document.getElementById("listaCargos");
                var linhas = tabela.getElementsByTagName("tr");
                for(var i = 0; i < linhas.length; i++){
                    linhas[i].addEventListener("click", function(){
                        var dados = this.getElementsByTagName("td");
                        $("#idCargo").val(dados[0].innerHTML);
                        $("#nomeCargo").val(dados[1].innerHTML);
                        $("#cargoModal").click();
                    });
                }
                */
            }
        });
    };

    $(document).on("click", "#salvar", function() {
        nome = $("#nomeCargo").val();
        if(nome === ""){
            alert("Campo vazio!");
        } else{
            var dados = JSON.stringify({ nome: nome}); 
            $.ajax({ 
                url: "http://localhost:5000/incluirCargo", 
                type: "POST", 
                dataType: "json",
                contentType: "application/json",
                data: dados, 
                success: sucesso,
                error: erroAoIncluir 
            });

            function sucesso (retorno) {
                if (retorno.resultado == "ok") { 
                    alert("Sucesso!");
                    $("#nomeCargo").val("");
                } else {
                    alert(retorno.resultado + ":" + retorno.detalhes);
                    $("#nomeCargo").val("");
                }            
            }

            function erroAoIncluir (retorno) {
                alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
                $("#nomeCargo").val("");
            }
        }
    });
});