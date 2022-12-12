setInterval(() => {
    $(document).ready(function () {
        $("div.btn-success").click(function () {
            $('#prescriptionDetail').append(`<tr>
        <td class="col-xs-2"><input type="text" name="medicine_id" id="medicine_id"></td>
        <td class="col-xs-2"><input type="text" name="medicine_name" id="medicine_name"></td>
        <td class="col-xs-2"><input type="text" name="dose" id="dose"></td>
        <td class="col-xs-2"><input type="text" name="usage" id="usage"></td>
        <td><div class="btn btn-success">Add</div></td>
        <td><div class="btn btn-danger">Delete</div></td>
        </tr`)
        });
        // $('#prescriptionDetail btn-success')
        $("div.btn-danger").click(function () {
            alert($(this).parent)
            $('#prescriptionDetail').remove($(this).parent.parent)
        })
    });

}, 3000);


