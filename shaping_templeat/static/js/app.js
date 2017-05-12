let Nav = React.createClass({

    render: function() {
        return (
<nav className="navbar navbar-default">
        <div className="container-fluid">
          <div className="navbar-header">
            <button type="button" className="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
              <span className="sr-only">Toggle navigation</span>
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
            </button>
            <a className="navbar-brand" href="#">Project name</a>
          </div>
          <div id="navbar" className="navbar-collapse collapse">
            <ul className="nav navbar-nav">
              <li className="active"><a href="#">Home</a></li>
              <li><a href="#">About</a></li>
              <li><a href="#">Contact</a></li>
              <li className="dropdown">
                <a href="#" className="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span className="caret"></span></a>
                <ul className="dropdown-menu">
                  <li><a href="#">Action</a></li>
                  <li><a href="#">Another action</a></li>
                  <li><a href="#">Something else here</a></li>
                  <li role="separator" className="divider"></li>
                  <li className="dropdown-header">Nav header</li>
                  <li><a href="#">Separated link</a></li>
                  <li><a href="#">One more separated link</a></li>
                </ul>
              </li>
            </ul>
            <ul className="nav navbar-nav navbar-right">
              <li className="active"><a href="./">Default <span className="sr-only">(current)</span></a></li>
              <li><a href="../navbar-static-top/">Static top</a></li>
              <li><a href="../navbar-fixed-top/">Fixed top</a></li>
            </ul>
          </div>
        </div>
      </nav>
        );
    }
});

let Slaider = React.createClass({
    componentDidMount: function () {
        $(document).ready(function(){
            // invoke the carousel
            $('#myCarousel').carousel({
                interval:6000
                });

            // scroll slides on mouse scroll 
            $('#myCarousel').bind('mousewheel DOMMouseScroll', function(e){

                if(e.originalEvent.wheelDelta > 0 || e.originalEvent.detail < 0) {
                    $(this).carousel('prev');
                
                
                }
                else{
                    $(this).carousel('next');
                
                }
            });

            //scroll slides on swipe for touch enabled devices 

            $("#myCarousel").on("touchstart", function(event){
    
                var yClick = event.originalEvent.touches[0].pageY;
                $(this).one("touchmove", function(event){

                    var yMove = event.originalEvent.touches[0].pageY;
                    if( Math.floor(yClick - yMove) > 1 ){
                        $(".carousel").carousel('next');
                    }
                    else if( Math.floor(yClick - yMove) < -1 ){
                        $(".carousel").carousel('prev');
                    }
                });
                $(".carousel").on("touchend", function(){
                    $(this).off("touchmove");
                });
            });
        });
        //animated  carousel start
        $(document).ready(function(){
            //to add  start animation on load for first slide 
            $(function(){
                $.fn.extend({
                    animateCss: function (animationName) {
                        var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
                        this.addClass('animated ' + animationName).one(animationEnd, function() {
                            $(this).removeClass(animationName);
                        });
                }
                });
                $('.item1.active img').animateCss('slideInDown');
                $('.item1.active h2').animateCss('zoomIn');
                $('.item1.active p').animateCss('fadeIn');
                
            });
        
            //to start animation on  mousescroll , click and swipe
            $("#myCarousel").on('slide.bs.carousel', function () {
                $.fn.extend({
                    animateCss: function (animationName) {
                        var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
                        this.addClass('animated ' + animationName).one(animationEnd, function() {
                            $(this).removeClass(animationName);
                        });
                    }
                });
        
            // add animation type  from animate.css on the element which you want to animate

                $('.item1 img').animateCss('slideInDown');
                $('.item1 h2').animateCss('zoomIn');
                $('.item1 p').animateCss('fadeIn');
                
                $('.item2 img').animateCss('zoomIn');
                $('.item2 h2').animateCss('swing');
                $('.item2 p').animateCss('fadeIn');
                
                $('.item3 img').animateCss('fadeInLeft');
                $('.item3 h2').animateCss('fadeInDown');
                $('.item3 p').animateCss('fadeIn');
            });
        });

    },
    render: function () {
        return(
        <section className="slide-wrapper">
        <div className="container">
            <div id="myCarousel" className="carousel slide">
                <ol className="carousel-indicators">
                    <li data-target="#myCarousel" data-slide-to="0" className="active"></li>
                    <li data-target="#myCarousel" data-slide-to="1"></li>
                    <li data-target="#myCarousel" data-slide-to="2"></li>
                 </ol>

                <div className="carousel-inner">
                    <div className="item item1 active">
                        <div className="fill" >
                            <div className="inner-content">
                                <div className="carousel-img">
                                    <img src="http://vocefalandoingles.com/wp-content/uploads/2016/09/sofa.png" alt="sofa" className="img img-responsive" />
                                </div>
                                <div className="carousel-desc">

                                    <h2>Modern Designer Sofa</h2>
                                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis elit ipsum, scelerisque non semper eu, aliquet vel odio. Sed auctor id purus nec tristique. Donec euismod, urna vel dapibus tristique, dolor arcu ultrices lectus, nec pulvinar est turpis sit amet felis. Duis interdum purus quam, vitae cursus erat ornare at. Donec congue mi a ipsum tincidunt, imperdiet vehicula odio rutrum. Nam porta vulputate magna, id pretium lectus iaculis eu. Ut ut viverra libero.</p>

                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="item item2">
                        <div className="fill" >
                            <div className="inner-content">
                                <div className="carousel-img">
                                    <img src="http://cdn.homedit.com/wp-content/uploads/2011/08/137CLUB2ST.png" 
                                    alt="white-sofa" className="img img-responsive" />
                                </div>
                                <div className="carousel-desc">

                                    <h2>Vintage Style Sofa</h2>
                                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis elit ipsum, scelerisque non semper eu, aliquet vel odio. Sed auctor id purus nec tristique. Donec euismod, urna vel dapibus tristique, dolor arcu ultrices lectus, nec pulvinar est turpis sit amet felis. Duis interdum purus quam, vitae cursus erat ornare at. Donec congue mi a ipsum tincidunt, imperdiet vehicula odio rutrum. Nam porta vulputate magna, id pretium lectus iaculis eu. Ut ut viverra libero.</p>

                                </div>
                            </div>
                        </div>
                    </div>


                    <div className="item item3">
                        <div className="fill" >
                            <div className="inner-content">
                                <div className="carousel-img">
                                    <img src="http://cdn.homedit.com/wp-content/uploads/2011/08/137CLUB2ST.png" 
                                    alt="white-sofa" className="img img-responsive" />
                                </div>
                                <div className="carousel-desc">

                                    <h2>Vintage Style Sofa</h2>
                                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis elit ipsum, scelerisque non semper eu, aliquet vel odio. Sed auctor id purus nec tristique. Donec euismod, urna vel dapibus tristique, dolor arcu ultrices lectus, nec pulvinar est turpis sit amet felis. Duis interdum purus quam, vitae cursus erat ornare at. Donec congue mi a ipsum tincidunt, imperdiet vehicula odio rutrum. Nam porta vulputate magna, id pretium lectus iaculis eu. Ut ut viverra libero.</p>

                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>);
    }
});

