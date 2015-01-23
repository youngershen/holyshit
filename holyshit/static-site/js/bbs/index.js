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

            if(data.state)
            {
                window.location.reload(true);

            }else{

            }
        },
        'error':function(data){

            alert('服务器出错，请重新提交');
        },
        processData: false,
        contentType: false
    });
});
