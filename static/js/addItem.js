/**
 * Created by mira on 6/12/16.
 */
var tbody = $('tbody');

$('#modalAddItem').click(function(){
    var frm = $('form');
    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: frm.serialize(),
        success: function(data){
            if(data.success){
                tbody.append(data.row);
                $('.price').text(data.price);
                frm[0].reset();
                $('#addItem').modal('hide');
            }
        }
    })
});
