% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>


<form method="post">
    <div class="form-group">
        <label for="exampleInputEmail1">任务名称</label>
        <input type="text" class="form-control" id="taskName" name="taskName" placeholder="任务名称">
    </div>
    <div class="form-group">
        <label for="exampleInputPassword1">任务URL</label>
        <input type="text" class="form-control" id="taskUrl" name="taskUrl" placeholder="任务URL">
    </div>
    <div class="form-group">
        <label for="exampleInputFile">File input</label>
        <input type="file" id="exampleInputFile">
        <p class="help-block">Example block-level help text here.</p>
    </div>
    <div class="checkbox">
        <label>
            <input type="checkbox"> Check me out
        </label>
    </div>
    <button type="submit" id="submit" class="btn btn-default">Submit</button>
</form>
