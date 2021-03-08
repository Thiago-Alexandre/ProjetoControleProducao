$(document).ready(function(){
    
    $(document).on("click", ".adicionar_processo", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "adicionar_";
        var id_producao = componente_clicado.substring(nome_icone.length);
        $("#idProducao").val(id_producao);
        $('#novoProcessoModal').modal('show'); 
    });

    $("#novoProcessoModal").on("shown.bs.modal", function (e) {
        $("#tipoId").empty();
        $.get("http://localhost:5000/tipos",function(tipos,status){
            for (var t in tipos) {
                $("#tipoId").append( 
                    $("<option></option>").attr("value", tipos[t].id).text(tipos[t].nome));
            }
        });
        $("#supervisorId").empty();
        $.get("http://localhost:5000/funcionarios",function(funcionarios,status){
            for (var f in funcionarios) {
                $("#supervisorId").append( 
                    $("<option></option>").attr("value", funcionarios[f].id).text(funcionarios[f].nome));
            }
        });
    });

    $(document).on("click", "#salvarNovoProcesso", function() {
        idProducao = $("#idProducao").val();
        tipoProcesso = $("#tipoId").val();
        supervisorProcesso = $("#supervisorId").val();
        var dados = JSON.stringify({tipo_id: tipoProcesso, producao_id: idProducao, supervisor_id: supervisorProcesso}); 
        $.ajax({ 
            url: "http://localhost:5000/processos", 
            type: "POST", 
            dataType: "json",
            contentType: "application/json",
            data: dados, 
            success: sucessoSalvarProcesso,
            error: erroAoIncluirProcesso
        });

        function sucessoSalvarProcesso (retorno) {
            if (retorno.resultado == "ok") {
                alert("Processo salvo com sucesso!");
                fecharModalProcesso();
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoIncluirProcesso (retorno) {
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });

    $(document).on("click", "#cancelarNovoProcesso", function() {
        fecharModalProcesso();
    });

    $(document).on("click", "#fecharModalProcesso", function() {
        fecharModalProcesso();
    });

    function fecharModalProcesso(){
        $("#idProducao").val("");
        $('#novoProcessoModal').modal('hide');
    };

    $(document).on("click", ".ver_processos", function() { 
        var componente_clicado = $(this).attr('id');
        var nome_icone = "ver_"; 
        var id_producao = componente_clicado.substring(nome_icone.length);
        carregarProcessos(id_producao);
        $('#processosModal').modal('show');
    });

    function carregarProcessos(id){
        var url = "http://localhost:5000/producoes/" + id + "/processos";
        $.get(url,function(data,status){
            if (data.length === 0){
                $("#listaProcessos").html("<tr><td colspan=1>Nenhum Processo encontrado!</td></tr>");
            } else{
                var table = "";
                for(x in data){
                    var aprovar = "";
                    var reprovar = "";
                    if (!data[x].aprovado){
                        aprovar = "<a href=# id='aprovar_processo_" + data[x].id + "' class='aprovar_processo'>" + 
                                        "<img src='img/aprovar.ico' alt='Aprovar Processo' title='Aprovar Processo' height='30' width='30'>" +
                                    "</a>";
                        reprovar = "<a href=# id='reprovar_processo_" + data[x].id + "' class='reprovar_processo'>" + 
                                        "<img src='img/reprovar.ico' alt='Reprovar Processo' title='Reprovar Processo' height='30' width='30'>" +
                                    "</a>";
                    } 
                    table += "<tr class='linha'>" +
                                "<td>" + data[x].tipo.nome + "</td>" +
                                "<td>" + data[x].supervisor.nome + "</td>" +
                                "<td>" + data[x].horaInicial + "</td>" +
                                "<td>" + data[x].horaFinal + "</td>" +
                                "<td>" + data[x].aprovado + "</td>" +
                                "<td>" + data[x].tempoTotal + "</td>" +
                                "<td>" + data[x].custoTotal + "</td>" +
                                "<td>" + 
                                    aprovar + reprovar +
                                    "<a href=# id='ver_materiais_" + data[x].id + "' class='ver_materiais'>" + 
                                        "<img src='img/material.ico' alt='Visualizar Materiais no Processo' title='Visualizar Materiais no Processo' height='30' width='30'>" +
                                    "</a>" +
                                    "<a href=# id='ver_funcionarios_" + data[x].id + "' class='ver_funcionarios'>" + 
                                        "<img src='img/funcionario.ico' alt='Visualizar Funcionários no Processo' title='Visualizar Funcionários no Processo' height='30' width='30'>" +
                                    "</a>" +
                                    "<a href=# id='excluir_processo_" + data[x].id + "' class='excluir_processo'>" + 
                                        "<img src='img/excluir.ico' alt='Excluir Processo' title='Excluir Processo' height='30' width='30'>" +
                                    "</a>" +
                                "</td>" +
                            "</tr>";
                }
                $("#listaProcessos").html(table);
            }
        });
    }

    $(document).on("click", "#okProcessos", function() {
        $("#listaProcessos").html("");
        $("#processosModal").modal("hide");
    });

    $(document).on("click", "#fecharModalProcessos", function() {
        $("#listaProcessos").html("");
        $("#processosModal").modal("hide");
    });

    $(document).on("click", ".excluir_processo", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_processo_"; 
        var id_processo = componente_clicado.substring(nome_icone.length); 
        $.ajax({ 
            url: "http://localhost:5000/processos/" + id_processo,
            type: "DELETE",
            dataType: "json",
            success: function(retorno) {
                if (retorno.resultado == "ok") { 
                    alert("Processo removido com sucesso!");
                    $("#listaProcessos").html("");
                    $("#processosModal").modal("hide");
                } else {
                    alert(retorno.resultado + ":" + retorno.detalhes);
                }
            },
            error: function (retorno) { 
                alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes); 
            }
        });
    });

    $(document).on("click", ".aprovar_processo", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "aprovar_processo_"; 
        var id_processo = componente_clicado.substring(nome_icone.length);
        var dados = JSON.stringify({aprovado: true});
        $.ajax({ 
            url: "http://localhost:5000/processos/" + id_processo + "/finalizar", 
            type: "POST",
            dataType: "json",
            contentType: "application/json",
            data: dados,
            success: sucessoAprovarProcesso, 
            error: erroAoAprovarProcesso
        });

        function sucessoAprovarProcesso (retorno) {
            if (retorno.resultado == "ok") {
                alert("Processo Aprovado!");
                $("#listaProcessos").html("");
                $("#processosModal").modal("hide");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoAprovarProcesso (retorno) { 
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes); 
        }
    });

    $(document).on("click", ".reprovar_processo", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "reprovar_processo_"; 
        var id_processo = componente_clicado.substring(nome_icone.length);
        var dados = JSON.stringify({aprovado: false});
        $.ajax({ 
            url: "http://localhost:5000/processos/" + id_processo + "/finalizar", 
            type: "POST",
            dataType: "json",
            contentType: "application/json",
            data: dados,
            success: sucessoReprovarProcesso, 
            error: erroAoReprovarProcesso
        });

        function sucessoReprovarProcesso (retorno) {
            if (retorno.resultado == "ok") {
                alert("Processo Reprovado!");
                $("#listaProcessos").html("");
                $("#processosModal").modal("hide");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoReprovarProcesso (retorno) { 
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes); 
        }
    });
    
});