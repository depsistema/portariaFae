$(document).ready(function () {
    $('#tableVisitante').DataTable(
        {
            "language":{
                "url": "//cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json",
            },
            order: [[0, 'desc']],
        },
    )
});

$(document).ready(function () {
    $('#tableControleVeiculo').DataTable(
        {
            "language":{
                "url": "//cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json",
            },
            order: [[0, 'desc']],
        },
    )
});

$(document).ready(function () {
    $('#tableControleChave').DataTable(
        {
            "language":{
                "url": "//cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json",
            },
            order: [[0, 'desc']],
        },
    )
});

$(document).ready(function () {
    $('#relatorioVisitante').DataTable(
        {
            "language":{
                "url": "//cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json",
            },
            order: [[0, 'desc']],
            dom: 'Bfrtip',
            buttons: [
                'excel', 'pdf',
            ],
        },
    )
});

$(document).ready(function () {
    $('#relatorioChave').DataTable(
        {
            "language":{
                "url": "//cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json",
            },
            order: [[0, 'desc']],
            dom: 'Bfrtip',
            buttons: [
                'excel', 'pdf',
            ],
            
        },
    )
});

$(document).ready(function () {
    $('#relatorioVeiculo').DataTable(
        {
            "language":{
                "url": "//cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json",
            },
            order: [[0, 'desc']],
            dom: 'Bfrtip',
            buttons: [
                'excel', 'pdf',
            ],
        },
    )
});