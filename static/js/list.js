$(document).ready(function(){
    LoadingMoreViaPost();
});
$('#LoadingMore').click(function(){
    LoadingMoreViaPost();
});
function LoadingMoreViaPost(){
    var loadingMore = $('#LoadingMore');
    var loadTimes = loadingMore.data('load');
    loadingMore.text('正在加载中...');
    $.post(
        '#',
        {
            load_times : loadTimes, 
            _xsrf : getCookie("_xsrf"),
        },
        function(data){
            var loadingMore = $('#LoadingMore')
            if(data=="failed"){
                loadingMore.text('加载失败');                
                loadingMore.addclass('disable');                
            }
            else if(data=="-1"){
                loadingMore.text('全部加载完毕');
                loadingMore.fadeOut();
            }
            else{
                var last = $("ul.list-group").children('a').last();
                var template = last.clone();
                template.removeClass('template');
                for(var stockItem in data["data"]){
                    var stockItem = data["data"][stockItem];
                    var newItem = template.clone();
                    newItem.attr('href', '/info/000001');
                    var code = newItem.children().children().first();
                    code.html(stockItem[1]);
                    var name = code.next();
                    name.html(stockItem[2]);
                    var score = name.next();
                    score.html(stockItem[3]);
                    var index = score.next();
                    index.html(stockItem[0]);
                    last.after(newItem);
                    last = newItem;
                }
                loadingMore.data('load', loadTimes+1);
                loadingMore.text('加载更多');
            }
        } 
    );
}
