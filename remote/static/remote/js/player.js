$(document).ready(function() {
    $(".remote-button").click(function() {
        $.get(ajax_url, {"key" : $(this).attr("data-key")});
    });
});