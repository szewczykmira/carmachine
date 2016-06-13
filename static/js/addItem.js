/**
 * Created by mira on 6/12/16.
 */
var tbody = $('tbody');

$('#modalAddItem').click(function(){
    var frm = $('form');
    console.log('Click!');
    console.log(frm.attr('method'));
    console.log(frm.attr('action'));
    console.log(frm.serialize());
    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: frm.serialize(),
        success: function(data){
            if(data.success){
                tbody.append(data.row);
                $('.price').innerHTML = data.price;
                frm[0].reset();
                $('#addItem').modal('hide');
            }
        }
    })
});
