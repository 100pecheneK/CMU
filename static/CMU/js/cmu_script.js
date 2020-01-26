$(function () {
    $('[data-toggle="tooltip"]').tooltip()
});
$(document).ready(function () {
    $('.cmu_form').removeAttr('hidden');
    $('.cmu_form').submit(function (e) {
        const form = $(this);
        $.ajax({
            type: form.attr('method'),
            url: form.attr('action'),
            data: {
                cmu_obj_url: window.location.href,
                csrfmiddlewaretoken: form.children('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
            success: function (json) {
                if (form.children(".cmu_new_url")){
                    form.children(".cmu_new_url").text(json.cmu_new_url);
                }
                navigator.clipboard.writeText(json.cmu_new_url)
                    .then(() => {
                        $('.cmu_button').html('<i class="far fa-copy"></i>');
                        $('.cmu_button').attr("title", "Получить ссылку");
                        $('.cmu_button').attr("data-original-title", "Получить ссылку");
                        form.children('.cmu_button').html('<i class="fas fa-check"></i>');
                        form.children('.cmu_button').attr("title", "Скопирована!").tooltip("_fixTitle").tooltip("show").attr("title", "Скопирована!").tooltip("_fixTitle");
                    })
                    .catch(err => {
                        console.log('Something went wrong', err);
                    });
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
        e.preventDefault();
    });
});