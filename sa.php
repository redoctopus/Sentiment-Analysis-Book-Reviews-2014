<!-- The kind of gross file I used to run Sentiment Analysis on the TJHSST server.
     Don't have the book stock photo on GitHub, and it's probably not worth digging up. -->

<html>
  <head>
  <link rel="stylesheet" href="stylesheet.css">
    <title>Jocelyn Huang's Book Review Sentiment Analysis</title>
  </head>

  <body bgcolor='D0D0D0'>
  <font face="bookman,modern,courier">
   <div id="banner">
   <font color='000066'>
    <h1>Book Review Sentiment Analysis</h1>
   </font>
  </div>

  <hr style="border: 3px double #333366">

 <table>
 <tr>
 <td id="leftcell">
  <div id="leftbar">
  <font face="Trebuchet MS">
  <b>Project Overview:</b>
  <br><br>
  This sentiment analysis program will take an input (preferably a book review, since that is what it has been trained on) and return a positivity or negativity rating depending on what the input text is. The scale used ranges from 0 to 100, with 0 being the most negative and 100 being the most positive; 50 is the neutral default value.
  <br><br>
  Currently, the program is in its final stages!
  </font>
  </div>
 </td>

 <td id="centercell">
  <div id="center">
    <?php
      $in_text = isset($_REQUEST['intext']) ? $_REQUEST['intext'] : "Enter text to analyze";
    ?>

    <form action="sa.php" method="post">
      <br><b><font size="5">Enter your text to Analyze:</font></b>
      <br><br>
      <textarea name="intext" rows="15" cols="50"><?=$in_text;?></textarea>
      <img src="BookStockPhoto.png" width=200 height=200>
      <p><input type="submit" Value="Analyze" />
      <br><h2>Results:</h2>
      <!--You entered <b><?=$in_text;?></b> -->
      <?php
        //$in_text = preg_replace('/\'/', '', $in_text);
	//--> // $in_text = str_replace("'", "", $in_text);
        //$in_text = preg_replace('/\x27/', '', $in_text);
	//$in_text = str_replace("\x27", "", $in_text);

	//$in_text = str_replace("\xD3\x99", "", $in_text);
	//$in_text = preg_replace('/\xD3-\x99/', '', $in_text);
	
	$in_text = preg_replace('/\'/', '', $in_text); // Apostrophes first
	$in_text = preg_replace('/[^\w ]/', ' ', $in_text);

	//////print "<pre>Single quotes removed: {$in_text}</pre>";
	$cmd = "python3 ReadFromFileTest.py '$in_text'";
	//$cmd = "python3 DebugCopyRFFT.py '$in_text{}'";
	//$cmd = "python3 WebTest.py";
        $res = shell_exec ($cmd);
	print "<br/><pre>{$res}</pre>";
	//print "<br/>Cmd = {$cmd} <br/>Res =<pre>{$res}</pre>";
      ?>
    </form>
   </div>
  </td>
  </tr>
 </table>

    </font>
  </body>
 </div>

    <br>
    <div><p><small><b>Or you can go <a href=".">back</a>.</b></small></p></div>
</html>

