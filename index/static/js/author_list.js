function get_authors(char){
    $('#authors').html('<div class="center"><div class="spinner-border text-info" role="status"><span class="sr-only">Loading...</span></div></div>');
    $.ajax({
        url: '/authors_list',
        data: {'char' : char},
        success: function(data){
            $('#filter-char').html(char);
            $('#authors').html(data);
        } 
    })
}

function get_page(num){
    $('#authors').html('<div class="center"><div class="spinner-border text-info" role="status"><span class="sr-only">Loading...</span></div></div>');
    $.ajax({
        url: '/authors_list',
        data: {'char' : $('#filter-char').html(), 'page' : num},
        success: function(data){            
            $('#authors').html(data);
        } 
    })
}
