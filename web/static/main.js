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