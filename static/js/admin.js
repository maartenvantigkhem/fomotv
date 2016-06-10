var discountFunc = function() {

    var discount = django.jQuery('#id_discount_amount').val() * django.jQuery('#id_retail_price').val()/ 100;
    var sale_price = django.jQuery('#id_retail_price').val() - discount;

    if(sale_price > 0) {
        sale_price = Number((sale_price).toFixed(0));
        django.jQuery('#id_sale_price').val(sale_price);
    }
    else {
        django.jQuery('#id_sale_price').val(0);
    }

};

django.jQuery(document).ready(function(e) {

    django.jQuery('#id_discount_amount, #id_retail_price').keyup(discountFunc);
    django.jQuery('#id_discount_amount, #id_retail_price').change(discountFunc);

    django.jQuery(".grp-filter-choice").change(function(){location.href=django.jQuery(this).val()});

});