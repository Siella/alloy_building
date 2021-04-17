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

function processServerResponse(data) {
    if (data.ok) {
        const columnNames = data.data;
        $("#columnCounter").text(columnNames.length);
        $("#columnList").empty();

        for (const column of columnNames) {
            $("#columnList").append(
                $("<li/>")
                    .addClass("list-group-item d-flex justify-content-between lh-sm")
                    .append($("<h6/>")
                        .addClass("my-0")
                        .text(column)
                    )
            );
        }
    }
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

    $("#fileUploadForm").submit(function (event) {
        event.preventDefault();
        const form = $("#fileUploadForm")[0];
        const formData = new FormData(form);
        console.log(...formData);

        $.ajax({
            url: $(this).attr("action"),
            type: "POST",
            enctype: 'multipart/form-data',
            data: formData,
            success: processServerResponse,
            cache: false,
            contentType: false,
            processData: false
        });
    });
});