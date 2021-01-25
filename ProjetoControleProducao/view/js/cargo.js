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
                    table += "<tr class='linha'>" +
                             "<td>" + data[x].nome + "</td>" + 
                             "<td><a href=# id='excluir_" + data[x].id + "' class='excluir_cargo'>" + 
                             "<img src='img/excluir.png' alt='Excluir Cargo' title='Excluir cargo'>" + 
                             "</a></td></tr>";
                }
                $("#listaCargos").html(table);
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
                success: sucessoSalvarCargo,
                error: erroAoIncluir 
            });

            function sucessoSalvarCargo (retorno) {
                if (retorno.resultado == "ok") {
                    $('#cargoModal').modal('hide'); 
                    alert("Cargo salvo com sucesso!");
                    $("#nomeCargo").val("");
                    carregar();
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

    $(document).on("click", ".excluir_cargo", function() { 
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_"; 
        var id_cargo = componente_clicado.substring(nome_icone.length); 
        $.ajax({ 
            url: "http://localhost:5000/excluirCargo/" + id_cargo, 
            type: "DELETE",
            dataType: "json",
            success: sucessoExcluirCargo, 
            error: erroAoExcluir 
        });

        function sucessoExcluirCargo (retorno) {
            if (retorno.resultado == "ok") { 
                alert("Cargo removido com sucesso!");
                carregar();
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoExcluir (retorno) { 
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes); 
        }
    });
});