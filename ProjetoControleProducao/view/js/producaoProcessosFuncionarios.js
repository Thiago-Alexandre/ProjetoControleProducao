$(document).ready(function(){

    $(document).on("click", ".ver_funcionarios", function() { 
        var componente_clicado = $(this).attr('id');
        var nome_icone = "ver_funcionarios_"; 
        var id_processo = componente_clicado.substring(nome_icone.length);
        $("#idProcessoFuncionarios").val(id_processo);
        carregarFuncionarios(id_processo);
        $('#processosModal').modal('hide');
        $('#funcionariosModal').modal('show');
    });

    function carregarFuncionarios(id){
        var url = "http://localhost:5000/processos/" + id + "/funcionarios";
        $.get(url,function(data,status){
            if (data.length === 0){
                $("#listaFuncionarios").html("<tr><td colspan=1>Nenhum Funcionário encontrado!</td></tr>");
            } else{
                var table = "";
                for(x in data){
                    table += "<tr class='linha'>" +
                                "<td>" + data[x].funcionario.nome + "</td>" +
                                "<td>" +
                                    "<a href=# id='excluir_funcionario_" + data[x].id + "' class='excluir_funcionario'>" + 
                                        "<img src='img/excluir.ico' alt='Excluir Funcionário do Processo' title='Excluir Funcionário do Processo' height='30' width='30'>" +
                                    "</a>" +
                                "</td>" +
                            "</tr>";
                }
                $("#listaFuncionarios").html(table);
            }
        });
    }

    function fecharModalFuncionarios(){
        $("#idProcessoFuncionarios").val("");
        $("#listaFuncionarios").html("");
        $("#funcionariosModal").modal("hide");
        $("#processosModal").modal("show");
    };

    $(document).on("click", "#okFuncionarios", function() {
        fecharModalFuncionarios();
    });

    $(document).on("click", "#fecharModalFuncionarios", function() {
        fecharModalFuncionarios();
    });

    $(document).on("click", ".excluir_funcionario", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_funcionario_"; 
        var id_funcionario = componente_clicado.substring(nome_icone.length); 
        $.ajax({ 
            url: "http://localhost:5000/funcionarios_processo/" + id_funcionario,
            type: "DELETE",
            dataType: "json",
            success: function (retorno) {
                if (retorno.resultado == "ok") { 
                    alert("Funcionário removido do Processo com sucesso!");
                    fecharModalFuncionarios();
                } else {
                    alert(retorno.resultado + ":" + retorno.detalhes);
                }
            },
            error: function (retorno) {
                alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes); 
            }
        });
    });

    $(document).on("click", "#addFuncionario", function() {
        $("#idProcessoF").val($("#idProcessoFuncionarios").val());
        $.get("http://localhost:5000/funcionarios",function(funcionarios,status){
            for (var f in funcionarios) {
                $("#funcionarioId").append( 
                    $("<option></option>").attr("value", funcionarios[f].id).text(funcionarios[f].nome));
            }
        });
        $("#funcionariosModal").modal("hide");
        $('#novoFuncionarioModal').modal('show');
    });

    function fecharModalFuncionario(){
        $("#idProcessoF").val("");
        $("#funcionarioId").empty();
        $("#novoFuncionarioModal").modal("hide");
        fecharModalFuncionarios();
    };

    $(document).on("click", "#cancelarNovoFuncionario", function() {
        fecharModalFuncionario();
    });

    $(document).on("click", "#fecharModalFuncionario", function() {
        fecharModalFuncionario();
    });


    $(document).on("click", "#salvarNovoFuncionario", function() {
        var idProcesso = $("#idProcessoF").val();
        var idFuncionario = $("#funcionarioId").val();
        var dados = JSON.stringify({processo_id: idProcesso, funcionario_id: idFuncionario}); 
        $.ajax({ 
            url: "http://localhost:5000/funcionarios_processo", 
            type: "POST", 
            dataType: "json",
            contentType: "application/json",
            data: dados, 
            success: function (retorno) {
                if (retorno.resultado == "ok") { 
                    alert("Funcionário adicionado no Processo com sucesso!");
                    fecharModalFuncionario();
                } else {
                    alert(retorno.resultado + ":" + retorno.detalhes);
                }
            },
            error: function (retorno) {
                alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes); 
            }
        });
    });
    
});