$(".button").click(function() {
  var n = document.getElementById("num").value;
  var c = document.getElementById("cols").value;
  var arr = [];
  for (i = 0; i < n; i++)
    arr[i] = [];
  var sub = 1;
  var count = 1;
  i = 0;
  while (count <= n) {
    var loopcount = 1;
    while (loopcount <= c) {
      arr[i].push(sub);
      sub += count;
      loopcount++;
    }
    count++;
    sub = count;
    i++;
  }

  var $table = $("<table></table>");
  var $row;
  arr.forEach(function(subArr) {
    $row = $("<tr></tr>");
    subArr.forEach(function(el) {
      $row.append('<td>' + el + '</td>');
    });
    $table.append($row);
  });
  $table.appendTo(document.body);

});
