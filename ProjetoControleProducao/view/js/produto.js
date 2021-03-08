$(document).ready(function(){
    
    $(function(){
        carregar("http://localhost:5000/produtos");
    });

    $("#pesquisar").click(function(){
        id_produto = $("#pesquisa").val();
        $("#pesquisa").val("");
        if (id_produto === ""){
            carregar("http://localhost:5000/produtos");
        } else{
            carregar("http://localhost:5000/produtos/" + id_produto);     
        }
    });

    function carregar(url){
        $.get(url,function(data,status){
            if (data.length === 0){
                $("#listaProdutos").html("<tr><td colspan=1>Nenhum Produto encontrado!</td></tr>");
            } else{
                var table = "";
                for(x in data){
                    table += "<tr class='linha'>" +
                                "<td>" + data[x].nome + "</td>" +
                                "<td>" + data[x].quantidadeEstoque + "</td>" +
                                "<td>" + data[x].valorVenda + "</td>" +
                                "<td>" + 
                                    "<a href=# id='editar_" + data[x].id + "' class='editar_produto'>" + 
                                        "<img src='img/editar.ico' alt='Editar Produto' title='Editar Produto' height='30' width='30'>" +
                                    "</a>" +
                                    "<a href=# id='excluir_" + data[x].id + "' class='excluir_produto'>" + 
                                        "<img src='img/excluir.ico' alt='Excluir Produto' title='Excluir Produto' height='30' width='30'>" +
                                    "</a>" +
                                "</td>" +
                            "</tr>";
                }
                $("#listaProdutos").html(table);
            }
        });
    };

    $(document).on("click", "#salvar", function() {
        idProduto = $("#idProduto").val();
        nomeProduto = $("#nomeProduto").val();
        descricaoProduto = $("#descricaoProduto").val();
        metodo = "PUT";
        endpoint = "http://localhost:5000/produtos/" + idProduto;
        if (idProduto === ""){
            metodo = "POST";
            endpoint = "http://localhost:5000/produtos";
        }
        var dados = JSON.stringify({nome: nomeProduto, descricao: descricaoProduto}); 
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
                alert("Produto salvo com sucesso!");
                fecharModal();
                carregar("http://localhost:5000/produtos");
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
        $("#idProduto").val("");
        $("#nomeProduto").val("");
        $("#descricaoProduto").val("");
        $("#quantidadeEstoque").val("");
        $("#valorProducao").val("");
        $("#valorVenda").val("");
        $('#produtoModal').modal('hide');
    };

    $(document).on("click", ".excluir_produto", function() { 
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_"; 
        var id_produto = componente_clicado.substring(nome_icone.length); 
        $.ajax({ 
            url: "http://localhost:5000/produtos/" + id_produto, 
            type: "DELETE",
            dataType: "json",
            success: sucessoExcluir, 
            error: erroAoExcluir 
        });

        function sucessoExcluir (retorno) {
            if (retorno.resultado == "ok") { 
                alert("Produto removido com sucesso!");
                carregar("http://localhost:5000/produtos");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoExcluir (retorno) { 
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes); 
        }
    });

    $(document).on("click", ".editar_produto", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "editar_";
        var id_produto = componente_clicado.substring(nome_icone.length);
        var url = "http://localhost:5000/produtos/" + id_produto;
        $.get(url,function(data,status){
            if (data.length === 0){
                alert("Nenhum Produto encontrado!")
            } else{
                $("#idProduto").val(data[0].id);
                $("#nomeProduto").val(data[0].nome);
                $("#descricaoProduto").val(data[0].descricao);
                $("#quantidadeEstoque").val(data[0].quantidadeEstoque);
                $("#valorProducao").val(data[0].valorUnitario);
                $("#valorVenda").val(data[0].valorVenda);
                $('#produtoModal').modal('show');
            }
        });
    });
});