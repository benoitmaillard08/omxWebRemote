$(document).ready(function() {
    $("#play-pause").click(
        $.get(pause_url)
    );
});