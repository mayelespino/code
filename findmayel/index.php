<?PHP
    require 'class.sosumi.php';
    
    // You'll need to enter your own Google Maps API key
    // Get one from here: http://code.google.com/apis/maps/signup.html
    $google_maps_key = '';

    // Enter your MobileMe username and password
    $ssm = new Sosumi('mayelespino', '3878@rio-senegal.juarez');
    $loc = $ssm->locate();
    
    if(isset($_POST['btnSend']))
    {
        $alarm = isset($_POST['alarm']);
        $ssm->sendMessage($_POST['msg'], $alarm);
        header('Location: ' . $_SERVER['PHP_SELF']);
    }
?>
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<meta http-equiv="refresh" content="120" >
	<META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE">
		
    <title>Find Mayel Espino</title>
    <link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/2.8.0r4/build/reset-fonts-grids/reset-fonts-grids.css">
    <link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/2.8.0r4/build/base/base-min.css">
    <style type="text/css" media="screen">
        p { text-align:left; }
        #map_canvas { width:700px; height:500px; border:1px solid #000; }
    </style>
    <script src="http://maps.google.com/maps?file=api&amp;v=2&amp;key=<?PHP echo $google_maps_key; ?>&amp;sensor=false" type="text/javascript"></script>
    <script type="text/javascript">
        function initialize() {
            function zoomFit() {
                newzoom = map.getBoundsZoomLevel(bounds);
                newcenter = bounds.getCenter();
                map.setCenter(newcenter, newzoom);
            }

            function createMarker(point, msg) {
                bounds.extend(point);
                var marker = new GMarker(point);
                GEvent.addListener(marker, "click", function() {
                    map.openInfoWindowHtml(point, msg);
                });
                zoomFit();
                return marker;
            }

            if (GBrowserIsCompatible()) {
                var bounds = new GLatLngBounds();

                var map = new GMap2(document.getElementById("map_canvas"));
                map.setUIToDefault();

                var point = new GLatLng(<?PHP echo $loc['latitude']; ?>, <?PHP echo $loc['longitude']; ?>);
                map.addOverlay(createMarker(point, "Your Location"));
            }
        }
    </script>
</head>



<body onload="initialize()" onunload="GUnload()">
    <h2 align="left">Send me a message:</h2>
    <form action="" method="post">
        <p>
            <label for="msg">Message:</label>
            <input type="text" name="msg" value="" id="msg">
            <input type="checkbox" name="alarm" value="1" id="alarm">
            <label for="alarm">Alarm?</label>
            <input type="submit" name="btnSend" value="Send" id="btnSend">
        </p>
    </form>


    <div id="map_canvas"></div>
    </br>
    <h2 align="left">Where I am now:</h2>
    <table width="700">
        <tr>
        <td>Latitude:</td>
        <td><?PHP echo $loc['latitude'];  ?></td>
        <td>Longitude:</td>
        <td><?PHP echo $loc['longitude']; ?></td>
	<td><?PHP echo date('l jS \of F Y h:i:s A'); ?></>
        </tr>
	<tr>
	<td>Address : </td>
        <td colspan="4">

  <?PHP
   //$service_url = 'http://maps.google.com/maps/api/geocode/json?latlng='+$loc['latitude']+','+$loc['longitude']+'&sensor=false';
   $service_url = sprintf('http://maps.google.com/maps/api/geocode/json?latlng=%s,%s&sensor=false',$loc['latitude'] , $loc['longitude']);
   echo "<br/>";
   $curl = curl_init($service_url);
   curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
   curl_setopt($curl, CURLOPT_POST, true);
   curl_setopt($curl, CURLOPT_POSTFIELDS, $curl_post_data);
   $curl_response = curl_exec($curl);
   curl_close($curl);
   $json = json_decode($curl_response,true);

   echo trim($json["results"][0]["formatted_address"]);
?>
	</tr>
    </table>



</br>
<h2  align="left">Last 10 places I've been at:</h2>
<table width="700">
<?PHP
    $file = '5105125323.txt';
    $line = sprintf("<tr><td>%s</td><td>%s</td></tr>\n", trim($json["results"][0]["formatted_address"]), date('l jS \of F Y h:i:s A'));
    file_put_contents($file, $line, FILE_APPEND | LOCK_EX);
    $lines = file($file);
    if(count($lines) > 10)
    {
        unset($lines[0]);
	$lines = array_values($lines);
	file_put_contents($file,implode($lines));
    }
    $lines = array_reverse($lines);
    foreach ($lines as $line_num => $line) {
        echo $line;
    }
    fclose($lines);    
?>
</table>
</body>
<!--
http://www.phpeveryday.com/articles/PHP-File-Removing-Lines-From-File-P515.html
http://www.php.net/manual/en/function.ftruncate.php
http://us3.php.net/count
http://www.php.net/manual/en/function.array-reverse.php
-->
</html>
