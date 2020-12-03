
(function ($) {
    "use strict";

    /*==================================================================
    [ Focus Contact2 ]*/
    $('.input100').each(function(){
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })    
    })

    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(e){
        e.preventDefault()
        var checkResult = validateAll(input);
        if (checkResult == false) {
            return false;
        }
        
        /*==================================================================
        [ Here will be a call to our API ]*/
        
        
        
        var ageInput = $("#age").val();
        var erythroInput = $("#erythrocytes").val();
        var haemoglobinInput = $("#haemoglobin").val();
        var haematocritInput = $("#haematocrit").val();
        var leucocytesInput = $("#leucocytes").val();
        var thromboInput = $("#thrombocytes").val();
        var mchInput = $("#mch").val();
        var mchcInput = $("#mchc").val();
        var mcvInput = $("#mcv").val();

        $.ajax({
            url: "/bloodTest",
            type: "get",
            data: $.param({age: ageInput, erythrocytes: erythroInput, haemoglobin: haemoglobinInput, haematocrit: haematocritInput,
            leucocytes: leucocytesInput, thrombocytes: thromboInput, mch: mchInput, mchc: mchcInput, mcv: mcvInput}),
            success: function (response) {
                $("#place_for_suggestions").html(response);
            },
            error: function (xhr) {
                
            }
        });
        
        return true;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });
    
    function validateAll (input) {
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    }
    
    function validate (input) {
        if($(input).val().trim() == ''){
            return false;
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }


})(jQuery);