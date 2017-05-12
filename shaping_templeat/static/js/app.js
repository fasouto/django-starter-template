var Nav = React.createClass({

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

var Header = React.createClass({

    render: function() {
        return (
            <p>s</p>
        );
    }
});

var Footer = React.createClass({
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

var Index = React.createClass({

    render: function() {
        return ( <div >
            <Nav/>  
            <Footer/>
             </div>
        );
    }
});


ReactDOM.render( < Index/> ,
    document.getElementById('content')
);