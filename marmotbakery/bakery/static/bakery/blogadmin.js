document.addEventListener('DOMContentLoaded', () => {
    //create content area
    
    if (document.querySelector('.number')){
        var total= document.querySelectorAll('.number').length;
        elementcounter=document.querySelectorAll('.number')[total-1].innerHTML;
    }
    else{elementcounter = 0;}
    
    //upload content
    document.querySelector('.contentbutton').addEventListener('click', () => {
        elementcounter= parseInt(elementcounter)+1;
        var textarea = document.createElement('textarea');
        textarea.style.resize = "vertical";
        textarea.className = "contentblock";
        textarea.id = elementcounter;
        textarea.style.width = "100%";
        textarea.style.marginBottom = "10px";
        var element = document.createElement("p");
        element.innerHTML = elementcounter;
        element.className = "number";

        
        document.querySelector('.create').insertBefore(element, document.querySelector('.last'))
        document.querySelector('.create').insertBefore(textarea, document.querySelector('.last'))
    })

    // upload image
    document.querySelector('.imagebutton').addEventListener('click', () => {
        saveData();
        var blogid = document.getElementById('blogid').innerHTML;
        window.location = `/fileupload/${blogid}`;
    })
    // save
    document.querySelector('#save').addEventListener('click', () => {
        saveData();
        document.querySelector('#post').disabled = false;
    })

    //post
    document.querySelector('#post').addEventListener('click', () => {
        
        var blogid = document.getElementById('blogid').innerHTML;
        fetch(`createblog/${blogid}`,
            {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    "X-CSRFToken": getCookie("csrftoken"),
                    
                },
           })
           .then(response => window.location.assign("blog") )
        
            
       
    })


})

function saveData(){
// preparefor fetch
var blogid = document.getElementById('blogid').innerHTML;

// fetch to database to store data before file upload
var contentdict = {};
contentdict[0] = document.getElementById('title').value;
document.querySelectorAll('.contentblock').forEach((block) => {
    contentdict[block.id] = block.value;
})
console.log(contentdict)
fetch(`contententry/${blogid}`,
    {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            "X-CSRFToken": getCookie("csrftoken"),
            
        },
        body:JSON.stringify(contentdict),
        
        
    })
}

// function getCookie
// taken from stackoverflow
// url: https://stackoverflow.com/questions/10730362/get-cookie-by-name
//
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}