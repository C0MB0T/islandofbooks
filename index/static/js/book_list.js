function get_books(filt){
    $('#books').html('<div class="center"><div class="spinner-border text-info" role="status"><span class="sr-only">Loading...</span></div></div>');
    $.ajax({
        url: '/books_list',
        method: POST,
        data: {filt: filt},
        success: function(data){
            $('#filter-value').html(filt);
            $('#books').html(data);
        }
    })
}

function get_page(num){
    $('#books').html('<div class="center"><div class="spinner-border text-info" role="status"><span class="sr-only">Loading...</span></div></div>');
    $.ajax({
        url: '/books_list',
        method: POST,
        data: {filt: $('#filter-value').html(), page: num},
        success: function(data){
            $('#books').html(data);
        }
    })
}

