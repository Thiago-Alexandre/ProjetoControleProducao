$(document).ready(function(){
    
    $(function(){
        carregar("http://localhost:5000/funcionarios");
    });

    $("#pesquisar").click(function(){
        id_funcionario = $("#pesquisa").val();
        $("#pesquisa").val("");
        if (id_funcionario === ""){
            carregar("http://localhost:5000/funcionarios");
        } else{
            carregar("http://localhost:5000/funcionarios/" + id_funcionario);     
        }
    });

    function carregar(url){
        $.get(url,function(data,status){
            if (data.length === 0){
                $("#listaFuncionarios").html("<tr><td colspan=1>Nenhum Funcionário encontrado!</td></tr>");
            } else{
                var table = "";
                for(x in data){
                    table += "<tr class='linha'>" +
                             "<td>" + data[x].nome + "</td>" +
                             "<td>" + data[x].cargo.nome + "</td>" +
                             "<td><a href=# id='editar_" + data[x].id + "' class='editar_funcionario'>" + 
                             "<img src='img/editar.ico' alt='Editar Funcionário' title='Editar Funcionário' height='30' width='30'></a>" +
                             "<a href=# id='excluir_" + data[x].id + "' class='excluir_funcionario'>" + 
                             "<img src='img/excluir.ico' alt='Excluir Funcionário' title='Excluir Funcionário' height='30' width='30'></a>" +
                             "</td></tr>";
                }
                $("#listaFuncionarios").html(table);
            }
        });
    };

    $(document).on("click", "#salvar", function() {
        idFuncionario = $("#idFuncionario").val();
        nomeFuncionario = $("#nomeFuncionario").val();
        cargoFuncionario = $("#cargoId").val();
        metodo = "PUT";
        endpoint = "http://localhost:5000/funcionarios/" + idFuncionario;
        if (idFuncionario === ""){
            metodo = "POST";
            endpoint = "http://localhost:5000/funcionarios";
        }
        var dados = JSON.stringify({nome: nomeFuncionario, cargo_id: cargoFuncionario}); 
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
                alert("Funcionário salvo com sucesso!");
                fecharModal();
                carregar("http://localhost:5000/funcionarios");
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
        $("#idFuncionario").val("");
        $("#nomeFuncionario").val("");
        $("#cargoID").val("");
        $('#funcionarioModal').modal('hide');
    };

    $(document).on("click", ".excluir_funcionario", function() { 
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_"; 
        var id_funcionario = componente_clicado.substring(nome_icone.length); 
        $.ajax({ 
            url: "http://localhost:5000/funcionarios/" + id_funcionario, 
            type: "DELETE",
            dataType: "json",
            success: sucessoExcluir, 
            error: erroAoExcluir 
        });

        function sucessoExcluir (retorno) {
            if (retorno.resultado == "ok") { 
                alert("Funcionário removido com sucesso!");
                carregar("http://localhost:5000/funcionarios");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoExcluir (retorno) { 
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes); 
        }
    });

    $("#funcionarioModal").on("shown.bs.modal", function (e) {
        if ($("#idFuncionario").val() === ""){
            carregarCargos(null);
        } else{
            $.get("http://localhost:5000/funcionarios/" + $("#idFuncionario").val(),function(data,status){
                var id = null;
                if (data.length === 0){
                    alert("Nenhum Funcionário encontrado!")
                } else{
                    id = data[0].cargo.id;
                }
                carregarCargos(id);
            });
        }
    });

    $(document).on("click", ".editar_funcionario", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "editar_";
        var id_funcionario = componente_clicado.substring(nome_icone.length);
        var url = "http://localhost:5000/funcionarios/" + id_funcionario;
        $.get(url,function(data,status){
            if (data.length === 0){
                alert("Nenhum Funcionário encontrado!")
            } else{
                $("#idFuncionario").val(data[0].id);
                $("#nomeFuncionario").val(data[0].nome);
                $('#funcionarioModal').modal('show'); 
            }
        });
    });

    function carregarCargos(id){
        $("#cargoId").empty();
        $.get("http://localhost:5000/cargos",function(cargos,status){
            for (var c in cargos) {
                $("#cargoId").append( 
                    $("<option></option>").attr("value", cargos[c].id).text(cargos[c].nome));
            }
            if (id !== null){
                $("#cargoId option[value='" + id + "']").attr("selected", true).change();
            }
        });
    };
});