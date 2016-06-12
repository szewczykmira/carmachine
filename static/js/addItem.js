/**
 * Created by mira on 6/12/16.
 */

$('#modalAddItem').click(function(){
    var frm = $('#addItem');
    console.log('Click!');
    $.ajax({
        type: frm.attr('type'),
        url: frm.attr('action'),
        data: frm.serialize(),
        success: function(data){
            if(data.success){
                tbody.append(data.row);
                $('.price').innerHTML = data.price;
            }
        }
    })
});
