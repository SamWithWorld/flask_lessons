// 解密
$(function () {

            $("#decrypt-btn").click(function(event){
                event.preventDefault();
                var self = $(this);
                var decryptE = $("input[name=decrypt_text]");
                var decrypt_text = decryptE.val();
                // alert('Success ~');

                var csrftoken = $('meta[name=csrf-token]').attr('content')

                $.ajaxSetup({
                    beforeSend: function(xhr, settings) {
                        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                            xhr.setRequestHeader("X-CSRFToken", csrftoken)
                        }
                    }
                })

                $.post({
                    'url':'/decrypt_encrypt/',
                    'data':{
                        'decrypt_text':decrypt_text
                    },
                    'success':function(data){
                        if(data['code']==200){
                            console.log(data);
                            // alert('Success fully ~');
                            //<h3 style="color:red;display:inline"> {{ data['result'].strip() }}</h3>
                            $("#message-p").html('解密结果：<h3 style="color:red;display:inline">'+ data['result']);
                            $("#message-p").show();
                            // window.location.reload();
                            // document.getElementById("message-p").style.display="block";
                        }
                        else{
                            console.log(data);
                            var message = data['message'];
                            $('#message-p').html(message);
                            $('#message-p').show();
                        }
                        console.log(data);
                    },
                    'fail': function(error) {
                        console.log(error);
                    }
                })

            });
            $("#encrypt-btn").click(function(event){
                event.preventDefault();
                var self = $(this);
                var encryptE = $("input[name=vault_text]");
                var vault_text = encryptE.val();
                // alert('Success ~');
                var csrftoken = $('meta[name=csrf-token]').attr('content')

                $.ajaxSetup({
                    beforeSend: function(xhr, settings) {
                        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                            xhr.setRequestHeader("X-CSRFToken", csrftoken)
                        }
                    }
                })
                $.post({
                    'url':'/en/',
                    'data':{
                        'vault_text':vault_text
                    },
                    'success':function(data){
                        if(data['code']==200){
                            console.log(data);
                            // alert('Success fully ~');
                            $("#encrypt-message-p").html('加密结果：'+ data['result']);
                            $("#encrypt-message-p").show();
                            // window.location.reload();
                            // document.getElementById("message-p").style.display="block";
                        }
                        else{
                            console.log(data);
                            var message = data['message'];
                            $('#encrypt-message-p').html(message);
                            $('#encrypt-message-p').show();
                        }
                        console.log(data);
                    },
                    'fail': function(error) {
                        console.log(error);
                    }
                })

            });

});

//加密
// $(function () {
//
//             $("#encrypt-btn").click(function(event){
//                 event.preventDefault();
//                 var self = $(this);
//                 var encryptE = $("input[name=encrypt_text]");
//                 var encrypt_text = encryptE.val();
//                 // alert('Success ~');
//                 $.post({
//                     'url':'/de/',
//                     'data':{
//                         'encrypt_text':encrypt_text
//                     },
//                     'success':function(data){
//                         if(data['code']==200){
//                             console.log(data);
//                             alert('Success fully ~');
//                             $("#encrypt-message-p").html('加密结果：'+ data['result']);
//                             $("#encrypt-message-p").show();
//                             // window.location.reload();
//                             // document.getElementById("message-p").style.display="block";
//                         }
//                         else{
//                             console.log(data);
//                             var message = data['message'];
//                             $('#encrypt-message-p').html(message);
//                             $('#encrypt-message-p').show();
//                         }
//                         console.log(data);
//                     },
//                     'fail': function(error) {
//                         console.log(error);
//                     }
//                 })
//
//             });
//
// });