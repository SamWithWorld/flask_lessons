$(function (){
    $('.copy-link').click(function(){
        var clipboard = new ClipboardJS('.copy-link');
        clipboard.on('success', function(e) {
        console.log(e);
        alert('复制成功');
        });
        clipboard.on('error', function(e) {
                    console.log(e);

        alert('复制失败e');
        });
        });
});


