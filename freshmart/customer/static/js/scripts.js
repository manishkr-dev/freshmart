// <!-- ----Custom-js---- -->
$(document).ready(function () {
    // ----banner-slider
    var owl = $("#banner-slider")
    owl.owlCarousel({
        loop: false,
        margin: 14,
        nav: false,
        dots: false,
        autoplay: false,
        autoplayTimerout: 2000,
        responsive: {
            0: {
                items: 1
            },
            375: {
                items: 2
            },
            600: {
                items: 2
            },
            960: {
                items: 4
            },
            1200: {
                items: 4
            }
        }
    })
    //Category-slider
    var owl = $("#cat-slider")
    owl.owlCarousel({
        loop: true,
        margin: 14,
        nav: false,
        dots: false,
        autoplay: true,
        autoplayTimerout: 2000,
        responsive: {
            0: {
                items: 1
            },
            375: {
                items: 2
            },
            576: {
                items: 3
            },
            960: {
                items: 4
            },
            1200: {
                items: 6
            }
        }
    })
    //product-slider
    var owl = $("#product-slider")
    owl.owlCarousel({
        loop: false,
        margin: 14,
        nav: false,
        dots: false,
        autoplay: true,
        autoplayTimerout: 1000,
        responsive: {
            0: {
                items: 1
            },
            375: {
                items: 2
            },
            576: {
                items: 3
            },
            960: {
                items: 4
            },
            1200: {
                items: 6
            }
        }
    })
    var owl = $("#adv-slider")
    owl.owlCarousel({
        loop: false,
        margin: 14,
        nav: false,
        dots: false,
        autoplay: true,
        autoplayTimerout: 1000,
        responsive: {
            0: {
                items: 1
            },
            375: {
                items: 2
            },
            576: {
                items: 3
            },
            960: {
                items: 4
            },
            1200: {
                items: 5
            }
        }
    })

    //simple login-function
    $(".register").hide();
    $("body").on("click", ".regist", function () {
        $(".register").show();
        $(".login").hide();
        $(".login-heading").html("Registration");
    })
    $("body").on("click", ".go-back", function () {
        $(".register").hide();
        $(".login").show();
        $(".login-heading").html("Login");
    })
    // Handle the click event on the "Add" button
    $(".product-add").on("click", function (e) {
        e.preventDefault();
        $(this).hide();
        $(this).siblings(".qty-items-count").addClass("d-flex").show();
        $(this).siblings(".qty-items-count").find(".qty-count").text(1);
        $(".fm-toast").animate({
            bottom: '20px'
        }, 400);

        // Hiding the toast after 3 seconds
        setTimeout(function () {
            $(".fm-toast").animate({
                bottom: '-100px'
            }, 400);
        }, 2000);
    });


    $(document).on("click", ".qnt-plus", function () {
        let qty = parseInt($(this).siblings(".qty-count").text());
        $(this).siblings(".qty-count").text(qty + 1);
        updateCartTotals();
    });

    $(document).on("click", ".qnt-minus", function () {
        let qty = parseInt($(this).siblings(".qty-count").text());
        if (qty > 1) {
            $(this).siblings(".qty-count").text(qty - 1);
        } else {
            $(this).closest(".qty-items-count").removeClass("d-flex").hide();
            $(this).closest(".card-footer").find(".product-add").show();
        }
        updateCartTotals();
    });

    // -----wishlist heart js 
    $(".product-card-wish").on("click", function () {
        $(this).find("i").removeClass("fa-regular").addClass("fa-solid red-heart");
    });

    // -----Toggle dropdown 
    $(".num-count-btn img").on("click", function () {
        $("#subMenu").toggleClass("open-menu");
    });

    // -----discount badge js
    var originalPrice = parseInt($('.original-price').text().replace('₹', '').replace(',', ''));
    var currentPrice = parseInt($('.current-price').text().replace('₹', '').replace(',', ''));
    var discountPercentage = Math.round(((originalPrice - currentPrice) / originalPrice) * 100);
    $('.discount-badge').text(discountPercentage + '% OFF');

    updateCartItemCount();
    updateCartTotals();

    // Handle thumbnail click
    $('.thumbnail').click(function () {
        $('.thumbnail').removeClass('active');
        $(this).addClass('active');
        var clickedImageSrc = $(this).attr('src');
        $('#mainImage').attr('src', clickedImageSrc);
    });

    // Function to update cart item count
    function updateCartItemCount() {
        var itemCount = $('.product-cart').length;
        $('#cart-item-count').text('(' + itemCount + ' Items)');
    }

    // Function to update cart totals
    function updateCartTotals() {
        var mrpTotal = 0;
        var discountTotal = 0;
        var currentTotal = 0;

        $('.product-cart').each(function () {
            // Get the current price
            var currentPriceText = $(this).find('.product-price').text().replace('₹', '').trim();
            var currentPrice = parseFloat(currentPriceText);

            // Get the original price (MRP)
            var originalPriceText = $(this).find('.product-price del').text().replace('₹', '').trim();
            var originalPrice = parseFloat(originalPriceText);

            // // Get the quantity
            // var quantity = parseInt($(this).find('.qty-count').text().trim());
            // Get the quantity, extracting only the numeric part
            var quantity = parseInt($(this).find('.qty-count').text().trim().match(/\d+/)[0]);


            // Calculate MRP total and discount total
            mrpTotal += originalPrice * quantity;
            discountTotal += (originalPrice - currentPrice) * quantity;

            // Update the current total
            currentTotal += currentPrice * quantity;
        });

        // Calculate order total
        var orderTotal = mrpTotal - discountTotal;

        $('#cart-total').text('₹' + mrpTotal.toFixed(2));
        $('#cart-discount').text('- ₹' + discountTotal.toFixed(2));
        $('#order-total').text('₹' + orderTotal.toFixed(2));
    }

    // Delete functionality (modal) handled here
    let productToDelete;

    $(document).on("click", ".delete", function () {
        productToDelete = $(this).closest(".product-cart");
        $("#deleteModalLabel").text("Confirm Deletion");
        $(".modal-body").html("Are you sure you want to delete this product?");
        $("#confirmDelete").show();
        $("#deleteModal").modal('show');
    });

    $(document).on("click", "#confirmDelete", function () {
        if (productToDelete) {
            productToDelete.remove();
            $(".modal-body").html("<p class='text-success fw-bold m-0'>Product has been removed from your cart.</p>");
            $("#deleteModalLabel").text("Product Removed");
            $("#confirmDelete").hide();
            setTimeout(function () {
                $("#deleteModal").modal('hide');
            }, 2000);

            updateCartItemCount();
            updateCartTotals();

            productToDelete = null;
        }
    });

    var successModal = new bootstrap.Modal(document.getElementById('successModal'));

    $('.checkout-btn').click(function () {
        successModal.show();
        var audio = document.getElementById('checkout-sound');
        audio.play();

        $('.container-fluid').addClass('blur-effect');

        $('body').css({
            'overflow': 'visible',
            'padding-right': '0'
        });
    });

    document.getElementById('successModal').addEventListener('show.bs.modal', function (event) {
        setTimeout(function () {
            successModal.hide();
            var audio = document.getElementById('checkout-sound');
            audio.pause();
            audio.currentTime = 0;
            window.location.href = 'my-account.html';
        }, 200000);
    });

    document.getElementById('successModal').addEventListener('hide.bs.modal', function (event) {
        $('.container-fluid').removeClass('blur-effect');
    });

    // $(document).on('click', '.tab-link', function (e) {
    //     e.preventDefault(); // Prevent default link behavior
    //     var target = $(this).data('target'); // Get the target tab content ID
    //     $('.tab-pane').removeClass('show active'); // Remove active classes from all tabs
    //     $(target).addClass('show active'); // Add active classes to the target tab
    // });
   

    

});
