$(function (){
    $('#add-user-coin').click(function (event){
        event.preventDefault();
        var envE = $('select[name="env"]');
        var phoneE = $('input[name="phone"]');
        var coinE = $('select[name="coin"]');

        var env = envE.val();
        var phone = phoneE.val();
        var coin = coinE.val();

        if (!phone){
            zlalert.alertError("请输入手机号");
            return;
        };
        zlajax.post({
            'url':"/coin/",
            'data':{
                "env":env,
                "phone":phone,
                "coin":coin
            },
            'success':function (data){
                if (data['code'] == 200){
                    zlalert.alertToast(msg=data["message"],type="success");
                }else{
                    // window.location.reload();
                    zlalert.alertError("修改洋葱币失败");

                }
            },
            'fail':function (data){
                    zlalert.alertInfo("修改洋葱币失败");
            }

        });

    });
});