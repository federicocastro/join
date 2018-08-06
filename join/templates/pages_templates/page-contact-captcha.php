
{% extends "base.html" %}
{% load static i18n %}
{% block content %}
<div class="wrapper-boxed">
<div class="site-wrapper">
<div class="topbar light topbar-padding">
<div class="container">
<div class="topbar-left-items">
<ul class="toplist toppadding pull-left paddtop1">
<li class="rightl">Customer Care</li>
<li>(888) 123-4567</li>
</ul>
</div>
<!--end left-->
<div class="topbar-right-items pull-right">
<ul class="toplist toppadding">
<li class="lineright"><a href="#">Login</a></li>
<li class="lineright"><a href="#">Register</a></li>
<li><a href="#"><i class="fa fa-facebook"></i></a></li>
<li><a href="#"><i class="fa fa-twitter"></i></a></li>
<li><a href="#"><i class="fa fa-google-plus"></i></a></li>
<li class="last"><a href="#"><i class="fa fa-linkedin"></i></a></li>
</ul>
</div>
</div>
</div>
<div class="clearfix"></div>
<!--end topbar-->
<div class="col-md-12 nopadding">
<div class="header-section white style1 white pin-style">
<div class="container">
<div class="mod-menu">
<div class="row">
<div class="col-sm-2"> <a class="logo mar-4" href="index.html" title=""> <img alt="" src="{% static "images/logo/logo-dark.png" %}  "/> </a> </div>
<div class="col-sm-10">
<div class="main-nav">
<ul class="nav navbar-nav top-nav">
<li class="search-parent"> <a href="javascript:void(0)" title=""><i aria-hidden="true" class="fa fa-search"></i></a>
<div class="search-box">
<div class="content">
<div class="form-control">
<input placeholder="Type to search" type="text">
<a class="search-btn" href="#"><i aria-hidden="true" class="fa fa-search"></i></a> </input></div>
<a class="close-btn" href="#">x</a> </div>
</div>
</li>
<li class="cart-parent"> <a href="javascript:void(0)" title=""> <i aria-hidden="true" class="fa fa-shopping-cart"></i> <span class="number"> 4 </span> </a>
<div class="cart-box">
<div class="content">
<div class="row">
<div class="col-xs-8"> 2 item(s) </div>
<div class="col-xs-4 text-right"> <span>$99</span> </div>
</div>
<ul>
<li> <img alt="" src="http://via.placeholder.com/80x80"/> Jean &amp; Teashirt <span>$30</span> <a class="close-btn" href="#" title="">x</a> </li>
<li> <img alt="" src="http://via.placeholder.com/80x80"/> Jean &amp; Teashirt <span>$30</span> <a class="close-btn" href="#" title="">x</a> </li>
</ul>
<div class="row">
<div class="col-xs-6"> <a class="btn btn-block btn-warning" href="#" title="View Cart">View Cart</a> </div>
<div class="col-xs-6"> <a class="btn btn-block btn-primary" href="#" title="Check out">Check out</a> </div>
</div>
</div>
</div>
</li>
<li class="visible-xs menu-icon"> <a aria-expanded="false" class="navbar-toggle collapsed" data-target="#menu" data-toggle="collapse" href="javascript:void(0)"> <i aria-hidden="true" class="fa fa-bars"></i> </a> </li>
</ul>
<div class="collapse" id="menu">
<ul class="nav navbar-nav">
<li class="right"> <a href="#">Home</a> <span class="arrow"></span>
<ul class="dm-align-2">
<li> <a href="index2.html">Home Page 2</a></li>
<li> <a href="index3.html">Home Page 3</a></li>
<li> <a href="index4.html">Home Page 4</a></li>
<li> <a href="index5.html">Home Page 5</a></li>
<li> <a href="index6.html">Home Page 6</a></li>
<li> <a href="index7.html">Home Page 7</a></li>
<li> <a href="index8.html">Home Page 8</a></li>
<li> <a href="index9.html">Home Page 9</a></li>
<li> <a href="index10.html">Home Page 10</a></li>
<li> <a href="index.html">Home Default</a></li>
</ul>
</li>
<li class="active"> <a href="{% url 'page_view' "slider-kenburns" %}">Pages</a> <span class="arrow"></span>
<ul class="dm-align-2">
<li> <a href="#">About <span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "page-about1" %}">About Style 1</a> </li>
<li> <a href="{% url 'page_view' "page-about2" %}">About Style 2</a> </li>
<li> <a href="{% url 'page_view' "page-about3" %}">About Style 3</a> </li>
<li> <a href="{% url 'page_view' "page-about4" %}">About Style 4</a> </li>
<li> <a href="{% url 'page_view' "page-about5" %}">About Me</a> </li>
</ul>
</li>
<li> <a href="#">Services <span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "page-services1" %}">Services Style 1</a> </li>
<li> <a href="{% url 'page_view' "page-services2" %}">Services Style 2</a> </li>
<li> <a href="{% url 'page_view' "page-services3" %}">Services Style 3</a> </li>
<li> <a href="{% url 'page_view' "page-services4" %}">Services Style 4</a> </li>
</ul>
</li>
<li> <a href="#">Team <span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "page-team-classic" %}">Team Classic</a> </li>
<li> <a href="{% url 'page_view' "page-team-parallax" %}">Team Parallax</a> </li>
<li> <a href="{% url 'page_view' "page-team-dark" %}">Team dark Style</a> </li>
<li> <a href="{% url 'page_view' "page-team-creative" %}">Team Creative</a> </li>
</ul>
</li>
<li> <a href="#">FAQ <span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "page-faq1" %}">FAQ Style 1</a> </li>
<li> <a href="{% url 'page_view' "page-faq2" %}">FAQ Style 2</a> </li>
</ul>
</li>
<li class="active"> <a href="#">Contact<span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "page-contact" %}">Contact Classic</a> </li>
<li> <a href="{% url 'page_view' "page-contact-left-sidebar" %}">Contact Left Sidebar</a> </li>
<li> <a href="{% url 'page_view' "page-contact-right-sidebar" %}">Contact Right Sidebar</a> </li>
<li> <a href="{% url 'page_view' "page-contact-map" %}">Full Width Map</a> </li>
<li> <a href="{% url 'page_view' "page-contact-parallax" %}">Contact Parallax</a> </li>
<li class="active"> <a href="page-contact-captcha.php">Contact With Captcha</a> </li>
</ul>
</li>
<li> <a href="#">Other Pages 1<span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "page-full-width" %}">Full Width Page</a></li>
<li> <a href="{% url 'page_view' "page-left-sidebar" %}">Left Sidebar</a></li>
<li> <a href="{% url 'page_view' "page-right-sidebar" %}">Right Sidebar</a></li>
<li> <a href="{% url 'page_view' "page-packages" %}">Package Plans</a></li>
<li> <a href="{% url 'page_view' "page-careers" %}">Careers</a></li>
<li> <a href="{% url 'page_view' "page-coming-soon" %}">Coming Soon</a></li>
</ul>
</li>
<li> <a href="#">Other Pages 2<span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "page-login" %}">Login</a></li>
<li> <a href="{% url 'page_view' "page-register" %}">Register</a></li>
<li> <a href="{% url 'page_view' "page-sitemap" %}">Sitemap</a></li>
<li> <a href="{% url 'page_view' "page-maintenance" %}">Maintenance</a></li>
<li> <a href="{% url 'page_view' "page-404" %}">404 Error Page</a></li>
<li> <a href="{% url 'page_view' "page-404-2" %}">404 Error Page 2</a></li>
</ul>
</li>
</ul>
</li>
<li> <a href="{% url 'page_view' "slider-kenburns" %}">Features</a> <span class="arrow"></span>
<ul class="dm-align-2">
<li> <a href="#">Sliders <span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "slider-kenburns" %}">KenBurns</a> </li>
<li> <a href="{% url 'page_view' "slider-parallax" %}">Parallax</a> </li>
<li> <a href="{% url 'page_view' "slider-3d" %}">3D</a> </li>
<li> <a href="{% url 'page_view' "slider-carousel" %}">Carousel</a> </li>
<li> <a href="{% url 'page_view' "slider-gallery" %}">Gallery</a> </li>
<li> <a href="{% url 'page_view' "slider-scroll-effect" %}">Scroll Efects</a> </li>
<li> <a href="{% url 'page_view' "slider-vimeo" %}">Vimeo Video</a> </li>
<li> <a href="{% url 'page_view' "slider-youtube" %}">Youtube Video</a> </li>
</ul>
</li>
<li> <a href="#">Headers <span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="index7.html">Header Light</a> </li>
<li> <a href="{% url 'page_view' "page-about5" %}">Header Dark</a> </li>
<li> <a href="index4.html">Header Modern</a> </li>
<li> <a href="index.html">Header Transparent</a> </li>
<li> <a href="{% url 'page_view' "page-team-creative" %}">Header Creative</a> </li>
<li> <a href="index.html">Header Left Logo</a> </li>
<li> <a href="{% url 'page_view' "page-team-creative" %}">Header Center Logo</a> </li>
<li> <a href="index7.html">Header White</a> </li>
</ul>
</li>
<li> <a href="#">Menu Styles <span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="index.html">Menu Transparent</a> </li>
<li> <a href="index2.html">Menu Left logo</a> </li>
<li> <a href="index7.html">Menu light</a> </li>
<li> <a href="index2.html">Menu Dark</a> </li>
<li> <a href="{% url 'page_view' "page-team-creative" %}">Menu Center Logo</a> </li>
<li> <a href="index4.html">Menu Boxed</a> </li>
<li> <a href="{% url 'page_view' "page-team-creative" %}">Menu Center</a> </li>
</ul>
</li>
<li> <a href="#">Loading Styles<span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "loading-style1" %}">Loading Style 1</a> </li>
<li> <a href="{% url 'page_view' "loading-style2" %}">Loading Style 2</a> </li>
<li> <a href="{% url 'page_view' "loading-style3" %}">Loading Style 3</a> </li>
<li> <a href="{% url 'page_view' "loading-style4" %}">Loading Style 4</a> </li>
<li> <a href="{% url 'page_view' "loading-style5" %}">Loading Style 5</a> </li>
<li> <a href="{% url 'page_view' "loading-style6" %}">Loading Style 6</a> </li>
<li> <a href="{% url 'page_view' "loading-style7" %}">Loading Style 7</a> </li>
<li> <a href="{% url 'page_view' "loading-style8" %}">Loading Style 8</a> </li>
<li> <a href="{% url 'page_view' "loading-style9" %}">Loading Style 9</a> </li>
<li> <a href="{% url 'page_view' "loading-style10" %}">Loading Style 10</a> </li>
</ul>
</li>
<li> <a href="#">Footer Styles<span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="index3.html">Footer Dark</a> </li>
<li> <a href="index4.html">Footer Light</a> </li>
<li> <a href="index3.html">Footer Simple</a> </li>
<li> <a href="{% url 'page_view' "page-about1" %}">Footer Parallax</a> </li>
<li> <a href="index8.html">Footer Big</a> </li>
<li> <a href="index5.html">Footer Modern</a> </li>
<li> <a href="index10.html">Footer With Map</a> </li>
<li> <a href="{% url 'page_view' "page-about1" %}">Footer Transparent</a> </li>
<li> <a href="index4.html">Footer Classic</a> </li>
</ul>
</li>
<li> <a href="#">Videos<span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "shortcodes-videos" %}">Youtube Videos</a> </li>
<li> <a href="{% url 'page_view' "shortcodes-videos" %}">Vimeo Videos</a> </li>
<li> <a href="{% url 'page_view' "shortcodes-videos" %}">HTML 5 Videos</a> </li>
</ul>
</li>
<li> <a href="#">Layered PSD Files</a> </li>
<li> <a href="#">Unlimited Colors</a> </li>
<li> <a href="#">Wide &amp; Boxed</a> </li>
</ul>
</li>
<li class="mega-menu"> <a href="{% url 'page_view' "header-style3" %}">Portfolio</a> <span class="arrow"></span>
<ul>
<li> <a href="#" title="home samples">Portfolio columns</a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "portfolio-1-columns" %}"><i class="fa fa-angle-right"></i>   One Column</a> </li>
<li> <a href="{% url 'page_view' "portfolio-2-columns" %}"><i class="fa fa-angle-right"></i>   Two Column</a> </li>
<li> <a href="{% url 'page_view' "portfolio-3-columns" %}"><i class="fa fa-angle-right"></i>   Three Column</a> </li>
<li> <a href="{% url 'page_view' "portfolio-4-columns" %}"><i class="fa fa-angle-right"></i>   Four Column</a> </li>
<li> <a href="{% url 'page_view' "portfolio-5-columns" %}"><i class="fa fa-angle-right"></i>   Five Column</a> </li>
<li> <a href="{% url 'page_view' "portfolio-6-columns" %}"><i class="fa fa-angle-right"></i>   Six Column</a> </li>
</ul>
</li>
<li> <a href="#">Portfolio Styles</a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "portfolio-masonry" %}"><i class="fa fa-angle-right"></i>   Masonry</a> </li>
<li> <a href="{% url 'page_view' "portfolio-masonry-projects" %}"><i class="fa fa-angle-right"></i>   Masonry-Projects</a> </li>
<li> <a href="{% url 'page_view' "portfolio-mosaic" %}"><i class="fa fa-angle-right"></i>   Mosaic</a> </li>
<li> <a href="{% url 'page_view' "portfolio-mosaic-flat" %}"><i class="fa fa-angle-right"></i>   Mosaic-Flat</a> </li>
<li> <a href="{% url 'page_view' "portfolio-mosaic-projects" %}"><i class="fa fa-angle-right"></i>   Mosaic-Projects</a> </li>
<li> <a href="{% url 'page_view' "portfolio-slider-projects" %}"><i class="fa fa-angle-right"></i>   slider-projects</a> </li>
</ul>
</li>
<li> <a href="#">Portfolio Styles</a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "portfolio-full-width" %}"><i class="fa fa-angle-right"></i>   Full Width</a> </li>
<li> <a href="{% url 'page_view' "portfolio-gallery" %}"><i class="fa fa-angle-right"></i>   Gallery</a> </li>
<li> <a href="{% url 'page_view' "portfolio-classic" %}"><i class="fa fa-angle-right"></i>   Classic</a> </li>
<li> <a href="{% url 'page_view' "portfolio-nospace" %}"><i class="fa fa-angle-right"></i>   No Space</a> </li>
<li> <a href="{% url 'page_view' "portfolio-boxed-size" %}"><i class="fa fa-angle-right"></i>   Boxed Size</a> </li>
<li> <a href="{% url 'page_view' "portfolio-modern" %}"><i class="fa fa-angle-right"></i>   Modern</a> </li>
</ul>
</li>
<li> <a href="#">Portfolio Single Page</a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "portfolio-parallax" %}"><i class="fa fa-angle-right"></i>   Parallax Image</a> </li>
<li> <a href="{% url 'page_view' "portfolio-video" %}"><i class="fa fa-angle-right"></i>   Video Background</a> </li>
<li> <a href="{% url 'page_view' "portfolio-left-sidebar" %}"><i class="fa fa-angle-right"></i>   Left Sidebar</a> </li>
<li> <a href="{% url 'page_view' "portfolio-right-sidebar" %}"><i class="fa fa-angle-right"></i>   Right Sidebar</a> </li>
<li> <a href="{% url 'page_view' "portfolio-carousel" %}"><i class="fa fa-angle-right"></i>   Carousel</a> </li>
<li> <a href="{% url 'page_view' "portfolio-fullwidth-image" %}"><i class="fa fa-angle-right"></i>   Full width Image</a> </li>
</ul>
</li>
</ul>
</li>
<li class="mega-menu five-col"> <a href="carousel-sliders.html">Shortcodes</a> <span class="arrow"></span>
<ul>
<li> <a href="#">Shortcodes 1</a> <span class="arrow"></span>
<ul>
<li><a href="{% url 'page_view' "shortcodes-accordions" %}"><i class="fa fa-plus-circle"></i>   Accordions</a> </li>
<li><a href="{% url 'page_view' "shortcodes-alerts" %}"><i aria-hidden="true" class="fa fa-exclamation"></i>   Alerts</a> </li>
<li><a href="{% url 'page_view' "shortcodes-animations" %}"><i class="fa fa-bars"></i>   Animations</a> </li>
<li><a href="{% url 'page_view' "shortcodes-blockquotes" %}"><i aria-hidden="true" class="fa fa-quote-right"></i>   Blockquotes</a> </li>
<li><a href="{% url 'page_view' "shortcodes-breadcrumbs" %}"><i aria-hidden="true" class="fa fa-share"></i>   Breadcrumbs</a> </li>
<li><a href="{% url 'page_view' "shortcodes-buttons" %}"><i aria-hidden="true" class="fa fa-external-link"></i>   Buttons</a> </li>
<li><a href="{% url 'page_view' "shortcodes-call-to-action" %}"><i aria-hidden="true" class="fa fa-level-up"></i>   Call to Action</a> </li>
<li><a href="{% url 'page_view' "shortcodes-clients-logos" %}"><i aria-hidden="true" class="fa fa-user"></i>   Clients Logos</a> </li>
<li><a href="{% url 'page_view' "shortcodes-carousel-sliders" %}"><i aria-hidden="true" class="fa fa-sort"></i>   Carousel Sliders</a> </li>
<li><a href="{% url 'page_view' "shortcodes-counters" %}"><i aria-hidden="true" class="fa fa-text-height"></i>   Counters</a> </li>
</ul>
</li>
<li> <a href="#">Shortcodes 2</a> <span class="arrow"></span>
<ul>
<li><a href="{% url 'page_view' "shortcodes-content-boxes" %}"><i aria-hidden="true" class="fa fa-th"></i>   Content Boxes</a> </li>
<li><a href="{% url 'page_view' "shortcodes-data-tables" %}"><i aria-hidden="true" class="fa fa-table"></i>   Data Tables</a> </li>
<li><a href="{% url 'page_view' "shortcodes-date-pickers" %}"><i aria-hidden="true" class="fa fa-calendar"></i>   Date Pickers</a> </li>
<li><a href="{% url 'page_view' "shortcodes-dropcaps" %}"><i aria-hidden="true" class="fa fa-font"></i>   Dropcap &amp; Highlight</a> </li>
<li><a href="{% url 'page_view' "shortcodes-dividers" %}"><i aria-hidden="true" class="fa fa-minus"></i>   Dividers</a> </li>
<li><a href="{% url 'page_view' "shortcodes-file-uploads" %}"><i aria-hidden="true" class="fa fa-upload"></i>   File Uploads</a> </li>
<li><a href="{% url 'page_view' "shortcodes-forms" %}"><i aria-hidden="true" class="fa fa-envelope"></i>   Forms</a> </li>
<li><a href="{% url 'page_view' "shortcodes-grids" %}"><i aria-hidden="true" class="fa fa-th-list"></i>   Grids</a> </li>
<li><a href="{% url 'page_view' "shortcodes-heading-styles" %}"><i aria-hidden="true" class="fa fa-text-height"></i>   Heading Styles</a> </li>
<li><a href="{% url 'page_view' "shortcodes-hover-styles" %}"><i aria-hidden="true" class="fa fa-picture-o"></i>   Hover Styles</a> </li>
</ul>
</li>
<li> <a href="#">Shortcodes 3</a> <span class="arrow"></span>
<ul>
<li><a href="{% url 'page_view' "shortcodes-icon-boxes" %}"><i aria-hidden="true" class="fa fa-th-large"></i>   Icon Boxes</a> </li>
<li><a href="{% url 'page_view' "shortcodes-icon-circles" %}"><i aria-hidden="true" class="fa fa-circle-o"></i>   Icon Circles</a> </li>
<li><a href="{% url 'page_view' "shortcodes-countdown-timers" %}"><i aria-hidden="true" class="fa fa-bars"></i>   Countdown Timers</a> </li>
<li><a href="{% url 'page_view' "shortcodes-icon-lists" %}"><i aria-hidden="true" class="fa fa-list"></i>   Icon Lists</a> </li>
<li><a href="{% url 'page_view' "shortcodes-images" %}"><i aria-hidden="true" class="fa fa-picture-o"></i>   Images</a> </li>
<li><a href="{% url 'page_view' "shortcodes-labels-and-badges" %}"><i aria-hidden="true" class="fa fa-adjust"></i>   Labels and Badges</a> </li>
<li><a href="{% url 'page_view' "shortcodes-lightbox" %}"><i aria-hidden="true" class="fa fa-th"></i>   Lightbox</a> </li>
<li><a href="{% url 'page_view' "shortcodes-lists" %}"><i aria-hidden="true" class="fa fa-list-ul"></i>   Lists</a> </li>
<li><a href="{% url 'page_view' "shortcodes-maps" %}"><i aria-hidden="true" class="fa fa-map-marker"></i>   Maps</a> </li>
<li><a href="{% url 'page_view' "shortcodes-modal-popup" %}"><i aria-hidden="true" class="fa fa-search-plus"></i>   Modal Popup</a> </li>
</ul>
</li>
<li> <a href="#">Shortcode 4</a> <span class="arrow"></span>
<ul>
<li><a href="{% url 'page_view' "shortcodes-pagenation" %}"><i aria-hidden="true" class="fa fa-exchange"></i>   Pagenation</a> </li>
<li><a href="{% url 'page_view' "shortcodes-parallax-backgrounds" %}"><i aria-hidden="true" class="fa fa-align-center"></i>   Parallax Backgrounds</a> </li>
<li><a href="{% url 'page_view' "shortcodes-pricing-tables" %}"><i aria-hidden="true" class="fa fa-table"></i>   Pricing Tables</a> </li>
<li><a href="{% url 'page_view' "shortcodes-pie-charts" %}"><i aria-hidden="true" class="fa fa-pie-chart"></i>   Pie Charts</a> </li>
<li><a href="{% url 'page_view' "shortcodes-pricing-badges" %}"><i class="fa fa-external-link"></i>   Pricing Badges</a> </li>
<li><a href="{% url 'page_view' "shortcodes-progress-bars" %}"><i aria-hidden="true" class="fa fa-outdent"></i>   Progress Bars</a> </li>
<li><a href="{% url 'page_view' "shortcodes-process-steps" %}"><i aria-hidden="true" class="fa fa-long-arrow-right"></i>   Process Steps</a> </li>
<li><a href="{% url 'page_view' "shortcodes-post-styles" %}"><i aria-hidden="true" class="fa fa-pencil"></i>   Post Styles</a> </li>
<li><a href="{% url 'page_view' "shortcodes-toogle-switches" %}"><i aria-hidden="true" class="fa fa-toggle-on"></i>   Toogle Switches</a> </li>
<li><a href="{% url 'page_view' "shortcodes-timeline" %}"><i aria-hidden="true" class="fa fa-align-left"></i>   Timeline</a> </li>
</ul>
</li>
<li> <a href="#">Shortcode 5</a> <span class="arrow"></span>
<ul>
<li><a href="{% url 'page_view' "shortcodes-star-ratings" %}"><i aria-hidden="true" class="fa fa-star-half-o"></i>   Star Ratings</a> </li>
<li><a href="{% url 'page_view' "shortcodes-sections" %}"><i aria-hidden="true" class="fa fa-square-o"></i>   Sections</a> </li>
<li><a href="{% url 'page_view' "shortcodes-social-icons" %}"><i aria-hidden="true" class="fa fa-twitter"></i>   Social Icons</a> </li>
<li><a href="{% url 'page_view' "shortcodes-tabs" %}"><i aria-hidden="true" class="fa fa-th-large"></i>   Tabs</a> </li>
<li><a href="{% url 'page_view' "shortcodes-team" %}"><i aria-hidden="true" class="fa fa-user"></i>   Team</a> </li>
<li><a href="{% url 'page_view' "shortcodes-testimonials" %}"><i class="fa fa-pencil-square"></i>   Testimonials</a> </li>
<li><a href="{% url 'page_view' "shortcodes-tooltips" %}"><i aria-hidden="true" class="fa fa-font"></i>   Tooltips</a> </li>
<li><a href="{% url 'page_view' "shortcodes-toogles" %}"><i aria-hidden="true" class="fa fa-toggle-on"></i>   Toogles</a> </li>
<li><a href="{% url 'page_view' "shortcodes-typography" %}"><i aria-hidden="true" class="fa fa-text-height"></i>   Typography</a> </li>
<li><a href="{% url 'page_view' "shortcodes-videos" %}"><i aria-hidden="true" class="fa fa-play-circle"></i>   Videos</a> </li>
</ul>
</li>
</ul>
</li>
<li class="right"> <a href="#">Blog</a> <span class="arrow"></span>
<ul class="dm-align-2">
<li> <a href="#">Classic <span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "blog-full-width" %}">Full Width</a> </li>
<li> <a href="{% url 'page_view' "blog-left-sidebar" %}">Left Sidebar</a> </li>
<li> <a href="{% url 'page_view' "blog-right-sidebar" %}">Right Sidebar</a> </li>
</ul>
</li>
<li> <a href="#">Grids <span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "blog-1-columns" %}">One Column</a> </li>
<li> <a href="{% url 'page_view' "blog-2-columns" %}">Two Column</a> </li>
<li> <a href="{% url 'page_view' "blog-3-columns" %}">Three Column</a> </li>
<li> <a href="{% url 'page_view' "blog-4-columns" %}">Four Column</a> </li>
<li> <a href="{% url 'page_view' "blog-5-columns" %}">Five Column</a> </li>
<li> <a href="{% url 'page_view' "blog-6-columns" %}">Six Column</a> </li>
</ul>
</li>
<li> <a href="#">Default<span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "blog-default-full-width" %}">Full Width</a> </li>
<li> <a href="{% url 'page_view' "blog-default-left-sidebar" %}">Left Sidebar</a> </li>
<li> <a href="{% url 'page_view' "blog-default-right-sidebar" %}">Right Sidebar</a> </li>
<li> <a href="{% url 'page_view' "blog-default-author" %}">Author Page</a> </li>
<li> <a href="{% url 'page_view' "blog-default-comments" %}">Blog Comments</a> </li>
</ul>
</li>
<li> <a href="#">Thumbnail<span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "blog-full-width-thumbnail" %}">Full Width</a> </li>
<li> <a href="{% url 'page_view' "blog-left-sidebar-thumbnail" %}">Left Sidebar</a> </li>
<li> <a href="{% url 'page_view' "blog-right-sidebar-thumbnail" %}">Right Sidebar</a> </li>
<li> <a href="{% url 'page_view' "blog-author-thumbnail" %}">Author Page</a> </li>
<li> <a href="{% url 'page_view' "blog-comments-thumbnail" %}">Blog Comments</a> </li>
</ul>
</li>
<li> <a href="#">Single Post<span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "blog-image-post" %}">Image Post</a> </li>
<li> <a href="{% url 'page_view' "blog-video-post" %}">Video Post</a> </li>
<li> <a href="{% url 'page_view' "blog-gallery-post" %}">Gallery Post</a> </li>
<li> <a href="{% url 'page_view' "blog-sidebar-post" %}">Sidebar Post</a> </li>
</ul>
</li>
</ul>
</li>
<li class="right"> <a href="#">Shop</a> <span class="arrow"></span>
<ul>
<li> <a href="#">Default<span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "shop-full-width" %}">Full Width</a> </li>
<li> <a href="{% url 'page_view' "shop-left-sidebar" %}">Left Sidebar</a> </li>
<li> <a href="{% url 'page_view' "shop-right-sidebar" %}">Right Sidebar</a> </li>
</ul>
</li>
<li> <a href="#">Grids <span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "shop-2-columns" %}">Two Column</a> </li>
<li> <a href="{% url 'page_view' "shop-3-columns" %}">Three Column</a> </li>
<li> <a href="{% url 'page_view' "shop-4-columns" %}">Four Column</a> </li>
<li> <a href="{% url 'page_view' "shop-5-columns" %}">Five Column</a> </li>
<li> <a href="{% url 'page_view' "shop-6-columns" %}">Six Column</a> </li>
</ul>
</li>
<li> <a href="#">Single Product<span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "shop-single-full-width" %}">Full Width</a> </li>
<li> <a href="{% url 'page_view' "shop-single-left-sidebar" %}">Left Sidebar</a> </li>
<li> <a href="{% url 'page_view' "shop-single-right-sidebar" %}">Right Sidebar</a> </li>
<li> <a href="{% url 'page_view' "shop-single-both-sidebar" %}">both Sidebars</a> </li>
</ul>
</li>
<li> <a href="#">Order Process<span class="sub-arrow dark pull-right"><i aria-hidden="true" class="fa fa-angle-right"></i></span> </a> <span class="arrow"></span>
<ul>
<li> <a href="{% url 'page_view' "shop-cart" %}">Shoping Cart</a> </li>
<li> <a href="{% url 'page_view' "shop-checkout" %}">Checkout</a> </li>
<li> <a href="{% url 'page_view' "shop-wishlist" %}">Wishlist</a> </li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<!--end menu-->
</div>
<!--end menu-->
<div class="clearfix"></div>
<section class="section-side-image clearfix">
<div class="img-holder col-md-12 col-sm-12 col-xs-12">
<div class="background-imgholder" style="background:url(http://via.placeholder.com/1500x1000);"><img alt="" class="nodisplay-image" src="http://via.placeholder.com/1500x1000"> </img></div>
</div>
<div class="container-fluid">
<div class="row">
<div class="col-md-12 col-sm-12 col-xs-12 clearfix nopadding">
<div class="header-inner less-height">
<div class="overlay">
<div class="text text-center">
<h3 class="uppercase text-white less-mar-1 title">Contact with Captcha</h3>
<h6 class="uppercase text-white sub-title">Get Many More Features</h6>
</div>
</div>
</div>
</div>
</div>
</div>
</section>
<div class=" clearfix"></div>
<!--end header section -->
<section>
<div class="pagenation-holder">
<div class="container">
<div class="row">
<div class="col-md-6">
<h4>Contact with Captcha</h4>
</div>
<div class="col-md-6">
<ol class="breadcrumb">
<li><a href="#">Home</a></li>
<li><a href="#">Pages</a></li>
<li class="current"><a href="#">Contact with Captcha</a></li>
</ol>
</div>
</div>
</div>
</div>
</section>
<div class="clearfix"></div>
<!--end section-->
<section class="sec-padding section-light">
<div class="container">
<div class="row">
<div class="col-md-8">
<h3 class="uppercase">Contact Form</h3>
<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Suspendisse et justo. Praesent mattis commodo augue. Aliquam ornare hendrerit consectetuer adipiscing elit. Suspendisse et justo. augue.</p>
<br/>
<br/>
<div class="text-box white padding-4">
<div class="smartforms-modal-body">
<div class="smart-wrap">
<div class="smart-forms smart-container transparent wrap-full">
<div class="form-body no-padd">
<form action="php/smartprocess.php" id="smart-form" method="post">
<div class="section">
<label class="field prepend-icon">
<input class="gui-input" id="sendername" name="sendername" placeholder="Enter name" type="text"/>
<span class="field-icon"><i class="fa fa-user"></i></span>
</label>
</div><!-- end section -->
<div class="section">
<label class="field prepend-icon">
<input class="gui-input" id="emailaddress" name="emailaddress" placeholder="Email address" type="email"/>
<span class="field-icon"><i class="fa fa-envelope"></i></span>
</label>
</div><!-- end section -->
<div class="section">
<label class="field prepend-icon">
<input class="gui-input" id="telephone" name="telephone" placeholder="Enter Telephone..." type="text"/>
<span class="field-icon"><i class="fa fa-phone-square"></i></span>
</label>
</div><!-- end section -->
<div class="section">
<label class="field prepend-icon">
<input class="gui-input" id="sendersubject" name="sendersubject" placeholder="Enter subjec" type="text"/>
<span class="field-icon"><i class="fa fa-lightbulb-o"></i></span>
</label>
</div><!-- end section -->
<div class="section">
<label class="field prepend-icon">
<textarea class="gui-textarea" id="sendermessage" name="sendermessage" placeholder="Enter message"></textarea>
<span class="field-icon"><i class="fa fa-comments"></i></span>
<span class="input-hint"> <strong>Hint:</strong> Please enter between 80 - 300 characters.</span>
</label>
</div><!-- end section -->
<div class="section">
<div class="smart-widget sm-left sml-120">
<label class="field">
<input class="gui-input sfcode" id="captcha" maxlength="6" name="captcha" placeholder="Enter CAPTCHA" type="text"/>
</label>
<label class="button captcode">
<img alt="captcha" id="captchax" src="php/captcha/captcha.php?&lt;?php echo time();?&gt;"/>
<span class="refresh-captcha"><i class="fa fa-refresh"></i></span>
</label>
</div><!-- end .smart-widget section -->
</div><!-- end section -->
<div class="result"></div><!-- end .result  section -->
<!-- end .form-body section -->
<div class="form-footer text-left">
<button class="button btn-primary" data-btntext-sending="Sending..." type="submit">Submit</button>
<button class="button" type="reset"> Cancel </button>
</div><!-- end .form-footer section -->
</form>
</div><!-- end .form-body section -->
</div><!-- end .smart-forms section -->
</div><!-- end .smart-wrap section -->
</div></div><!-- end .smart-wrap section -->
<!-- end .smart-forms section -->
</div>
<!--end item-->
<div class="col-md-4 text-left">
<h4>Address Info</h4>
<h6>Company name</h6>
<p>3096 Cemetery Hollow Street, Houston, TX 77099
              Telephone: +1 1234-567-89000
              FAX: +1 0123-4567-8900</p>
