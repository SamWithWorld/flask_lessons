
// 对jquery的ajax的封装

'use strict';
var zlajax = {
	'get':function(args) {
		args['method'] = 'get';
		this.ajax(args);
	},
	'post':function(args) {
		args['method'] = 'post';
		this.ajax(args);
	},
	'ajax':function(args) {
		// 设置csrftoken
		this._ajaxSetup();
		$.ajax(args);
	},
	'_ajaxSetup': function() {
		$.ajaxSetup({
			'beforeSend':function(xhr,settings) {
				if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    var csrftoken = $('meta[name=csrf-token]').attr('content');
                    xhr.setRequestHeader("X-CSRFToken", csrftoken)
                }
			}
		});
	}
};


$(function () {
    $('.nav-list>li>a').click(function (event) {
        var that = $(this);
        if(that.children('a').attr('href') == '#'){
            event.preventDefault();
        }
        if(that.parent().hasClass('unfold')){
            that.parent().removeClass('unfold');
        }else{
            that.parent().addClass('unfold').siblings().removeClass('unfold');
        }
        console.log('coming....');
    });

    $('.nav-list a').mouseleave(function () {
        $(this).css('text-decoration','none');
    });

});

$(function () {
    var url = window.location.href;
    if(url.replace(/^http(s)?:\/\/[^/]+\/?/, '') == ""){
        var IndexLi = $('.index');
        IndexLi.addClass('active').siblings().removeClass('active');
    }else if(url.indexOf('userinfo') >= 0){
        var UserInfoLi = $('.userinfo');
        UserInfoLi.addClass('active').siblings().removeClass('active');
    }else if(url.indexOf('delredis') >= 0){
        var DelRedisLi = $('.delredis');
        DelRedisLi.addClass('active').siblings().removeClass('active');
    }else if(url.indexOf('usergroup') >= 0){
        var UsergroupLi = $('.usergroup');
        UsergroupLi.addClass('active').siblings().removeClass('active');
    }else if(url.indexOf('coin') >= 0){
        var CoinLi = $('.coin');
        CoinLi.addClass('active').siblings().removeClass('active');
    }else if(url.indexOf('realtime_log') >= 0){
        var RealTimeLogLi = $('.realtime_log');
        RealTimeLogLi.addClass('active').siblings().removeClass('active');
    }else if(url.indexOf('jenkins_job') >= 0){
        var jenkins_jobLi = $('.jenkins');
        jenkins_jobLi.addClass('active').siblings().removeClass('active');
    }else if(url.endsWith('vault/')){
        var profileLi = $('.profile-li');
        profileLi.siblings().removeClass('active');
        profileLi.children('.submenu').css('display','block');
        profileLi.children('.submenu').children().eq(0).addClass('active').siblings().removeClass('active');
    }else if(url.endsWith('decrypt/')){
        var profileLi = $('.profile-li');
        profileLi.siblings().removeClass('active');
        profileLi.children('.submenu').css('display','block');
        profileLi.children('.submenu').children().eq(1).addClass('active').siblings().removeClass('active');
    }else if(url.indexOf('decrypt_encrypt') >= 0){
        var profileLi = $('.profile-li');
        profileLi.siblings().removeClass('active');
        profileLi.children('.submenu').css('display','block');
        profileLi.children('.submenu').children().eq(2).addClass('active').siblings().removeClass('active');
    }



    // else if(url.indexOf('vault') >= 0){
    //     var VaultLi = $('.vault');
    //     VaultLi.addClass('active').siblings().removeClass('active');
    // }
    // else if(url.endsWith('decrypt/')){
    //     var DecryptLi = $('.decrypt');
    //     DecryptLi.addClass('active').siblings().removeClass('active');
    // }

    // else if(url.includes('decrypt_encrypt')){
    //     var Decrypt_EncryptLi = $('.decrypt_encrypt');
    //     Decrypt_EncryptLi.addClass('active').siblings().removeClass('active');
    // }

});
