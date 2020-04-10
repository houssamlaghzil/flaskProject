<?php

$result = json_decode($json ,true);

echo "<table>";
foreach($result  as $R=>$D){
 echo "<tr id='Tr_".$R."'>";
 foreach($D as $key=>$Value){
    echo "<td id='Td_".$R."_".$key."'>".$Value."</td>";
  }
 echo "</tr>";
}
echo "</table>";
?>