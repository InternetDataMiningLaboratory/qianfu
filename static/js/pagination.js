$(document).ready(function(){
    $("ul.pagination").each(function(){
        page(1, $(this));
    })
});
$("ul.pagination li.pages").click(function(){
    page($(this).text(), $(this).parent());
});
function page(index, pagination){
    refreshPageData(pagination.attr("name"), index, pagination);
}
$("ul.pagination li.page-formal").click(function(){
    var activeIndex = parseInt($(this).siblings(".active").text());
    page(activeIndex-1, $(this).parent());
});
$("ul.pagination li.page-next").click(function(){
    var activeIndex = parseInt($(this).siblings(".active").text());
    page(activeIndex+1, $(this).parent());
});
function selectPage(index, pagination){
    //转换index
    index = parseInt(index);
    //获取数据来源
    var pageSrc = pagination.attr("name");
    //获取页码总数
    var pageNum = pagination.data("pages");

    //重置所有页码
    pagesReset(pagination);
    var pages = pagination.children(".pages");

    //从前往后填充页码
    var startPage = 1;
    var pageIndex = 0;
    //点选页码大于4 左端省略号出现，从index-2开始填充页码
    if(index > 4){
        startPage = index - 2;
        pageIndex = 1;
        if(index == 5){
            pageIndex = 2;
            renderPage(pages.eq(1), 2);
        }
        else{
            pagination.children(".left-ellipsis").css("display", "inline");    
        }
        renderPage(pages.first(), 1);
    }
    //从1开始向后填充至index
    for(;startPage<index;pageIndex++,startPage++){
        renderPage(pages.eq(pageIndex), startPage);
    }

    //从后向前填充页码
    startPage = pageNum;
    pageIndex = 8;

    //点选页码小于pageNum-2，右端省略号显示，从index+2开始填充页码
    if(index + 3 < pageNum){
        startPage = index + 2;
        pageIndex = 7;
        if(index + 4 == pageNum){
            pageIndex = 6;
            renderPage(pages.eq(7), index+3);     
        }
        else{
            pagination.children(".right-ellipsis").css("display", "inline");
        }
        renderPage(pages.last(), pageNum);
    }
    var selectPage = pageIndex - startPage + index;
    //从pageNum开始向前填充页码
    for(;startPage>=index;pageIndex--,startPage--){
        renderPage(pages.eq(pageIndex), startPage);
    }
    pages.filter(".active").removeClass("active");
    pages.eq(selectPage).addClass("active");
}

//重置页码状态
function pagesReset(pagination){
    //所有页码隐藏
    var pages = pagination.children(".pages");
    pages.each(function(){$(this).css("display", "none");});
    //左右省略号隐藏
    pagination.children(".left-ellipsis").css("display", "none");    
    pagination.children(".right-ellipsis").css("display", "none");    
}

//填充页码
function renderPage(page, text){
    page.children().first().text(text);
    page.css("display", "inline");
}
//更新页面数据
function refreshPageData(name, index, pages){
    $.post(
        '/pagination/'+name,
        {
            index: index,    
            _xsrf: getCookie("_xsrf"), 
        },
        function(data){
            if(data=="failed"){
                alert("请求数据失败");
            }
            else{
                var paginationId = name.substring(0, 1).toUpperCase() + name.substring(1).toLowerCase();
                var pagination = $('#Pagination'+paginationId);
                var pageNum = parseInt(data["page_num"]);
                pages.data("pages", pageNum);
                pagination.html(data["data"]);
                selectPage(index, pages);
            } 
        }
    );
}
