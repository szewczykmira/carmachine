/**
 * Created by mira on 6/6/16.
 */

$('.active-checkbox').on('click', function(){
    var account_id = $(this).data('id');
    $.ajax({
        type: "POST",
        url: toggle_activate_url,
        data:
        {
            'account_id': account_id,
            'csrfmiddlewaretoken': csrf
        },
        success: function(data) {
            if(data.success=true){
                $('#activation-success').show();
            } else {
                $('#activation-fail').show();
            }
        }
    })
});
