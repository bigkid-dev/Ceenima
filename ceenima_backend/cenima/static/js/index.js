

$(document).ready( 
    function(){
        console.log("Ready");
        $("#get-ticket-btn").click(function(){
            $(".book-a-ticket").show("slow");
            }),
        $("button:eq(2)").click(function(){
                $(".book-a-ticket").hide();
                
            });   
});

$(document).ready( 

        $("button:eq(2)").click(function(){
                $(".book-a-ticket").hide();
                console.log("Hello therwe") ;
            }) 
);

