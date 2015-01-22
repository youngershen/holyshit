/**
 * Created by youngershen on 15-1-22.
 */

$("#add_post_button").click(function(){

    var target = $('#add_post_box_form').attr('action');
    var title = $('#add_post_box_title').val()
    var author = $('#add_post_box_author').val()
    var email = $('#add_post_box_email').val()
    $.ajax({
        type  :'POST',
        'url' : target,
        'data':{

        },
        'success':function(data){

        },
        'error':function(data){

        }

    });
});
