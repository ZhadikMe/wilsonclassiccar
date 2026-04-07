var _____WB$wombat$assign$function_____=function(name){return (self._wb_wombat && self._wb_wombat.local_init && self._wb_wombat.local_init(name))||self[name];};if(!self.__WB_pmw){self.__WB_pmw=function(obj){this.__WB_source=obj;return this;}}{
let window = _____WB$wombat$assign$function_____("window");
let self = _____WB$wombat$assign$function_____("self");
let document = _____WB$wombat$assign$function_____("document");
let location = _____WB$wombat$assign$function_____("location");
let top = _____WB$wombat$assign$function_____("top");
let parent = _____WB$wombat$assign$function_____("parent");
let frames = _____WB$wombat$assign$function_____("frames");
let opens = _____WB$wombat$assign$function_____("opens");
jQuery(document).ready(function ($) {
    // lazy load
    if (fifuImageVars.fifu_lazy)
        fifu_lazy();
    else {
        // no WordPress lazy load for the top images
        jQuery('img').each(function (index) {
            if (jQuery(this).offset().top < jQuery(window).height()) {
                jQuery(this).removeAttr('loading');
            }
        });
    }

    // woocommerce lightbox/zoom
    disableClick($);
    disableLink($);

    // zoomImg
    setTimeout(function () {
        jQuery('img.zoomImg').css('z-index', '');
    }, 1000);

    jQuery('img[height=1]').each(function (index) {
        if (jQuery(this).attr('width') != 1)
            jQuery(this).css('position', 'relative');
    });
});

jQuery(window).on('ajaxComplete', function () {
    if (fifuImageVars.fifu_lazy)
        fifu_lazy();
});

jQuery(document).ajaxSuccess(function ($) {
    if (fifuImageVars.fifu_lazy)
        fifu_lazy_ajax();
});

var observer = new MutationObserver(function (mutations) {
    if (fifuImageVars.fifu_lazy) {
        mutations.forEach(function (mutation) {
            mutation.addedNodes.forEach(function (node) {
                if (jQuery(node).find('img').length > 0) {
                    // ignore WooCommerce zoom
                    if (!jQuery(node).hasClass('pswp__zoom-wrap')) {
                        jQuery(node).find('img').each(function (index) {
                            // dont touch on slider
                            if (jQuery(this).attr('src') == 'null' || jQuery(this).hasClass('lazyload'))
                                return;

                            fifu_lazy_ajax(this);
                        });
                    }
                    return;
                } else if (jQuery(node).prop('tagName') == 'IMG') {
                    // ignore WooCommerce zoom
                    if (!jQuery(node).hasClass('zoomImg'))
                        fifu_lazy_ajax(node);
                    return;
                }
            });
        });
    }
});
observer.observe(document, {attributes: false, childList: true, characterData: false, subtree: true});

function disableClick($) {
    if (!fifuImageVars.fifu_woo_lbox_enabled) {
        firstParentClass = '';
        parentClass = '';
        jQuery('figure.woocommerce-product-gallery__wrapper').find('div.woocommerce-product-gallery__image').each(function (index) {
            parentClass = jQuery(this).parent().attr('class').split(' ')[0];
            if (!firstParentClass)
                firstParentClass = parentClass;

            if (parentClass != firstParentClass)
                return false;

            jQuery(this).children().click(function () {
                return false;
            });
            jQuery(this).children().children().css("cursor", "default");
        });
    }
}

function disableLink($) {
    if (!fifuImageVars.fifu_woo_lbox_enabled) {
        firstParentClass = '';
        parentClass = '';
        jQuery('figure.woocommerce-product-gallery__wrapper').find('div.woocommerce-product-gallery__image').each(function (index) {
            parentClass = jQuery(this).parent().attr('class').split(' ')[0];
            if (!firstParentClass)
                firstParentClass = parentClass;

            if (parentClass != firstParentClass)
                return false;

            jQuery(this).children().attr("href", "");
        });
    }
}

jQuery(document).click(function ($) {
    fifu_fix_gallery_height();
})

function fifu_fix_gallery_height() {
    if (fifuImageVars.fifu_is_flatsome_active) {
        mainImage = jQuery('.woocommerce-product-gallery__wrapper div.flickity-viewport').find('img')[0];
        if (mainImage)
            jQuery('.woocommerce-product-gallery__wrapper div.flickity-viewport').css('height', mainImage.clientHeight + 'px');
    }
}

}

/*
     FILE ARCHIVED ON 09:07:15 Dec 13, 2022 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 13:49:00 Apr 02, 2026.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 0.881
  exclusion.robots: 0.043
  exclusion.robots.policy: 0.023
  esindex: 0.014
  cdx.remote: 92.209
  LoadShardBlock: 3473.441 (3)
  PetaboxLoader3.datanode: 439.548 (4)
  PetaboxLoader3.resolve: 431.653 (2)
  load_resource: 165.393
*/