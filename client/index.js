import $ from 'jquery'
import 'imports-loader?jQuery=jquery!jquery-bracket'
import 'style-loader!../node_modules/jquery-bracket/dist/jquery.bracket.min.css'

var minimalData = {
    teams : [
      ["Team 1", "Team 2"],
      ["Team 3", "Team 4"] 
    ],
    results : [
      [[1,2], [3,4]],      
      [[4,6], [2,1]]       
    ]
  }
 
$(function() {
    $('#bracket.demo').bracket({
      init: minimalData })
  })
