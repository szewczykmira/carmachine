/**
 * Created by mira on 6/10/16.
 */

var delete_employee_id = null;
$('.removeObject').on('click', function(){
    delete_employee_id = $(this).data('id');
});

$('#modalDelete').on('click', function(){
    $.ajax({
        type: "POST",
        url: delete_url,
        data: {
            'csrfmiddlewaretoken': csrf,
            'object_id': delete_employee_id
        },
        success: function(data){
            if(data.success){
                $('#object-'+delete_employee_id).hide();
            }
        }
    });
    $('#deleteModal').modal('hide');
});
