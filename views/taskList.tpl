% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>


<form>
    <div class="panel panel-default">
        <!-- Default panel contents -->
        <div class="panel-heading">Panel heading</div>
        <div class="panel-body">
            <p>...</p>
        </div>

        <!-- Table -->
        <table class="table">
            ...
        </table>
    </div>
</form>
<script>
    var data = {{ !data }}
    for (var i = 0; i < data.length; i++) {
        $(".table").append("<tr></tr>");
        for (var j = 0; j < data[i].length; j++) {
            $(".table tr").last().append("<td>"+ data[i][j] +"</td>");

        }
    }
    
</script>