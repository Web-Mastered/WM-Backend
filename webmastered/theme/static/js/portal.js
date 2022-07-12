jQuery(function($) {
    var path = window.location.pathname;
    var activeElements = 0;
    $('.wm-sidebar-link').each(function() {
        var link = (new URL(this.href)).pathname
        if (path.includes(link)) {
            $(this).addClass('text-white');
            $(this).addClass('bg-gradient-to-r');
            $(this).addClass('from-wm-blue');
            $(this).addClass('to-wm-lightblue');
            activeElements++;
        }
    });
    if (activeElements > 1) {
        $('.wm-sidebar-link').each(function() {
            var link = (new URL(this.href)).pathname
            if (link == "/portal/") {
                $(this).removeClass('text-white');
                $(this).removeClass('bg-gradient-to-r');
                $(this).removeClass('from-wm-blue');
                $(this).removeClass('to-wm-lightblue');
            }
        });
    }
});

$(document).ready(function () {
    $('.wm-httpRequests1hGroupTable').DataTable(
        {
            // scrollX: true,
            searching: false,
        }
    );
});

$(document).ready(function () {
    $('.wm-firewallEventsHistoryTable').DataTable(
        {
            // scrollX: true,
            searching: false,
        }
    );
});