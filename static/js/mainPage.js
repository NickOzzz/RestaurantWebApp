function setItemCookie(name, description, price, imageUrl, itemId){
       let uuid = generateUUIDUsingMathRandom();
       setCookie("itemName" + uuid, name, 1);
       setCookie("itemDescription" + uuid, description, 1);
       setCookie("itemPrice" + uuid, price, 1);
       setCookie("imageUrl" + uuid, imageUrl, 1);
       setCookie("itemId" + uuid, itemId, 1);
       updateCashierCounter();
}

function updateCashierCounter(){
       let counterNumber = (Number(document.getElementById("title-cart-counter").innerHTML) + 1).toString();
       document.getElementById("title-cart-counter").innerHTML = counterNumber;
}

function setCookie(cName, cValue, expDays) {
        let date = new Date();
        date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();
        document.cookie = cName + "=" + cValue + "; " + expires + "; path=/";
}

function initApp(foodBox1Count, foodBox2Count, foodBox3Count, foodBox4Count, spacingBox2, spacingBox3, spacingBox4){
        setFoodBoxesPositionAdjustmentInterval(
                           foodBox1Count, foodBox2Count, foodBox3Count,
                           foodBox4Count, spacingBox2, spacingBox3, spacingBox4);
        setIntroImageRotation();
        setCookieCounter();
}

function setFoodBoxesPositionAdjustmentInterval(
                foodBox1Count, foodBox2Count, foodBox3Count, foodBox4Count,
                                    spacingBox2, spacingBox3, spacingBox4){

        setUpFoodBoxesPositions(foodBox1Count, foodBox2Count, foodBox3Count,
                                foodBox4Count, parseInt(spacingBox2), parseInt(spacingBox3), parseInt(spacingBox4));
        setInterval(() => {
               setUpFoodBoxesPositions(foodBox1Count, foodBox2Count, foodBox3Count,
               foodBox4Count, parseInt(spacingBox2), parseInt(spacingBox3), parseInt(spacingBox4));
        }, "500")
}

function setIntroImageRotation(){
        intro_images = [
        "static/assets/shashlik-intro2.png",
        "static/assets/shashlik-intro3.png",
        "static/assets/shashlik-intro.png"
        ]
        intro_image_counter = 0

        setInterval(() => {
        changeIntroImage(intro_images[intro_image_counter]);
        intro_image_counter++;

        if (intro_image_counter == 3){
        intro_image_counter = 0;
        }
        }, 5000);
}

function changeIntroImage(image_name){
       document.getElementById("intro-img").src = image_name;
}

function setUpFoodBoxesPositions(foodBox1Count, foodBox2Count, foodBox3Count,
                                 foodBox4Count, spacingBox2, spacingBox3, spacingBox4){

       var informationBoxAdditionalPositioning = parseInt(foodBox4Count) * 7;

       setUpFoodBoxPosition(1, 2, foodBox1Count, position, spacingBox2);
       setUpFoodBoxPosition(2, 3, foodBox2Count, position, spacingBox3);
       setUpFoodBoxPosition(3, 4, foodBox3Count, position, spacingBox4);

       if (parseInt(foodBox4Count) != 0){
           var heightOfFoodCards = parseInt($("#food-card").css("height").split("p")[0]);
           var heightOfFoodSectionHolders = parseInt($("#food-section-holder4").css("height").split("p")[0]);
           var position = heightOfFoodCards + heightOfFoodSectionHolders;

           $("#information-box")
               .css("top", (parseInt($("#food-box4")
               .css("top")) + informationBoxAdditionalPositioning + parseInt(foodBox4Count) * position).toString() + "px");
       }
}

function setUpFoodBoxPosition(comparisonBox, boxToAdjust, boxCount, position, spacing){
       var boxAdditionalPositioning = parseInt(boxCount) * spacing;

       if (parseInt(boxCount) != 0){
           var heightOfFoodCards = parseInt($("#food-card").css("height").split("p")[0]);
           var heightOfFoodSectionHolders = parseInt($("#food-section-holder" + comparisonBox.toString())
                                                                                .css("height").split("p")[0]);
           var position = heightOfFoodCards + heightOfFoodSectionHolders;

           $("#food-box" + boxToAdjust.toString())
               .css("top", (parseInt($("#food-box" + comparisonBox.toString())
               .css("top").split("p")[0]) + boxAdditionalPositioning + parseInt(boxCount) * position).toString() + "px");

           $("#food-section-holder" + boxToAdjust.toString())
               .css("top", (parseInt($("#food-section-holder" + comparisonBox.toString())
               .css("top").split("p")[0]) + boxAdditionalPositioning + parseInt(boxCount) * position).toString() + "px");
       }
}

function setCookieCounter(){
        var counter = 0;
        for (var cookie of document.cookie.split(";")){
                if (cookie.includes("itemId")){
                     counter++;
                }
                document.getElementById("title-cart-counter").innerHTML = counter.toString();
        }
}

function getCookie(name) {
        var dc = document.cookie;
        var prefix = name + "=";
        var begin = dc.indexOf("; " + prefix);
        if (begin == -1) {
            begin = dc.indexOf(prefix);
            if (begin != 0) return null;
        }
        else
        {
            begin += 2;
            var end = document.cookie.indexOf(";", begin);
            if (end == -1) {
                end = dc.length;
            }
        }
        return decodeURI(dc.substring(begin + prefix.length, end));
}

function generateUUIDUsingMathRandom() {
        var d = new Date().getTime();
        var d2 = (performance && performance.now && (performance.now()*1000)) || 0;
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
            var r = Math.random() * 16;
            if(d > 0){
                r = (d + r)%16 | 0;
                d = Math.floor(d/16);
            } else {
                r = (d2 + r)%16 | 0;
                d2 = Math.floor(d2/16);
            }
            return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
}

//Scroll to Shashlik na ugliach on button press
$("#choice1").click(function()
    {
    var myElement = document.getElementById('food-section-holder1');
    var topPos = (myElement.offsetTop - myElement.offsetHeight) - 40;
        $("body,html").animate(
        {
            scrollTop : topPos
        }, 300);
    });

//Scroll to Assorti on button press
$("#choice2").click(function()
    {
    var myElement = document.getElementById('food-section-holder2');
    var topPos = (myElement.offsetTop - myElement.offsetHeight) - 40;
    $("body,html").animate(
        {
            scrollTop : topPos
        }, 300);
    });

//Scroll to Miasnoi assorti on button press
$("#choice3").click(function()
    {
        var myElement = document.getElementById('food-section-holder3');
    var topPos = (myElement.offsetTop - myElement.offsetHeight) - 40;
    $("body,html").animate(
        {
            scrollTop : topPos
        }, 300);
    });

//Scroll to Shawerma on button press
$("#choice4").click(function()
    {
     var myElement = document.getElementById('food-section-holder4');
    var topPos = (myElement.offsetTop - myElement.offsetHeight) - 40;
    $("body,html").animate(
        {
            scrollTop : topPos
        }, 300);
    });

//Scroll to Information on button press
$("#choice5").click(function()
    {
     var myElement = document.getElementById('information-box');
    var topPos = (myElement.offsetTop - myElement.offsetHeight) - 40;
    $("body,html").animate(
        {
            scrollTop : topPos
        }, 300);
    });