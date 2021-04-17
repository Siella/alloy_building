(() => {
    'use strict';

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation');

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms).forEach((form) => {
        form.addEventListener('submit', (event) => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
})();

const saveData = (function () {
    const a = document.createElement("a");
    document.body.appendChild(a);
    a.style = "display: none";

    return function (data, fileName) {
        const blob = new Blob([data], {type: "text/csv"}),
            url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = fileName;
        a.click();
        window.URL.revokeObjectURL(url);
    };
})();

function serverResponseCallbackFactory(tableName) {
    const tblNode = $(tableName);
    const tbl = new Table(tblNode);

    tblNode.find(".goose-export-result").click(function () {
        const result = "result\n" + tbl.column("result").join("\n");
        saveData(result, "result.csv");
    });

    tblNode.find(".goose-export-full").click(function () {
        const csv = tbl.exportAsCsv();
        saveData(csv, "full.csv");
    });

    function f(data) {
        if (data.ok) {
            tbl.loadData(data.data.table);
        }
    }

    return f;
}

$(document).ready(function () {
    $(".goose-manual-form-check").change(function () {
        const id = this.id.split('Skip')[0];
        $('#' + id).attr('required', !this.checked);
        $('#' + id).attr('disabled', this.checked);
    });

    $("#batchOutlierMin").change(function () {
        const val = $(this).val();
        if (val > $("#batchOutlierMax").val()) {
            $("#batchOutlierMax").val(val);
        }
    });

    $("#batchOutlierMax").change(function () {
        const val = $(this).val();
        if (val < $("#batchOutlierMin").val()) {
            $("#batchOutlierMin").val(val);
        }
    });

    const csvParamsValidator = function () {
        const decimal = $("#batchCsvDecimal");
        const delimiter = $("#batchCsvDelimiter");
        if (decimal.val() === delimiter.val()) {
            decimal[0].setCustomValidity("Разделители должны быть разными");
            delimiter[0].setCustomValidity("Разделители должны быть разными");
        } else {
            decimal[0].setCustomValidity("");
            delimiter[0].setCustomValidity("");
        }
    };

    $("#batchCsvDelimiter").change(csvParamsValidator);
    $("#batchCsvDecimal").change(csvParamsValidator);

    const submitHandlerFactory = function (tableName) {
        return function (event) {
            event.preventDefault();
            const form = $(this)[0];
            const formData = new FormData(form);

            $.ajax({
                url: $(this).attr("action"),
                type: "POST",
                enctype: 'multipart/form-data',
                data: formData,
                cache: false,
                contentType: false,
                processData: false
            }).done(serverResponseCallbackFactory(tableName)).fail(function (jqXHR, textStatus, error) {
                console.log(jqXHR);
                console.log(textStatus);
                console.log(error);
            });
        };
    };

    $("#manualForm").submit(submitHandlerFactory("#manualTable"));
    $("#batchForm").submit(submitHandlerFactory("#batchTable"));
});