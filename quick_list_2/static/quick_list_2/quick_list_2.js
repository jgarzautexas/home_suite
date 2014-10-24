$(document).ready(function(){
     var csrftoken = $.cookie("csrftoken");
    // $('.list_title').on('swiperight', function(e){
    //     console.log("Sliding right");
    //     $(this).toggle();
    // });
//     $('.list_buttons').on({
//         click: function(event){
//             event.preventDefault();
//             $('#list_form').toggle();
//             console.log("Tyring to add a list");
//         }
//     });

//     $('.item_delete').on({
//         click: function(event){
//             event.preventDefault();
//             console.log("Tyring to delete item");
//         }
//     });
});

function csrfSafeMethod(method) {
        console.log("calling method");
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$(document).on('pagecreate', function(evt){
    var csrftoken = $.cookie("csrftoken");
    $('.list_title').on('swiperight', function(e){
        console.log("Sliding right");
        $(this).toggle();
    });

    $('.list_buttons').on({
        click: function(event){
            event.preventDefault();
            $('#list_form_content #list_form').toggle();
            console.log("Tyring to add a list");
        }
    }, '#add_list_button');

    $('.item_delete').on({
        click: function(event){
            event.preventDefault();
            console.log("Tyring to delete item");
            var $this = $(this);
            // var $exist_item_form = $this.closest(".exist_item_form").wrapAll('<form />').submit();
            // var $exist_item_form = $this.closest(".exist_item_form").submit();
            // var $exist_item_form = $this.closest(".exist_item_form");

            var $exist_item_form = $this.closest(".exist_item_form").wrapAll('<form method="DELETE" />');
            var $quick_list_id = $exist_item_form.find("#id_quick_list_id").val();
            console.log($quick_list_id);
            var $url = "/quick_list_2/" + $quick_list_id;
            // var $quick_list_id = $exist_item_form.find("#id_quick_list_id").val();
            // console.log($quick_list_id);
            $.ajax($url, {
                type: 'DELETE',
                 data: $exist_item_form.serialize(),
                    // console.log(data);
                success: function(response){
                    $exist_item_form.fadeOut(300, function(){ $(this).remove('slow');});
                },
                error: function(request, errorType, errorMessage){
                    alert("error:" +  errorType, + 'with message: ' + errorMessage);

                },
                timeout: 3000,

                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
     
                },
                complete: function(){

                },
            });
        }
    });

    $('.item_button_form').on({
        click: function(event){
            event.preventDefault();
            console.log("Tyring to edit item");
            var $this = $(this);
            // var $exist_item_form = $this.closest(".exist_item_form").wrapAll('<form />').submit();
            // var $exist_item_form = $this.closest(".exist_item_form").submit();
            var $exist_item_form = $this.closest(".exist_item_form");
            var $quick_list_id = $exist_item_form.find("#id_quick_list_id").val();

            var $url = "/quick_list_2/" + $quick_list_id;
            console.log($exist_item_form);
            $.ajax($url, {
                type: 'POST',
                 data: $exist_item_form.serialize(),
                    // console.log(data);
                success: function(response){

                },
                error: function(request, errorType, errorMessage){
                    alert("error:" +  errorType, + 'with message: ' + errorMessage);

                },
                timeout: 3000,

                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
     
                },
                complete: function(){

                },
            });
        }
    });
});
