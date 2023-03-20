<html><head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>


    <!-- navigation  -->
    <link href="CSS/navigation.css" media="screen and (min-width:1150px)" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Girassol&display=swap" rel="stylesheet">
    <link href="CSS/phnavigation.css" media="screen and (max-width:1150px)" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&display=swap" rel="stylesheet">
    <!-- navigation  -->




</head>
    <body>
        <header class="header" id="header">
        <div class="logo" id="logo">
            Covid-19
        </div>
        <div class="navmenu" id="navmenu">
            <ul class="menu">
                <li class="navitem" id="home"><a href="https://nileshmalav.github.io/Team-LEO-DevJam-2021/index.html">Home</a></li>
                <li class="navitem" id="covidInfo"><a href="https://nileshmalav.github.io/Team-LEO-DevJam-2021/covid%20info.html">Covid Info</a></li>
                <li class="navitem" id="covidTracker"><a href="https://nileshmalav.github.io/Team-LEO-DevJam-2021/covid%20tracker.html">Covid Tracker</a></li>
                <li class="navitem" id="plagam"><a href="https://nileshmalav.github.io/Team-LEO-DevJam-2021/play%20games.html">Play Games</a></li>
                <li class="navitem" id="help"><a href="http://hckd.tk/helpln.php">Help</a></li>
                <!-- <li class="navitem" id="QA"><a href="que ans.html">Q&A</a></li> -->
                <div class="dropdown" id="more">
                    <button class="dropbtn">More
                    </button>
                    <div class="dropdown-content">
                        <a href="https://nileshmalav.github.io/Team-LEO-DevJam-2021/listen%20music.html" id="lismus">Listen Music</a>
                        <a href="https://nileshmalav.github.io/Team-LEO-DevJam-2021/movies%20and%20shows.html" id="movsho">Movies & shows</a>
                        <!-- <a href="play games.html" id="plagam">Play Games</a> -->
                        <a href="http://hckd.tk/" id="QA">Q&A</a>
                    </div>
                </div>
            </ul>
        </div>
        <div class="right" id="right">
            <button id="navBtn"><a href="https://www.cowin.gov.in/home" target="blank">Get Vaccine</a></button>
        </div>
    </header>
    <!-- header dropdown -->
    <div class="dNavVisible">

        <div class="dlogo" id="dlogo">
            Covid-19
        </div>
        <div class="dnmenu">
            <input class="menu-btn" type="checkbox" id="menu-btn" />
            <label class="menu-icon" for="menu-btn"><span class="navicon"></span></label>
            <header class="dheader" id="dheader">

                <div class="dnavmenu" id="dnavmenu">
                    <ul class="dmenu">
                        <li class="dnavitem" id="phome"><a href="https://nileshmalav.github.io/Team-LEO-DevJam-2021/index.html">Home</a></li>
                        <li class="dnavitem" id="pcovidInfo"><a href="https://nileshmalav.github.io/Team-LEO-DevJam-2021/covid%20info.html">Covid Info</a></li>
                        <li class="dnavitem" id="pcovidTracker"><a href="https://nileshmalav.github.io/Team-LEO-DevJam-2021/covid%20tracker.html">Covid Tracker</a></li>
                        <li class="dnavitem" id="pplagam"><a href="https://nileshmalav.github.io/Team-LEO-DevJam-2021/play%20games.html">Play Games</a></li>
                        <li class="dnavitem" id="phelp"><a href="http://hckd.tk/helpln.php">Help</a></li>
                        <li class="dnavitem" id="pQA"><a href="http://hckd.tk/">Q & A</a></li>
                        <li class="dnavitem" id="plismus"><a href="https://nileshmalav.github.io/Team-LEO-DevJam-2021/listen%20music.html">Listen Music</a></li>
                        <li class="dnavitem" id="pmovsho"><a href="https://nileshmalav.github.io/Team-LEO-DevJam-2021/movies%20and%20shows.html">Movies & Shows</a></li>
                    </ul>
                </div>
                <div class="dright" id="dright">
                    <button id="dnavBtn"><a href="https://www.cowin.gov.in/home" target="blank">Get Vaccine</a></button>
                </div>
        </div>
        </header>
    </div>

    <box class="headerbox"></box>
    <!-- header -->
        Your answer:
        <?php
            $servername = "localhost";
            $username = "id16437582_admin";
            $dbname="id16437582_questions";
            $password="Lambapassword77!";

            $ans=$_POST["ans"];
            echo $ans;
            $qno=$_POST["qno"];
            $conn = mysqli_connect($servername, $username,$password, $dbname,);
            $sql = "INSERT INTO answer(ans,qno,upv) VALUES ('".$ans."','".$qno."','0')";
            if($conn->query($sql)==true) echo "has been added successfully.";
            else echo "could not be added. Please try again later";
            

?>
<!-- footer -->
<footer data-aos="fade-up" class="footer" id="footer">
    <div data-aos="fade-right" class="footerimg"><a href="https://www.mohfw.gov.in/" target="blank"><img
                src="images/footer.png">
            <div class="footerimgtext">Ministry of Health <br>and Family Welfare</div>
        </a>
    </div>
    <div class="footertext">
        <div class="fdiv">Created at @WOC Devjam 2021</div>
        <div class="fdiv">By Team LEO</div>
    </div>
</footer>
<!-- footer  -->
</body>
</html>
