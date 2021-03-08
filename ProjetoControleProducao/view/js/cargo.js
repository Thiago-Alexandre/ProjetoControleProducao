$(document).ready(function(){
    
    $(function(){
        carregar("http://localhost:5000/cargos");
    });

    $("#pesquisar").click(function(){
        id_cargo = $("#pesquisa").val();
        $("#pesquisa").val("");
        if (id_cargo === ""){
            carregar("http://localhost:5000/cargos");
        } else{
            carregar("http://localhost:5000/cargos/" + id_cargo);     
        }
    });

    function carregar(url){
        $.get(url,function(data,status){
            if (data.length === 0){
                $("#listaCargos").html("<tr><td colspan=1>Nenhum Cargo encontrado!</td></tr>");
            } else{
                var table = "";
                for(x in data){
                    table += "<tr class='linha'>" +
                             "<td>" + data[x].nome + "</td>" + 
                             "<td><a href=# id='editar_" + data[x].id + "' class='editar_cargo'>" + 
                             "<img src='img/editar.ico' alt='Editar Cargo' title='Editar cargo' height='30' width='30'></a>" +
                             "<a href=# id='excluir_" + data[x].id + "' class='excluir_cargo'>" + 
                             "<img src='img/excluir.ico' alt='Excluir Cargo' title='Excluir cargo' height='30' width='30'></a>" +
                             "</td></tr>";
                }
                $("#listaCargos").html(table);
            }
        });
    };

    $(document).on("click", "#salvar", function() {
        idCargo = $("#idCargo").val();
        nomeCargo = $("#nomeCargo").val();
        metodo = "PUT";
        endpoint = "http://localhost:5000/cargos/" + idCargo;
        if (idCargo === ""){
            metodo = "POST";
            endpoint = "http://localhost:5000/cargos";
        }
        var dados = JSON.stringify({nome: nomeCargo}); 
        $.ajax({ 
            url: endpoint, 
            type: metodo, 
            dataType: "json",
            contentType: "application/json",
            data: dados, 
            success: sucessoSalvar,
            error: erroAoIncluir 
        });

        function sucessoSalvar (retorno) {
            if (retorno.resultado == "ok") {
                alert("Cargo salvo com sucesso!");
                fecharModal();
                carregar("http://localhost:5000/cargos");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoIncluir (retorno) {
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });

    $(document).on("click", "#cancelar", function() {
        fecharModal();
    });

    $(document).on("click", "#fechar", function() {
        fecharModal();
    });

    function fecharModal(){
        $("#idCargo").val("");
        $("#nomeCargo").val("");
        $('#cargoModal').modal('hide');
    };

    $(document).on("click", ".excluir_cargo", function() { 
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_"; 
        var id_cargo = componente_clicado.substring(nome_icone.length); 
        $.ajax({ 
            url: "http://localhost:5000/cargos/" + id_cargo, 
            type: "DELETE",
            dataType: "json",
            success: sucessoExcluir, 
            error: erroAoExcluir 
        });

        function sucessoExcluir (retorno) {
            if (retorno.resultado == "ok") { 
                alert("Cargo removido com sucesso!");
                carregar("http://localhost:5000/cargos");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoExcluir (retorno) { 
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes); 
        }
    });

    $(document).on("click", ".editar_cargo", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "editar_";
        var id_cargo = componente_clicado.substring(nome_icone.length);
        var url = "http://localhost:5000/cargos/" + id_cargo;
        $.get(url,function(data,status){
            if (data.length === 0){
                alert("Nenhum Cargo encontrado!")
            } else{
                $("#idCargo").val(data[0].id);
                $("#nomeCargo").val(data[0].nome);
                $('#cargoModal').modal('show'); 
            }
        });
    });
});