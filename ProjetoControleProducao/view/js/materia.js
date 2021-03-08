$(document).ready(function(){
    
    $(function(){
        carregar("http://localhost:5000/materias");
    });

    $("#pesquisar").click(function(){
        id_materia = $("#pesquisa").val();
        $("#pesquisa").val("");
        if (id_materia === ""){
            carregar("http://localhost:5000/materias");
        } else{
            carregar("http://localhost:5000/materias/" + id_materia);     
        }
    });

    function carregar(url){
        $.get(url,function(data,status){
            if (data.length === 0){
                $("#listaMaterias").html("<tr><td colspan=1>Nenhuma Matéria-Prima encontrada!</td></tr>");
            } else{
                var table = "";
                for(x in data){
                    table += "<tr class='linha'>" +
                                "<td>" + data[x].nome + "</td>" +
                                "<td>" + data[x].fornecedor + "</td>" +
                                "<td>" + data[x].quantidadeEstoque + "</td>" +
                                "<td>" + 
                                    "<a href=# id='editar_" + data[x].id + "' class='editar_materia'>" + 
                                        "<img src='img/editar.ico' alt='Editar Matéria-Prima' title='Editar Matéria-Prima' height='30' width='30'>" +
                                    "</a>" +
                                    "<a href=# id='excluir_" + data[x].id + "' class='excluir_materia'>" + 
                                        "<img src='img/excluir.ico' alt='Excluir Matéria-Prima' title='Excluir Matéria-Prima' height='30' width='30'>" +
                                    "</a>" +
                                    "<a href=# id='adicionar_" + data[x].id + "' class='adicionar_estoque'>" + 
                                        "<img src='img/adicionar.ico' alt='Adicionar Estoque' title='Adicionar Estoque' height='30' width='30'>" +
                                    "</a>" +
                                "</td>" +
                            "</tr>";
                }
                $("#listaMaterias").html(table);
            }
        });
    };

    $(document).on("click", "#salvarMateria", function() {
        idMateria = $("#idMateria").val();
        nomeMateria = $("#nomeMateria").val();
        descricaoMateria = $("#descricaoMateria").val();
        valorMateria = $("#valorMateria").val();
        fornecedorMateria = $("#fornecedorMateria").val();
        metodo = "PUT";
        endpoint = "http://localhost:5000/materias/" + idMateria;
        if (idMateria === ""){
            metodo = "POST";
            endpoint = "http://localhost:5000/materias";
        }
        var dados = JSON.stringify({nome: nomeMateria, descricao: descricaoMateria, valorUnitario: valorMateria, fornecedor: fornecedorMateria}); 
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
                alert("Matéria-Prima salva com sucesso!");
                fecharModalMateria();
                carregar("http://localhost:5000/materias");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoIncluir (retorno) {
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });

    $(document).on("click", "#cancelarMateria", function() {
        fecharModalMateria();
    });

    $(document).on("click", "#fecharModalMateria", function() {
        fecharModalMateria();
    });

    function fecharModalMateria(){
        $("#idMateria").val("");
        $("#nomeMateria").val("");
        $("#descricaoMateria").val("");
        $("#estoqueMateria").val("");
        $("#valorMateria").val("");
        $("#fornecedorMateria").val("");
        $('#materiaModal').modal('hide');
    };

    $(document).on("click", "#salvarEstoque", function() {
        idMateria = $("#idEstoque").val();
        quantidadeAdicionada = $("#quantidadeAdicionada").val();
        var dados = JSON.stringify({quantidade: quantidadeAdicionada}); 
        $.ajax({ 
            url: "http://localhost:5000/materiais/" + idMateria, 
            type: "POST", 
            dataType: "json",
            contentType: "application/json",
            data: dados, 
            success: sucessoAtualizarEstoque,
            error: erroAoAtualizar 
        });

        function sucessoAtualizarEstoque (retorno) {
            if (retorno.resultado == "ok") {
                alert("EstoqueAtualizado!");
                fecharModalEstoque();
                carregar("http://localhost:5000/materias");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoAtualizar (retorno) {
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });

    $(document).on("click", "#cancelarEstoque", function() {
        fecharModalEstoque();
    });

    $(document).on("click", "#fecharModalEstoque", function() {
        fecharModalEstoque();
    });

    function fecharModalEstoque(){
        $("#idEstoque").val("");
        $("#nomeEstoque").val("");
        $("#estoqueAtual").val("");
        $("#fornecedorEstoque").val("");
        $("#quantidadeAdicionada").val("");
        $('#addEstoqueModal').modal('hide');
    };

    $(document).on("click", ".excluir_materia", function() { 
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_"; 
        var id_materia = componente_clicado.substring(nome_icone.length); 
        $.ajax({ 
            url: "http://localhost:5000/materias/" + id_materia, 
            type: "DELETE",
            dataType: "json",
            success: sucessoExcluir, 
            error: erroAoExcluir 
        });

        function sucessoExcluir (retorno) {
            if (retorno.resultado == "ok") { 
                alert("Matéria-Prima removida com sucesso!");
                carregar("http://localhost:5000/materias");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoExcluir (retorno) { 
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes); 
        }
    });

    $(document).on("click", ".editar_materia", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "editar_";
        var id_materia = componente_clicado.substring(nome_icone.length);
        var url = "http://localhost:5000/materias/" + id_materia;
        $.get(url,function(data,status){
            if (data.length === 0){
                alert("Nenhuma Matéria-Prima encontrada!")
            } else{
                $("#idMateria").val(data[0].id);
                $("#nomeMateria").val(data[0].nome);
                $("#descricaoMateria").val(data[0].descricao);
                $("#estoqueMateria").val(data[0].quantidadeEstoque);
                $("#valorMateria").val(data[0].valorUnitario);
                $("#fornecedorMateria").val(data[0].fornecedor);
                $('#materiaModal').modal('show');
            }
        });
    });

    $(document).on("click", ".adicionar_estoque", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "adicionar_";
        var id_materia = componente_clicado.substring(nome_icone.length);
        var url = "http://localhost:5000/materias/" + id_materia;
        $.get(url,function(data,status){
            if (data.length === 0){
                alert("Nenhuma Matéria-Prima encontrada!")
            } else{
                $("#idEstoque").val(data[0].id);
                $("#nomeEstoque").val(data[0].nome);
                $("#estoqueAtual").val(data[0].quantidadeEstoque);
                $("#fornecedorEstoque").val(data[0].fornecedor);
                $("#quantidadeAdicionada").focus();
                $('#addEstoqueModal').modal('show');
            }
        });
    });
});