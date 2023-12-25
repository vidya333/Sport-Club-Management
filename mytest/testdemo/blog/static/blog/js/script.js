//$(document).ready(function(){
//    $('#insert').click(function(){
//        $ename=$('#ename').val();
//        $eloc=$('#eloc').val();
//        $esal=$('#esal').val();
//
//        if($ename==' ' ||  $eloc==' ' || $esal==' '){
//            alert('Please enter all required fields...');
//            }
//        else{
//            $.ajax({
//                url:'create',
//                type:'POST',
//                data:{
//                    ename:$ename,
//                    eloc:$eloc,
//                    esal:$esal,
//                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
//                    },
//                    success:function(){
//                        $('h1').text('Records Inserted Successfully...!!');
//                        $('#ename').val(' ');
//                        $('#eloc').val(' ');
//                        $('#esal').val(' ')
//                        }
//                 })
//        }
//
//    })
//})