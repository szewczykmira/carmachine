/**
 * Created by mira on 6/12/16.
 */

$(document).ready(function(){
    $('input').addClass('form-control');
    $('textarea').addClass('form-control');
    $('select').addClass('form-control');
    $('input').focus(function(){
        $(this).parent().parent().addClass('is-focused');
    });
    $('input').focusout(function(){
        $(this).parent().parent().removeClass('is-focused');
    });
    $('textarea').focus(function(){
        $(this).parent().parent().addClass('is-focused');
    });
    $('textarea').focusout(function(){
        $(this).parent().parent().removeClass('is-focused');
    });
    $('select').focus(function(){
        $(this).parent().parent().addClass('is-focused');
    });
    $('select').focusout(function(){
        $(this).parent().parent().removeClass('is-focused');
    });
});