$(document).ready(function(){
    
    $(function(){
        carregar("http://localhost:5000/tipos");
    });

    $("#pesquisar").click(function(){
        id_tipo = $("#pesquisa").val();
        $("#pesquisa").val("");
        if (id_tipo === ""){
            carregar("http://localhost:5000/tipos");
        } else{
            carregar("http://localhost:5000/tipos/" + id_tipo);     
        }
    });

    function carregar(url){
        $.get(url,function(data,status){
            if (data.length === 0){
                $("#listaTipos").html("<tr><td colspan=1>Nenhum Tipo de Processo encontrado!</td></tr>");
            } else{
                var table = "";
                for(x in data){
                    table += "<tr class='linha'>" +
                                "<td>" + data[x].nome + "</td>" +
                                "<td>" + 
                                    "<a href=# id='editar_" + data[x].id + "' class='editar_tipo'>" + 
                                        "<img src='img/editar.ico' alt='Editar Tipo de Processo' title='Editar tipo' height='30' width='30'>" +
                                    "</a>" +
                                    "<a href=# id='excluir_" + data[x].id + "' class='excluir_tipo'>" + 
                                        "<img src='img/excluir.ico' alt='Excluir Tipo de Processo' title='Excluir tipo' height='30' width='30'>" +
                                    "</a>" +
                                "</td>" +
                            "</tr>";
                }
                $("#listaTipos").html(table);
            }
        });
    };

    $(document).on("click", "#salvar", function() {
        idTipo = $("#idTipo").val();
        nomeTipo = $("#nomeTipo").val();
        descricaoTipo = $("#descricaoTipo").val();
        metodo = "PUT";
        endpoint = "http://localhost:5000/tipos/" + idTipo;
        if (idTipo === ""){
            metodo = "POST";
            endpoint = "http://localhost:5000/tipos";
        }
        var dados = JSON.stringify({nome: nomeTipo, descricao: descricaoTipo}); 
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
                alert("Tipo de Processo salvo com sucesso!");
                fecharModal();
                carregar("http://localhost:5000/tipos");
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
        $("#idTipo").val("");
        $("#nomeTipo").val("");
        $("#descricaoTipo").val("");
        $('#tipoModal').modal('hide');
    };

    $(document).on("click", ".excluir_tipo", function() { 
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_"; 
        var id_tipo = componente_clicado.substring(nome_icone.length); 
        $.ajax({ 
            url: "http://localhost:5000/tipos/" + id_tipo, 
            type: "DELETE",
            dataType: "json",
            success: sucessoExcluir, 
            error: erroAoExcluir 
        });

        function sucessoExcluir (retorno) {
            if (retorno.resultado == "ok") { 
                alert("Tipo de Processo removido com sucesso!");
                carregar("http://localhost:5000/tipos");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoExcluir (retorno) { 
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes); 
        }
    });

    $(document).on("click", ".editar_tipo", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "editar_";
        var id_tipo = componente_clicado.substring(nome_icone.length);
        var url = "http://localhost:5000/tipos/" + id_tipo;
        $.get(url,function(data,status){
            if (data.length === 0){
                alert("Nenhum Tipo de Processo encontrado!")
            } else{
                $("#idTipo").val(data[0].id);
                $("#nomeTipo").val(data[0].nome);
                $("#descricaoTipo").val(data[0].descricao);
                $('#tipoModal').modal('show'); 
            }
        });
    });
});