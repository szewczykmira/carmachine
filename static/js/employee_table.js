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

var employee_id = null;
$('.change-salary').on('click', function(){
    employee_id = $(this).data('id');
});

$('#modalSend').on('click', function(){
    var new_salary = $('input[name=salary]').val();
    $.ajax({
        type: "POST",
        url: change_salary_url,
        data: {
            'employee_id': employee_id,
            'new_salary': new_salary,
            'csrfmiddlewaretoken': csrf
        },
        success: function(data){
            if(data.success){
                $('span#salary-' + employee_id).text(new_salary);
                employee_id = null;
            }
        }
    });
    $('#salaryModal').modal('hide');
});

var delete_employee_id = null;
$('.removeEmployee').on('click', function(){
    delete_employee_id = $(this).data('id');
});

$('#modalDelete').on('click', function(){
    $.ajax({
        type: "POST",
        url: delete_employee_url,
        data: {
            'csrfmiddlewaretoken': csrf,
            'employee_id': delete_employee_id
        },
        success: function(data){
            if(data.success){
                $('#employee-'+delete_employee_id).hide();
            }
        }
    });
    $('#modalDelete').modal('hide');
});