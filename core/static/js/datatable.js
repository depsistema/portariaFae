$(document).ready(function () {
    $('#example').DataTable(
        {
            "language":{
                "url": "//cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json",
                order: [[0, 'desc']],
            }
            
        }

    );
});