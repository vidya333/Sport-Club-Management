$(document).ready(function(){
    $('#insert').click(function(){
        $ename=$('#ename').val();
        $eloc=$('#eloc').val();
        $esal=$('#esal').val();

        if($ename=='' ||  $eloc=='' || $esal==''){
            alert('Please enter all required fields...');
            }
        else{
            $.ajax({
                url:'create',
                type:'POST',
                data:{
                    ename:$ename,
                    eloc:$eloc,
                    esal:$esal,
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                    },
                    success:function(){
                        $('h1').text('Records Inserted Successfully...!!');
                        $('#ename').val('');
                        $('#eloc').val('');
                        $('#esal').val('')
                        }
                 })
        }

    })
    $('#display').click(function(){
    read();
})
})//end jquery code


function del(eid){
        $.ajax({
            url:`delete?id=${eid}`,
            type:'GET',
            success:function(response){
                alert("Record deleted successfully...!!")
                read();
            }
          })
        }

function read(){
    $.ajax({
        url:"show",
        type:"POST",
        data:{
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
             },
             success:function(response){
             let rows='';
             response.dt.forEach(emp=>{
                rows+=`
                    <tr>
                        <td>${emp.ename}</td>
                        <td>${emp.eloc}</td>
                        <td>${emp.esal}</td>
                        <td><a class='btn btn-danger' name="${emp.id}" onclick="del(${emp.id})">Delete</a></td>
                    </tr>
                `;
             $('tbody').html(rows);
             })
           }
        })
    }