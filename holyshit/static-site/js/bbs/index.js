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
                $('#email_errors').html('');
                $('#message_errors').html('');
                if(data.errors)
                {
                    var errors = JSON.parse(data.errors);
                    if(errors.email)
                    {
                        var html = "<div class='alert alert-warning' role='alert'>"+ errors.email[0].message +"</div>";
                        $('#email_errors').append(html);

                    }

                    if(errors.message)
                    {
                        var html = "<div class='alert alert-warning' role='alert'>"+ errors.message[0].message +"</div>";
                        $('#message_errors').append(html);
                    }
                }
            }
        },
        'error':function(data){

            alert('服务器出错，请重新提交');
        },
        processData: false,
        contentType: false
    });
});

var thread_reply = function(pk, target)
{
  current_add_comment_thread = pk;
}

$('#add_thread_reply_button').click(function(){

    var message = $('#thread_reply_textarea').val();
    var target = $('#thread_reply_textarea').attr('action');

    $.ajax({
        url:target,
        type:'POST',
        data:{
            message:message,
            thread:current_add_comment_thread
        },
        'success':function(data){
            if(data.state)
            {
                window.location.reload(true);
            }
            else{
                var errors = JSON.parse(data.messages).message;
                var html = "<div class='alert alert-warning' role='alert'>"+ errors[0].message +"</div>";
                $('#thread_reply_errors').html(html);
            }
        },
        'error':function(data){

        }
    });
});

var thread_up = function(pk, target)
{
    $.ajax({
        url:target,
        type:'POST',
        data:{
            pk:pk
        },
        'success':function(data)
        {
        },
        'error':function(data)
        {

        }

    });
}

var thread_down = function(pk, target)
{
    $.ajax({
        url:target,
        type:'POST',
        data:{
            pk:pk
        },
        'success':function(data)
        {
        },
        'error':function(data)
        {

        }

    });
}

window.onload = function()
{
    $('#flow_box').masonry({
        columnWidth: 90,
        itemSelector: '.flow_item'
    });
}