<br/>
<p>E-mail: mail@companyname.com</p>
<p>Website: www.yoursitename.com</p>
</div>
<!--end item-->
</div>
</div>
</section>
<div class="clearfix"></div>
<!-- end section -->
<section class="section-primary">
<div class="container">
<div class="divider-line solid light opacity-1"></div>
<div class="row sec-padding-6">
<ul class="clients-list grid-cols-5 hover-7 noborder">
<li><a href="#"><img alt="" src="http://via.placeholder.com/225x120"/></a></li>
<li><a href="#"><img alt="" src="http://via.placeholder.com/225x120"/></a></li>
<li><a href="#"><img alt="" src="http://via.placeholder.com/225x120"/></a></li>
<li><a href="#"><img alt="" src="http://via.placeholder.com/225x120"/></a></li>
<li><a href="#"><img alt="" src="http://via.placeholder.com/225x120"/></a></li>
</ul>
</div>
</div>
</section>
<div class="clearfix"></div>
<!-- end section -->
<div class="section-dark sec-padding">
<div class="container">
<div class="row">
<div class="col-md-3 col-sm-12 colmargin clearfix margin-bottom">
<div class="fo-map">
<div class="footer-logo"><img alt="" src="{% static "images/logo/logo.png" %}  "/></div>
<address>
<strong class="text-white">Address:</strong>
<br/>
        No.28 - 63739 street lorem ipsum,
        <br/>
        ipsum City, Country
        </address>
