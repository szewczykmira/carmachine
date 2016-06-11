/**
 * Created by mira on 6/10/16.
 */

var searchInput = $('#searchInput');
var tbody = $('tbody');

searchInput.focus(function(){
    $(this).parent().parent().parent().addClass('is-focused');
});

searchInput.focusout(function(){
    $(this).parent().parent().parent().removeClass('is-focused');
});

var delay = (function(){
    var timer = 0;
    return function(callback, ms){
        clearTimeout (timer);
        timer = setTimeout(callback, ms);
    };
})();

var sortBy = null;

function toggleSort(elem){
    let n = $(elem).data('time');
    let name = $(elem).data('type');
    switch(n){
        case 0:
            sortBy = null;
            break;
        case 1:
            sortBy = name;
            break;
        case 2:
            sortBy = "-" + name;
            break;
    }
    $(elem).data('time', (n + 1) % 3);
    console.log($(elem).data('time'));
    console.log($(elem).data('type'));
    
}

$('.sort').click(function(){
    toggleSort(this);
    find();
});

function find(){
    let searchValue = searchInput.val();
    $.ajax({
        type: 'get',
        url: search_url,
        data: {
            'input': searchValue,
            'sort' : sortBy
        },
        success: function(data){
            var objects = data.objects;
            tbody.empty();
            for(let i=0; i< objects.length; i++){
                tbody.append(objects[i]);
            }
        }
    })

}

searchInput.keyup(function() {
  delay(find, 700);
});