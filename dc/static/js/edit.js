$(document).ready(function () {
    var $question_list=$(".question_list");
    // 添加问题
    $(".add").on("click", function () {
    var num = $(".question").length + 1;
    var naire_id = $("#naire_id").attr("naire_id");
    var question = '<div class="form-group">\n' +
        '                                <label for="" class="col-sm-2 control-label">问题</label>\n' +
        '                                <div class="col-sm-6">\n' +
        '                                    <textarea name="title" class="form-control"\n' +
        '                                              id="id_question"></textarea></div></div>';
    var type = '<div class="form-group">\n' +
        '                                <label for="" class="col-sm-2 control-label">类型</label>\n' +
        '                                <div class="col-sm-3">\n' +
        '                                    <select name="type" class="form-control type" id="id_type">\n' +
        '                                        <option selected value="1">评分</option>\n' +
        '                                        <option value="2">描述</option>\n' +
        '                                        <option value="3">单选</option>\n' +
        '                                    </select>' +
        ''
        +'</div><a role="button" class="hide option"><span class="glyphicon glyphicon-plus"></span><span>添加选项</span></a></div>';
    var info = '<div class="question" question_id="'+Math.random()*10000+'">\n' +
        '                        <div>\n' +
        '                            <span class="text-left question_num" style="opacity: 10">问题' + num + '</span>\n' +
        '                            <a class="pull-right del_question"><span\n' +
        '                                    class="glyphicon glyphicon-remove text-right"></span></a>\n' +
        '                        </div>\n' +
        '                        <form class="form-horizontal" >' + question + type + '</form><div style="margin-left: 260px"><form class="form-inline" action="/dc/edit/naire/'+naire_id +'" method="post"><ul></ul></form></div></div>';
    $(".question_list").append(info);
});
    // 删除问题
    $question_list.on("click", "a.del_question", function () {
        $(this).parent().parent().remove();
        question_index()
    });
    // 添加单选按钮
    $question_list.on("change", ".type", function () {
        if ($(this).val() === "3") {
            $(this).parent().next().removeClass("hide")
        }
        else {
            $(this).parent().next().addClass("hide")
        }
    });
    // 添加单选选项
    $question_list.on("click", ".option", function () {
        var naire_id = $("#naire_id").attr("naire_id");
        // alert(123);
        var li = '<li class="option-item" option_id="'+Math.random()*10000+'"><div class="form-group">\n' +
            '               <label for="">内容</label>\n' +
            '               <input name="name" type="text" class="form-control 1">\n' +
            '            </div>\n' +
            '            <div class="form-group">\n' +
            '                <label for="">分值</label>\n' +
            '                <input name="score" type="text" class="form-control">\n' +
            '            </div>\n' +
            '            <a class="del_option"><span class="glyphicon glyphicon-remove"></span></a>\n' +
            '</li>';
        // console.log($(this).next());
        // console.log(li);
        $(this).parent().parent().next().children().children().append(li);
    });
    // 删除单选选项
    $question_list.on("click",".del_option",function () {
       $(this).parent().remove()
    });
    // 重新排序
    function question_index() {
        $(".question").each(function (i,j) {
            $(j).find(".question_num").html("问题"+(i+1))
        })
    }
    // 保存按钮
    $("#save").on("click",function () {
        var naire_id = $("#naire_id").attr("naire_id");
        var post_data=get_post_data();
        console.log(post_data);
        $.ajax({
            url:'/dc/edit/question/'+naire_id,
            type:"post",
            data:JSON.stringify(post_data),
            headers:{"X-CSRFToken":$.cookie("csrftoken")},
            contentType:"application/json",
            success:function (data) {
                console.log(data);
                location.href="/dc/index";
            }
        })
    });

    function get_post_data() {
        var post_list=[];
        $(".question").each(function (i,j) {
            var question_id=parseInt($(this).attr("question_id"));
            var question_title=$(this).find("[name=title]").val();
            var question_type=parseInt($(this).find("[name=type]").val());

            var post_option_list=[];
            if (question_type===3){
                $(this).find(".option-item").each(function (i,j) {
                    console.log("hello");
                    var option_id=parseInt($(this).attr("option_id"));
                    var option_name=$(this).find("[name='name']").val();
                    var option_score=parseInt($(this).find("[name='score']").val());
                    var option_dict={"nid":option_id,"name":option_name,"score":option_score};
                    post_option_list.push(option_dict);
                })
            }
            var post_question_dict={"nid":question_id,"title":question_title,"type":question_type,"option_list":post_option_list};
            post_list.push(post_question_dict);


        });
        return post_list
    }
});