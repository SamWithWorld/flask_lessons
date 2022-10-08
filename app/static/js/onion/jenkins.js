// 获取job状态
function get_job_status(queue_id,build_type,platform) {
    zlajax.post({
        'url':'/job_status/',
        'data': {
            'queue_id': queue_id,
            'build_type': build_type,
            'platform': platform
        },
        'success':function (data) {
            var buildNumber = data['data']['buildNumber']
            if(buildNumber) {
                // zlalert.alertToast(msg="更新Job状态成功",type="success", timer=2000);
                zlalert.alertSuccessWithTitle('恭喜~','更新Job %s 状态成功' % buildNumber)
                //重新加载当前页面
                window.location.reload();
            }
            console.log(arg);
            get_job_status(queue_id,build_type,platform);
        },
        'fail': function (data){
            zlalert.alertInfo("获取job状态");
        }
    });
}

$(function (){
    $('#build-job').click(function (event){
        event.preventDefault();
        var build_typeE = $('select[name="build_type"]');
        var platformE = $('select[name="platform"]');
        var branchE = $('input[name="branch"]');

        var build_type = build_typeE.val();
        var platform = platformE.val();
        var branch = branchE.val();
        var queue_id = ''
        if (platform !="IOS" && !branch){
            zlalert.alertError("请输入分支号");
            return;
        };
        zlajax.post({
            'url':"/jenkins_job/",
            'data':{
                "build_type":build_type,
                "platform":platform,
                "branch":branch
            },
            'success':function (data){
                if (data['code'] == 200){
                    var queue_id = data['datas']['queue_id']
                    zlalert.alertToast(msg="提交构建任务成功,请稍后再来",type="success", timer=2000);
                    get_job_status(queue_id,build_type,platform) // ajax版递归
                    //重新加载当前页面
                    // window.location.reload();

                }else{
                    // window.location.reload();
                    zlalert.alertError(data["message"]);

                }

            },
            'fail':function (data){
                    zlalert.alertInfo("提交构建任务失败");
            }

        });
     // get_job_status(queue_id,build_type,platform) // ajax版递归

    });
});

