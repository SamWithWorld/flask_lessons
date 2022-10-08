$(function (){
    $('#clear').click(function (event){
        event.preventDefault();
        var parentNode = document.getElementById('log-container');
        parentNode.innerHTML = "";

        // var envE = $('select[name="env"]');
        // var groupE = $('select[name="group"]');
        // var roleE = $('select[name="role"]');
        // var phoneE = $('input[name="phone"]');
        //
        // var env = envE.val();
        // var group = groupE.val();
        // var role = roleE.val();
        // var phone = phoneE.val();
        // if (!phone){
        //     zlalert.alertError("请输入手机号");
        //     return;
        // };
        // zlajax.post({
        //     'url':"/usergroup/",
        //     'data':{
        //         "env":env,
        //         "group":group,
        //         "role":role,
        //         "phone":phone
        //     },
        //     'success':function (data){
        //         if (data['code'] == 200){
        //             zlalert.alertToast(msg="设置分流规则成功",type="success", timer=2000);
        //         }else{
        //             // window.location.reload();
        //             zlalert.alertError(data["message"]);
        //
        //         }
        //     },
        //     'fail':function (data){
        //             zlalert.alertInfo("设置分流规则失败");
        //     }
        //
        // });

    });
});