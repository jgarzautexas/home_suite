function csrfSafeMethod(method) {
        console.log("calling method");
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ready(function(){

    var item_filter = 'All';
    var csrftoken = $.cookie("csrftoken");


    $('.list_filter').on({

        mouseenter: function(){
            // console.log("entering");
            $(this).css( 'cursor', 'pointer' );
            // $(this).find(".list_item_delete").toggle();
        },
        mouseleave: function(){
            // $(this).find(".list_item_delete").toggle();
        },
        dblclick: function(){

        }
    });
    // }, '.exist-item-link');
    $('#all_selection').on("click", function(event){
        console.log("All Selection clicked");
        // //Need to find a better way to do this
        item_filter = "All";
        $(this).find("span").attr('class', 'header').css("font-weight","Bold");
        $('#active_selection').find("span").attr('class', 'subheader');
        $('#complete_selection').find("span").attr('class', 'subheader');

        $forms = $("#item_ul").find('.exist_item_form');
        $forms.each(function(key, value){
            $(this).show();
        });
    });

    $('#active_selection').on("click", function(event){
        console.log("Active Selection clicked");
        //Need to find a better way to do this
        item_filter = "Active";
        $(this).find("span").attr('class', 'header').css("font-weight","Bold");
        $('#all_selection').find("span").attr('class', 'subheader');
        $('#complete_selection').find("span").attr('class', 'subheader');
        $forms = $("#item_ul").find('.exist_item_form');
        $forms.each(function(key, value){
            // console.log(i);
            console.log(this.id_active.value);
            if (this.id_active.value !== "True"){
                $(this).hide();
            }else{
                $(this).show();
            }
        });
    });

    $('#complete_selection').on("click", function(event){
        console.log("Active Selection clicked");
        //Need to find a better way to do this
        item_filter = "Complete";
        $(this).find("span").attr('class', 'header').css("font-weight","Bold");
        $('#all_selection').find("span").attr('class', 'subheader');
        $('#active_selection').find("span").attr('class', 'subheader');
        $forms = $("#item_ul").find('.exist_item_form');
        $forms.each(function(i){
            // console.log(i);
            console.log(this.id_active.value);
            if (this.id_active.value === "False"){
                $(this).show();
            }else{
                $(this).hide();
            }
        });
    });

    $(".list_item_delete").on("click", function(event){
        console.log("Clicked a delete Now I need to do something");
        $(this).closest("li").toggle();
    });

    $(".delete_list_button").on("click", function(event){
        event.preventDefault();
        console.log("Clicked a delete Now I need to do something");
        // $(this).closest("li").toggle();

        item_update($('#delete_list_form'), "DELETE", "/");
    });


    $('.item_active').on("click", function(event){
        console.log("I clicked on the active icon");
    });

    $('.item_name').on("click", function(event){
        console.log("I clicked on the item name icon");
    });

    // For New Item 
    $('#id_name').keypress(function(event){
        console.log("key was pressed");
        if(event.keyCode === 13 ){
            console.log("I really hit enter");
            event.preventDefault();
            $('#new_item_form a').trigger("click");
        }
    });

    // For Quick List Title
    $('#id_title').keypress(function(event){
        console.log("Key was pressed");
        if(event.keyCode === 13 ){
            console.log("I really hit enter");
            event.preventDefault();
            $('#quick_list_form a').trigger("click");
        }
    });

    // Click on the grocery item 
    $('#shopping_list').on({
        mouseenter: function(){
            $(this).css( 'cursor', 'pointer' );
            // $(this).find(".list_item_delete").toggle();
        },
        mouseleave: function(){
            // $(this).find(".list_item_delete").toggle();
        }
    }, '.grocery_link');

    $('#shopping_list').on({
        click: function(event){
            event.preventDefault();
            console.log($(this).find("a").attr('href'))
            window.location.href = $(this).find("a").attr('href')
        }
    },'.grocery_link');

    $('#item_ul').on({
        mouseenter: function(){
            $(this).css( 'cursor', 'pointer' );
            // $(this).find(".list_item_delete").toggle();
        },
        mouseleave: function(){
            // $(this).find(".list_item_delete").toggle();
        },
        dblclick: function(){
            console.log("Item was dbl clicked");
            var $this = $(this);
            var $exist_item_form = $this.closest("form");
            $active = $exist_item_form.find("#id_active").val();

            if($active === "True"){
                console.log("I am true");
                $active = "False";
                $this.css('text-decoration', 'line-through');
                // $this.find("h4").attr('subheader', 'header');
                $this.find("h4").attr('class', 'subheader');
                // if (item_filter === "Active"){
                //     $this.hide();
                // }

            }else{
                console.log("I am false");
                $active = "True";
                $this.css('text-decoration', 'none');
                $this.find("h4").attr('class', 'header');

            }
            $exist_item_form.find("#id_active").val($active);
            item_update($exist_item_form, "PUT");
        }
    }, '.exist-item-link');

    $('.add_new_quick_list_button').on('click', function(event){
        event.preventDefault();
        $('#quick_list_form').toggle();
    });

    // New Quick List
    $('#quick_list_form').on('click', 'a', function(event){
        event.preventDefault();
        var shopping_list = $('#quick_list');
        var list_form = $('#quick_list_form');
        var title = $('#id_title').val();
        var ghetto_json = '{"title": "' + title + '"}';
        var no_list = $('#no_list');
        console.log($('#quick_list_form').serialize());

        // $.ajaxSetup({
        //     beforeSend: function(xhr, settings) {
        //         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        //             xhr.setRequestHeader("X-CSRFToken", csrftoken);
        //         }
        //     }
        // });
        $.ajax('/quick_list', {
            type: 'POST',
            // processData: false,
            data: $('#quick_list_form').serialize(),
            // dataType: 'json',
            success: function(response){
                var title_link = 
                    '<li class="bullet-item quick_list_link">' +
                        '<a class="ui-link" href="/quick_list/' + response.id + '/items">' + 
                            '<h5 class="subheader">' + 
                                    response.title + '</h5></a>' +
                    '</li>';

                if(no_list.text() !== ''){
                    shopping_list.html(title_link);
                }else{
                    shopping_list.append(title_link);   
                }
                list_form.trigger('reset').toggle();
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
            // contentType: 'application/json'
        });
    });

    $('#new_item_form').on('click', 'a', function(event){
        event.preventDefault();
        var $item_ul = $('#item_ul');
        var $item_form = $(this).closest("form"); //$('#new_item_form');
        var $quick_list_id = $item_form.find("#id_quick_list").val();
        console.log("quicklist ID " + $quick_list_id);
        var $url = "/quick_list/" + $quick_list_id + "/items";
        console.log($item_form.serialize());

        $.ajax($url, {
            type: 'POST',
            data:  $item_form.serialize(),
            dataType: 'json',
            success: function(response){
                $active = response.active;
                console.log("testing value" + $active);
                $active  =  ($active === true) ? 'True': 'False';
                // console.log("New "+ $active );
                // $active = response.active.toLowerCase();
                var $item_html = 
                    '<form class="exist_item_form">' +
                        '<input id="id_item_id" name="item_id" type="hidden" value="' + response.id + '">' +
                        '<input id="id_quick_list" name="quick_list" type="hidden" value="' +  response.list_id + '">' +
                        '<input id="id_name" name="name" type="hidden" value="' + response.name +'">' +
                        '<input id="id_active" name="active" type="hidden" value="' + $active + '">' +
                        '<li class="bullet-item exist-item-link">' + 
                        '<h4 class="header">' +
                        response.name + 
                        '</h4>' +
                        '</li>' +
                    '</form>';
                
                // $item_ul.find(".title").prepend($item_html);
                $item_ul.find(".price").after($item_html);
                $item_form.trigger('reset');
            },
            error: function(request, errorType, errorMessage){
                alert("error:" +  errorType, + 'with message: ' + errorMessage);

                var error_msg = '';
            },
            timeout: 3000,
            beforeSend: function(){

            },
            complete: function(){

            },
            // contentType: 'application/json'
        });

    });


}); // End Document
// curl -X POST --data '{"title": "My Title"}' http://localhost:8000/api/v1/grocery_list/ -H "Content-Type: application/json"



function item_update($form, $method, redirect_url){
    console.log("I am in the item update function");
    console.log("method" + $method);

    var $grocery_list_id = $form.find("#id_quick_list").val();
    console.log("GID " + $grocery_list_id);
    var $url = "/quick_list/" + $grocery_list_id + "/items";
    console.log($form.serialize());

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $.cookie("csrftoken"));
            }
        }
    });

    $.ajax($url, {
        type: $method,
        // data: $('#list_form').serialize(),
        data:  $form.serialize(),
        dataType: 'json',
        success: function(response){
            console.log("success");
            $form.trigger('reset');
        },
        error: function(request, errorType, errorMessage){
            alert("error:" +  errorType, + 'with message: ' + errorMessage);

            var error_msg = '';
        },
        timeout: 3000,
        // beforeSend: function(){

        // },
        complete: function(){
            console.log("done");
            if (redirect_url){
                window.location.href = redirect_url;
            }
          
        },
        // contentType: 'application/json'

    });

};


function DeleteForm ($form){
    this.method = "DELETE";
    this.$form = $form;
    this.$url = "/";
}