let Header = React.createClass({

    render: function() {
        return (
            <div className="container">
    <div className="page-header">
        <h3>Add the (.grid-divider) className to any row to separate grid columns with equal height lines.</h3>
    </div>
    <div className="row grid-divider">
    <div className="col-sm-4">
      <div className="col-padding">
        <h3>Column 1</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima expedita incidunt rerum.</p>
      </div>
    </div>
    <div className="col-sm-4">
      <div className="col-padding">
        <h3>Column 2</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate placeat suscipit maxime tenetur officiis asperiores quae molestias fugiat praesentium dolorum.</p>
      </div>
    </div>
    <div className="col-sm-4">
      <div className="col-padding">
        <h3>Column 3</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab veniam aperiam numquam cupiditate maiores repudiandae ea dicta, sunt rerum corporis. Ab veniam aperiam numquam cupiditate maiores repudiandae ea dicta, sunt rerum corporis. Ab veniam aperiam numquam cupiditate maiores repudiandae ea dicta.</p>
      </div>
    </div>
    </div>

</div>
        );
    }
});

let Footer = React.createClass({
    render: function() {
        return (
                <footer>
                <div className="footer" id="footer">
                    <div className="container">
                        <div className="row">
                            <div className="col-lg-2  col-md-2 col-sm-4 col-xs-6">
                                <h3> Lorem Ipsum </h3>
                                <ul>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                </ul>
                            </div>
                            <div className="col-lg-2  col-md-2 col-sm-4 col-xs-6">
                                <h3> Lorem Ipsum </h3>
                                <ul>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                </ul>
                            </div>
                            <div className="col-lg-2  col-md-2 col-sm-4 col-xs-6">
                                <h3> Lorem Ipsum </h3>
                                <ul>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                </ul>
                            </div>
                            <div className="col-lg-2  col-md-2 col-sm-4 col-xs-6">
                                <h3> Lorem Ipsum </h3>
                                <ul>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                    <li> <a href="#"> Lorem Ipsum </a> </li>
                                </ul>
                            </div>
                            <div className="col-lg-3  col-md-3 col-sm-6 col-xs-12 ">
                                <h3> Lorem Ipsum </h3>
                                <ul>
                                    <li>
                                        <div className="input-append newsletter-box text-center">
                                            <input type="text" className="full text-center" placeholder="Email "/>
                                            <button className="btn  bg-gray" type="button"> Lorem ipsum <i className="fa fa-long-arrow-right"> </i> </button>
                                        </div>
                                    </li>
                                </ul>
                                <ul className="social">
                                    <li> <a href="#"> <i className=" fa fa-facebook">   </i> </a> </li>
                                    <li> <a href="#"> <i className="fa fa-twitter">   </i> </a> </li>
                                    <li> <a href="#"> <i className="fa fa-google-plus">   </i> </a> </li>
                                    <li> <a href="#"> <i className="fa fa-pinterest">   </i> </a> </li>
                                    <li> <a href="#"> <i className="fa fa-youtube">   </i> </a> </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="footer-bottom">
                    <div className="container">
                        <p className="pull-left"> Copyright © Footer 2014. All right reserved. </p>
                        <div className="pull-right">
                            <ul className="nav nav-pills payments">
                                <li><i className="fa fa-cc-visa"></i></li>
                                <li><i className="fa fa-cc-mastercard"></i></li>
                                <li><i className="fa fa-cc-amex"></i></li>
                                <li><i className="fa fa-cc-paypal"></i></li>
                            </ul> 
                        </div>
                    </div>
                </div>
                </footer>
                );
    }
});

let Index = React.createClass({

    render: function() {
        return ( 
        <div >
            <Nav/>  
            <Slaider/>
            <Header/>
            <Footer/>
        </div>
        );
    }
});


ReactDOM.render( < Index/> ,
    document.getElementById('content')
);