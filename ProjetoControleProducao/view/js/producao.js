$(document).ready(function(){
    
    $(function(){
        carregar("http://localhost:5000/producoes");
    });

    $("#pesquisar").click(function(){
        var id_producao = $("#pesquisa").val();
        $("#pesquisa").val("");
        if (id_producao === ""){
            carregar("http://localhost:5000/producoes");
        } else{
            carregar("http://localhost:5000/producoes/" + id_producao);     
        }
    });

    function carregar(url){
        $.get(url,function(data,status){
            if (data.length === 0){
                $("#listaProducoes").html("<tr><td colspan=1>Nenhuma Produção encontrada!</td></tr>");
            } else{
                var table = "";
                for(x in data){
                    var finalizar = "";
                    if (!data[x].finalizada){
                        finalizar = "<a href=# id='finalizar_" + data[x].id + "' class='finalizar_producao'>" + 
                                        "<img src='img/finalizar.ico' alt='Finalizar Produção' title='Finalizar Produção' height='30' width='30'>" +
                                    "</a>";
                    }
                    table += "<tr class='linha'>" +
                                "<td>" + data[x].produto.nome + "</td>" +
                                "<td>" + data[x].quantidadeProduzida + "</td>" +
                                "<td>" + data[x].finalizada + "</td>" +
                                "<td>" + data[x].tempoTotal + "</td>" +
                                "<td>" + data[x].custoTotal + "</td>" +
                                "<td>" + 
                                    "<a href=# id='adicionar_" + data[x].id + "' class='adicionar_processo'>" + 
                                        "<img src='img/adicionar.ico' alt='Adicionar Processo' title='Adicionar Processo' height='30' width='30'>" +
                                    "</a>" +
                                    "<a href=# id='ver_" + data[x].id + "' class='ver_processos'>" + 
                                        "<img src='img/detalhes.ico' alt='Visualizar Processos' title='Visualizar Processos' height='30' width='30'>" +
                                    "</a>" +
                                    finalizar + 
                                    "<a href=# id='excluir_" + data[x].id + "' class='excluir_producao'>" + 
                                        "<img src='img/excluir.ico' alt='Excluir Produção' title='Excluir Produção' height='30' width='30'>" +
                                    "</a>" +
                                "</td>" +
                            "</tr>";
                }
                $("#listaProducoes").html(table);
            }
        });
    };

    $(document).on("click", "#salvarProducao", function() {
        produtoProduzido = $("#produtoId").val();
        quantidade = $("#quantidadeProduzida").val();
        var dados = JSON.stringify({produto_id: produtoProduzido, quantidadeProduzida: quantidade}); 
        $.ajax({ 
            url: "http://localhost:5000/producoes", 
            type: "POST", 
            dataType: "json",
            contentType: "application/json",
            data: dados, 
            success: sucessoSalvarProducao,
            error: erroAoIncluirProducao
        });

        function sucessoSalvarProducao (retorno) {
            if (retorno.resultado == "ok") {
                alert("Produção salva com sucesso!");
                fecharModalProducao();
                carregar("http://localhost:5000/producoes");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoIncluirProducao (retorno) {
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });

    $("#producaoModal").on("shown.bs.modal", function (e) {
        $("#produtoId").empty();
        $.get("http://localhost:5000/produtos",function(produtos,status){
            for (var p in produtos) {
                $("#produtoId").append( 
                    $("<option></option>").attr("value", produtos[p].id).text(produtos[p].nome));
            }
        });
    });

    $(document).on("click", "#cancelarProducao", function() {
        fecharModalProducao();
    });

    $(document).on("click", "#fecharModalProducao", function() {
        fecharModalProducao();
    });

    function fecharModalProducao(){
        $("#produtoId").val("");
        $("#quantidadeProduzida").val("");
        $('#producaoModal').modal('hide');
    };

    $(document).on("click", ".excluir_producao", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_"; 
        var id_producao = componente_clicado.substring(nome_icone.length); 
        $.ajax({ 
            url: "http://localhost:5000/producoes/" + id_producao, 
            type: "DELETE",
            dataType: "json",
            success: sucessoExcluirProducao, 
            error: erroAoExcluirProducao
        });

        function sucessoExcluirProducao (retorno) {
            if (retorno.resultado == "ok") { 
                alert("Produção removida com sucesso!");
                carregar("http://localhost:5000/producoes");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoExcluirProducao (retorno) { 
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes); 
        }
    });

    $(document).on("click", ".finalizar_producao", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "finalizar_"; 
        var id_producao = componente_clicado.substring(nome_icone.length); 
        $.ajax({ 
            url: "http://localhost:5000/producoes/" + id_producao + "/finalizar", 
            type: "POST",
            dataType: "json",
            success: sucessoFinalizarProducao, 
            error: erroAoFinalizarProducao
        });

        function sucessoFinalizarProducao (retorno) {
            if (retorno.resultado == "ok") {
                alert("Produção finalizada com sucesso!");
                carregar("http://localhost:5000/producoes");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoFinalizarProducao (retorno) { 
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes); 
        }
    });
    
});