<span><strong class="text-white">Phone:</strong> + 1 (234) 567 8901</span><br/>
<span><strong class="text-white">Email:</strong> support@yoursite.com </span><br/>
<span><strong class="text-white">Fax:</strong> + 1 (234) 567 8901</span>
<ul class="footer-social-icons primary left-align icons-plain text-center">
<li><a class="twitter" href="#"><i class="fa fa-twitter"></i></a></li>
<li><a href="#"><i class="fa fa-facebook"></i></a></li>
<li><a class="active" href="#"><i class="fa fa-google-plus"></i></a></li>
<li><a href="#"><i class="fa fa-linkedin"></i></a></li>
<li><a href="#"><i class="fa fa-dribbble"></i></a></li>
</ul>
</div>
</div>
<!--end item-->
<div class="col-md-3 col-xs-12 clearfix margin-bottom">
<h4 class="text-white uppercase less-mar3 font-weight-5">Popular Services</h4>
<div class="clearfix"></div>
<div class="footer-title-bottomstrip"></div>
<ul class="footer-quick-links-4 white">
<li><a href="#"><i class="fa fa-angle-right"></i> Placerat bibendum</a></li>
<li><a href="#"><i class="fa fa-angle-right"></i> Ullamcorper odio nec turpis</a></li>
<li><a href="#"><i class="fa fa-angle-right"></i> Aliquam porttitor vestibulum ipsum</a></li>
<li><a href="#"><i class="fa fa-angle-right"></i> Lobortis enim nec nisi</a></li>
<li><a href="#"><i class="fa fa-angle-right"></i> Placerat bibendum</a></li>
<li><a href="#"><i class="fa fa-angle-right"></i> Lobortis enim nec nisi</a></li>
<li><a href="#"><i class="fa fa-angle-right"></i> Lobortis enim nec nisi</a></li>
</ul>
</div>
<!--end item-->
<div class="col-md-3 col-sm-12 col-xs-12 bmargin clearfix margin-bottom">
<div class="item-holder">
<h4 class="text-white uppercase less-mar3">Recent Posts</h4>
<div class="fo-title-bottom-line white"></div>
<div class="clearfix"></div>
<div class="fo-posts">
<div class="imgbox-medium left"><img alt="" class="img-responsive" src="http://via.placeholder.com/300x300"/></div>
<div class="text-box-right">
<h6 class="less-mar3 uppercase nopadding text-white"><a href="#">Aenean arcu tortor</a></h6>
<p>Lorem ipsum dolor</p>
<div class="post-info"> <span>By John Doe</span><span>May 15</span> </div>
</div>
</div>
<div class=" divider-line light solid light opacity-1 "></div>
<div class="clearfix"></div>
<br>
<div class="fo-posts">
<div class="imgbox-medium left"><img alt="" class="img-responsive" src="http://via.placeholder.com/300x300"/></div>
<div class="text-box-right">
<h6 class="less-mar3 uppercase nopadding text-white"><a href="#">Maecenas sed nisl amet</a></h6>
<p>Lorem ipsum dolor</p>
<div class="post-info"> <span>By John Doe</span><span>May 15</span> </div>
</div>
</div>
</br></div>
</div>
<!--end item-->
<div class="col-md-3 col-xs-12 clearfix margin-bottom">
<h4 class="text-white uppercase less-mar3 font-weight-5">Need Help</h4>
<div class="clearfix"></div>
<div class="footer-title-bottomstrip"></div>
<ul class="footer-quick-links-4 white">
<li><a href="#"><i class="fa fa-angle-right"></i> Placerat bibendum</a></li>
<li><a href="#"><i class="fa fa-angle-right"></i> Ullamcorper odio nec turpis</a></li>
<li><a href="#"><i class="fa fa-angle-right"></i> Aliquam porttitor vestibulum ipsum</a></li>
<li><a href="#"><i class="fa fa-angle-right"></i> Lobortis enim nec nisi</a></li>
<li><a href="#"><i class="fa fa-angle-right"></i> Placerat bibendum</a></li>
<li><a href="#"><i class="fa fa-angle-right"></i> Lobortis enim nec nisi</a></li>
<li><a href="#"><i class="fa fa-angle-right"></i> Ullamcorper odio nec turpis</a></li>
</ul>
</div>
<!--end item-->
<div class="clearfix"></div>
<div class="col-divider-margin-5"></div>
<div class="col-md-12">
<input class="bb-newsletter" placeholder="Your Name" type="search"/>
<input class="bb-newsletter-email" placeholder="Email Address" type="search"/>
<input class="bb-newsletter-btn" name="search" type="submit" value="Submit"/>
</div>
<!--end newsletter-->
</div>
</div>
</div>
<div class="clearfix"></div>
<!-- end section -->
<section class="sec-padding-6">
<div class="container">
<div class="row">
<div class="fo-copyright-holder text-center">
            
            Copyright © 2017 l yourdomain.com. All rights reserved. </div>
</div>
</div>
</section>
<div class="clearfix"></div>
<!-- end section -->
<a class="scrollup" href="#"></a><!-- end scroll to top of the page-->
</div>
<!--end site wrapper-->
</div>
{% endblock %}
