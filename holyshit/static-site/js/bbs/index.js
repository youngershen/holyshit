/**
 * Created by youngershen on 15-1-22.
 */

$("#add_post_button").click(function(){

    var target = $('#add_post_box_form').attr('action');
    var form = new FormData(document.getElementById('add_post_box_form'));
    $.ajax({
        type  :'POST',
        'url' : target,
        contentType: "application/x-www-form-urlencoded",
        data:form,
        'success':function(data){

            console.log(data);
        },
        'error':function(data){

        },
        processData: false,
        contentType: false
    });
});
