function setItemCookie(name, description, price, imageUrl, itemId){
var uuid = generateUUIDUsingMathRandom();
setCookie("itemName" + uuid, name, 1);
setCookie("itemDescription" + uuid, description, 1);
setCookie("itemPrice" + uuid, price, 1);
setCookie("imageUrl" + uuid, imageUrl, 1);
setCookie("itemId" + uuid, itemId, 1);
}

function setCookie(cName, cValue, expDays) {
        let date = new Date();
        date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();
        document.cookie = cName + "=" + cValue + "; " + expires + "; path=/";
}

function deleteCookie(token){
document.cookie = "itemName" + token + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
document.cookie = "itemDescription" + token + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
document.cookie = "itemPrice" + token + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
document.cookie = "imageUrl" + token + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
document.cookie = "itemId" + token + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
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

function onlyOne(checkbox) {
    var checkboxes = document.getElementsByName('check')
    checkboxes.forEach((item) => {
        if (item !== checkbox){
        item.checked = false;
        if (item.id === "check-delivery"){
        $("#delivery-price").css("visibility", "hidden")
        }else if(item.id === "check-self"){
        $("#delivery-price").css("visibility", "visible")
        }}else{
        item.checked = true;
        }
    })
}

function check(){
document.getElementById("check-delivery").checked = true;
}

function openPopup(){
$("#fading-bg").css("visibility", "visible");
var selfCheck = document.getElementById("check-self");
var deliveryCheck = document.getElementById("check-delivery");
if (selfCheck.checked){
$("#pop-up-confirmation-self").css("visibility", "visible");
$("#pop-up-confirmation-delivery").css("visibility", "hidden");
}else if (deliveryCheck.checked){
$("#pop-up-confirmation-delivery").css("visibility", "visible");
$("#pop-up-confirmation-self").css("visibility", "hidden");
}
}

function closePopUp(){
$("#fading-bg").css("visibility", "hidden");
$("#warning-message").css("visibility", "hidden");
$("#warning-message2").css("visibility", "hidden");
$("#pop-up-confirmation-delivery").css("visibility", "hidden");
$("#pop-up-confirmation-self").css("visibility", "hidden");
}

function checkFields(){
var name = document.getElementById("input-username");
var phone = document.getElementById("input-usephone");
var place = document.getElementById("input-useplace");
if (place && place.value && phone && phone.value && name && name.value){
document.getElementById("hidden-delivery").click();
}else{
$("#warning-message").css("visibility", "visible");
}
}

function checkFields2(){
var name = document.getElementById("input-username2");
var phone = document.getElementById("input-usephone2");
if (phone && phone.value && name && name.value){
document.getElementById("hidden-delivery2").click();
}else{
$("#warning-message2").css("visibility", "visible");
}
}