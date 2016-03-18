$('#LoadingMore').click(function(){
    var loadTimes = $(this).data('load');
    $.post(
        '#',
        {
            load_times : loadTimes, 
            _xsrf : getCookie("_xsrf"),
        },
        function(data){
            var loadingMore = $('#LoadingMore')
            if(data=="failed"){
                loadingMore.html('加载失败');                
                loadingMore.addclass('disable');                
            }
            else if(data=="-1"){
                loadingMore.css('display', 'none');
            }
            else{
                var last = $("ul.list-group").children('a').last();
                var template = last.clone();
                for(var stockItem in data["data"]){
                    var stockItem = data["data"][stockItem];
                    var newItem = template.clone();
                    newItem.attr('href', '/info/000001');
                    var index = newItem.children().children().first();
                    index.html(stockItem[0]);
                    var code = index.next();
                    code.html(stockItem[1]);
                    var name = code.next();
                    name.html(stockItem[2]);
                    var score = name.next();
                    score.html(stockItem[3]);
                    last.after(newItem);
                    last = newItem;
                }
                loadingMore.data('load', loadTimes+1);
            }
        } 
    );
});
