$(document).ready(function(){
    
    $(function(){
        carregar();
    })

    $("#pesquisar").click(function(){
        id_cargo = $("#pesquisa").val();
        $("#pesquisa").val("");
        if (id_cargo === ""){
            carregar();
        } else{
            mostrar(id_cargo);     
        }
    });

    function carregar(){
        var url = "http://localhost:5000/cargos";
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

    function mostrar(id_cargo){
        var url = "http://localhost:5000/cargos/" + id_cargo;
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
        
        if(nomeCargo === ""){
            alert("Nome vazio!");
        } else{
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
                success: sucessoSalvarCargo,
                error: erroAoIncluir 
            });

            function sucessoSalvarCargo (retorno) {
                if (retorno.resultado == "ok") {
                    alert("Cargo salvo com sucesso!");
                    $('#cargoModal').modal('hide');
                    carregar();
                } else {
                    alert(retorno.resultado + ":" + retorno.detalhes);
                }
                $("#nomeCargo").val("");
                $("#idCargo").val("");
            }

            function erroAoIncluir (retorno) {
                alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
                $("#nomeCargo").val("");
                $("#idCargo").val("");
            }
        }
    });

    $(document).on("click", ".excluir_cargo", function() { 
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_"; 
        var id_cargo = componente_clicado.substring(nome_icone.length); 
        $.ajax({ 
            url: "http://localhost:5000/cargos/" + id_cargo, 
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