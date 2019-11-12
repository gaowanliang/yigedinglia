function splitFileName(text) {
    var pattern = /\.{1}[a-z]{1,}$/;
    if (pattern.exec(text) !== null) {
        return (text.slice(0, pattern.exec(text).index));
    } else {
        return text;
    }
}



function appendFile(files) {
    if (files.length < 2) {
        for (file of files) {
            if (file.type == "text/plain") {
                post(files)
                var k = splitFileName(file["name"])
                console.log(k, file["name"])
                $('#qq').html("题库 " + k + " 已载入")
            } else {
                alert("现阶段只能上传txt文件")
            }
        }
    } else {
        alert("一次只能上传一个题库")
    }

}

function upload(token) {
    if (token.length != 0) {
        if (gwl.length) {
            var formData = new FormData($('#uploadForm')[0]);
            formData.append('token', token);
            $.ajax({
                url: document.URL,
                type: "POST",
                data: formData,
                async: true,
                cashe: false,
                contentType: false,
                processData: false,
                success: function(returndata) {
                    alert(returndata)
                    location.replace(document.URL)
                }
            })
        } else {
            alert("你还没上传文件呢")
        }
    } else {
        alert("你还没进行reCAPTCHA的验证呢")
    }

}


function getNum() {
    var chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    var nums = "";
    for (var i = 0; i < 32; i++) {
        var id = parseInt(Math.random() * 61);
        nums += chars[id];
    }
    return nums;
}