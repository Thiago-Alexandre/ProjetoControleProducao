$(document).ready(function(){

    $(document).on("click", ".ver_materiais", function() { 
        var componente_clicado = $(this).attr('id');
        var nome_icone = "ver_materiais_"; 
        var id_processo = componente_clicado.substring(nome_icone.length);
        $("#idProcessoMateriais").val(id_processo);
        carregarMateriais(id_processo);
        $('#processosModal').modal('hide');
        $('#materiaisModal').modal('show');
    });

    function carregarMateriais(id){
        var url = "http://localhost:5000/processos/" + id + "/materiais";
        $.get(url,function(data,status){
            if (data.length === 0){
                $("#listaMateriais").html("<tr><td colspan=1>Nenhum Material encontrado!</td></tr>");
            } else{
                var table = "";
                for(x in data){
                    table += "<tr class='linha'>" +
                                "<td>" + data[x].material.nome + "</td>" +
                                "<td>" + data[x].quantidadeUsada + "</td>" +
                                "<td>" +
                                    "<a href=# id='excluir_material_" + data[x].id + "' class='excluir_material'>" + 
                                        "<img src='img/excluir.ico' alt='Excluir Material Usado' title='Excluir Material Usado' height='30' width='30'>" +
                                    "</a>" +
                                "</td>" +
                            "</tr>";
                }
                $("#listaMateriais").html(table);
            }
        });
    }

    function fecharModalMateriais(){
        $("#idProcessoMateriais").val("");
        $("#listaMateriais").html("");
        $("#materiaisModal").modal("hide");
        $("#processosModal").modal("show");
    };

    $(document).on("click", "#okMateriais", function() {
        fecharModalMateriais();
    });

    $(document).on("click", "#fecharModalMateriais", function() {
        fecharModalMateriais();
    });

    $(document).on("click", ".excluir_material", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_material_"; 
        var id_material = componente_clicado.substring(nome_icone.length); 
        $.ajax({ 
            url: "http://localhost:5000/materiais_processo/" + id_material,
            type: "DELETE",
            dataType: "json",
            success: function (retorno) {
                if (retorno.resultado == "ok") { 
                    alert("Material Usado removido com sucesso!");
                    fecharModalMateriais();
                } else {
                    alert(retorno.resultado + ":" + retorno.detalhes);
                }
            },
            error: function (retorno) {
                alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes); 
            }
        });
    });

    $(document).on("click", "#addMaterial", function() {
        $("#idProcesso").val($("#idProcessoMateriais").val());
        $.get("http://localhost:5000/materiais",function(materiais,status){
            alert(status);
            for (var m in materiais) {
                $("#materialId").append( 
                    $("<option></option>").attr("value", materiais[m].id).text(materiais[m].nome));
            }
        });
        $("#materiaisModal").modal("hide");
        $('#novoMaterialModal').modal('show');
    });

    function fecharModalMaterial(){
        $("#idProcesso").val("");
        $("#materialId").empty();
        $("#novoMaterialModal").modal("hide");
        fecharModalMateriais();
    };

    $(document).on("click", "#cancelarNovoMaterial", function() {
        fecharModalMaterial();
    });

    $(document).on("click", "#fecharModalMaterial", function() {
        fecharModalMaterial();
    });


    $(document).on("click", "#salvarNovoMaterial", function() {
        var idProcesso = $("#idProcesso").val();
        var idMaterial = $("#materialId").val();
        var quantidadeConsumida = $("#quantidadeUsada").val();
        var dados = JSON.stringify({processo_id: idProcesso, material_id: idMaterial, quantidadeUsada: quantidadeConsumida}); 
        $.ajax({ 
            url: "http://localhost:5000/materiais_processo", 
            type: "POST", 
            dataType: "json",
            contentType: "application/json",
            data: dados, 
            success: function (retorno) {
                if (retorno.resultado == "ok") { 
                    alert("Material Usado adicionado com sucesso!");
                    fecharModalMaterial();
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