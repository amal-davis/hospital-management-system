if (!('ontouchstart' in window)) {
    $('.tip').tooltip();
}
$(function passwordValidation() {

    var pwdInput = $('#input-password');
    var pwdInputText = $('#input-password-text');
    var pwdValid = false;

    function validatePwdStrength() {

        var pwdValue = $(this).val();
        if (pwdValue.length > 7) {
            $('#length').removeClass('invalid').addClass('valid');
            pwdValid = true;
        } else {
            $('#length').removeClass('valid').addClass('invalid');
        }
        if (pwdValue.match(/[A-Z]/)) {
            $('#capital').removeClass('invalid').addClass('valid');
            pwdValid = pwdValid && true;
        } else {
            $('#capital').removeClass('valid').addClass('invalid');
            pwdValid = false;
        }
        if (pwdValue.match(/[a-z]/)) {
            $('#lowercase').removeClass('invalid').addClass('valid');
            pwdValid = pwdValid && true;
        } else {
            $('#lowercase').removeClass('valid').addClass('invalid');
            pwdValid = false;
        }
        if (pwdValue.match(/[\d`~!@#$%\^&*()+=|;:'",.<>\/?\\\-]/)) {
            $('#number-special').removeClass('invalid').addClass('valid');
            pwdValid = pwdValid && true;
        } else {
            $('#number-special').removeClass('valid').addClass('invalid');
            pwdValid = false;
        }
    }

    function validatePwdValid(form, event) {
        if (pwdValid === true) {
            form.submit();
        } else {
            $('#alert-invalid-password').removeClass('hide');
            event.preventDefault();
        }
    }
    pwdInput.bind('change keyup input', validatePwdStrength);
    pwdInputText.bind('change keyup input', validatePwdStrength);
    $(".validate-password").validate({
        highlight: function (element) {
            $(element).parent('.form-group').addClass('error');
        },
        unhighlight: function (element) {
            $(element).parent('.form-group').removeClass('error');
        },
        rules: {
            "passwordCheckMasked": {
                equalTo: "#input-password"
            }
        },
        
        errorPlacement: function (error, element) {
            if (element.attr("name") == "password" || element.attr("name") == "passwordMasked") {
                error.insertAfter("#input-password");
            } else {
                error.insertAfter(element);
            }
            if (element.attr("name") == "passwordCheck" || element.attr("name") == "passwordCheckMasked") {
                error.insertAfter("#input-password-check");
            } else {
                error.insertAfter(element);
            }
        },
        submitHandler: function (form, event) {
            validatePwdValid(form, event);
        }
    });

});