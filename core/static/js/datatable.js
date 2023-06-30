$(document).ready(function () {
    $('#tableVisitante').DataTable(
        {
            "language":{
                "url": "//cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json",
            },
            order: [[0, 'desc']],
            dom: 'Bfrtip',
            buttons: [
                'excelHtml5',
                'pdfHtml5'
            ]
        },
    )
});

$(document).ready(function () {
    $('#tableControleVeiculo').DataTable(
        {
            "language":{
                "url": "//cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json",
            },
            order: [[2, 'desc']],
            dom: 'Bfrtip',
            buttons: [
                'excelHtml5',
                'pdfHtml5'
            ]
        },
    )
});

$(document).ready(function () {
    $('#tableControleChave').DataTable(
        {
            "language":{
                "url": "//cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json",
            },
            order: [[2, 'desc']],
            dom: 'Bfrtip',
            buttons: [
                'excelHtml5',
                'pdfHtml5'
            ]
        },
    )
});