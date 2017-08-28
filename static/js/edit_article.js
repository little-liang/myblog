/**
 * Created by Administrator on 2017/8/28.
 */

$(document).ready(function(){
    $("#dropdown1").next().hide();
    $("#dropdown1").click(function(){
        $(this).next().find("a").css("background-color","#f5f5f5");
        $(this).next().toggle(500);})
});


tinymce.init({
  selector: 'textarea#elm1',
  height: 400,
  theme: 'modern',
  language: "zh_CN",
	plugins: [
	'advlist autolink lists link image charmap print preview hr anchor pagebreak',
	'searchreplace wordcount visualblocks visualchars code fullscreen',
	'insertdatetime media nonbreaking save table contextmenu directionality',
	'emoticons template paste textcolor colorpicker textpattern imagetools codesample toc help'
  ],
  toolbar1: 'undo redo | insert | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
  toolbar2: 'print preview media | forecolor backcolor emoticons | codesample help',
  image_advtab: true,
  templates: [
	{ title: 'Test template 1', content: 'Test 1' },
	{ title: 'Test template 2', content: 'Test 2' }
  ]
 });
