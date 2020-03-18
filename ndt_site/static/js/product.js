const featureImage = document.querySelector(".product-featured-image .active");
const thumbnailImages = document.querySelectorAll(".image-list img");

function changeImage(e) {
    featureImage.src = e.target.src;
}

thumbnailImages.forEach(image => image.addEventListener('click', changeImage));

document.on('click', 'lighted', function(){

});

$(document).ready(function() {

    //adds oipacity and border to selected colors
    $(document).on('click', 'img', function(){
        $(this).addClass('focus').siblings().removeClass('focus');
        $(this).siblings().addClass('opace');
        $(this).removeClass('opace');
    });

    //removes the hidden class from colors to diplat color choices
    $('select#finish').change(function(){
        var selectedFinish = $(this).children('option:selected').val();
        // alert("this selection is " + selectedFinish);
        if (selectedFinish === "powdercoated") {
            // alert("this is " + selectedFinish);
            $('div.product-detail-color').removeClass('hidden');
        }
        else {
            $('div.product-detail-color').addClass('hidden');
        }
    });


});