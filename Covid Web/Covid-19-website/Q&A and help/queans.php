<html>
    <head>
    <link href="./CSS/qna.css" rel="stylesheet">
<title>Q&A</title>
        
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
    <a href="addquestion.html"><div class="button">Add question</div></a>
    <?php
    $servername = "localhost";
    $username = "id16437582_admin";
    $dbname="id16437582_questions";
    $password="Lambapassword77!";

    $conn = mysqli_connect($servername, $username,$password, $dbname,);

    $sql="SELECT * FROM question";

    $res=$conn->query($sql);

    if ($res->num_rows > 0)
    while($row=$res->fetch_assoc())
    {
        $qnum=$row["no"];
        echo '<button class="accordion">'.$row["question"]."</button>";
        echo '<div class="panel">';
        echo '<a href="./addans.php?q='.$qnum.'"> <div class="but">Add Answer</div></a>';
        $sql="SELECT ans FROM answer WHERE qno=".$qnum." ORDER BY upv DESC";
        $res1=$conn->query($sql);
        if ($res1->num_rows > 0)
        {
            echo "<ul>";
            while($row=$res1->fetch_assoc())
            echo "<li>".$row["ans"]."</li><hr>";
            echo "</ul>";
        }
        else echo 'No answers';
        echo '</div>';
    }

    mysqli_close($conn);?>
    <script src="./javascript/qna.js"></script>
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