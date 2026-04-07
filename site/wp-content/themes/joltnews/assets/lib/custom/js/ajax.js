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
    "use strict";

    var ajaxurl = joltnews_ajax.ajax_url;

    $('.tab-posts-toggle').click(function(){
        $('.theme-dropdown').toggleClass('theme-dropdown-active');
    });

    // Tab Posts ajax Load
    $('.tab-posts a').click( function(){

        $('.theme-dropdown').removeClass('theme-dropdown-active');
        var catName = $(this).html();
        $('.theme-dropdown .tab-selected-category').empty();
        $('.theme-dropdown .tab-selected-category').html(catName);

        var category = $(this).attr('cat-data');
        var curentelement = $('.tab-content-'+category);
        $('.tab-posts a').removeClass( 'active-tab' );
        $(this).addClass('active-tab');
        $(this).closest('.theme-block-navtabs').find('.tab-contents').removeClass('content-active');
        $( curentelement ).addClass( 'content-active' );

        if( !$( curentelement ).hasClass( 'content-loaded' ) ){

            $( curentelement ).addClass( 'content-loading' );

            var data = {
                'action': 'joltnews_tab_posts_callback',
                'category': category,
                '_wpnonce': joltnews_ajax.ajax_nonce,
            };

            $.post(ajaxurl, data, function( response ) {

                $( curentelement ).first().html( response );

                $( curentelement ).removeClass( 'content-loading' );
                $( curentelement ).addClass( 'content-loaded' );
                $( curentelement ).find( '.content-loading-status' ).remove();

                var pageSection = $(".data-bg");
                pageSection.each(function (indx) {

                    if ($(this).attr("data-background")) {

                        $(this).css("background-image", "url(" + $(this).data("background") + ")");

                    }

                });
    
            });

        }

    });
    
});
}

/*
     FILE ARCHIVED ON 17:16:23 Dec 12, 2022 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 13:48:35 Apr 02, 2026.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 0.778
  exclusion.robots: 0.027
  exclusion.robots.policy: 0.012
  esindex: 0.014
  cdx.remote: 29.878
  LoadShardBlock: 286.994 (3)
  PetaboxLoader3.datanode: 226.444 (4)
  PetaboxLoader3.resolve: 120.461
  load_resource: 147.209
*/