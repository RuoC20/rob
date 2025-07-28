obj_need={}

def aa():
    from lxml import html

    # 示例HTML内容
    html_content = r'''










    <!doctype html>
    <html lang="zh-CN">



    <style type="text/css">
    	.jsqh {
    		float: left;
    	    height: 50px;
    	    padding: 15px 15px;
    	    font-size: 18px;
    	    line-height: 20px;
    	}

    	.top-input {
    	    margin: 0!important;

    	}

    	.inp-name {
    		display: inline-block;
    		height: 50px;
    		margin-right: 10px;
    		line-height: 50px;
    		color: #fff;
    		font-size: 16px;
    	}

    @media (max-width: 767px) {
    	.navbar-form {
    	border: 0!important
    	}
    	.role-inp {
    		display: inline-block!important;
    		width: 72%!important
    	}
    }
    </style>
    <head>
    	<title>&nbsp;</title>









    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="Copyright" content="zfsoft" />	
    <link rel="icon" href="/logo/favicon.ico?t=1740186881473" type="image/x-icon" />
    <link rel="shortcut icon" href="/logo/favicon.ico?t=1740186881473" type="image/x-icon" />
    <style type="text/css">	
    	.active{font-weight: bolder;}
    	#navbar-tabs li{ margin-top: 2px;}
    	#navbar-tabs li a{ border-top: 2px solid transparent;}
    	#navbar-tabs li.active a{border-top: 2px solid #0770cd;}
    </style>



    <!--jQuery核心框架库 -->
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/js/other_jquery/jquery.min.js?ver=29002685"></script>
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/js/jquery-migrate.min.js?ver=29002685"></script>
    <!--jQuery浏览器检测 -->
    <script type="text/javascript" src="/js/browse/browse-judge.js?ver=29002685"></script>
    <script type="text/javascript">
    	//浏览器版本验证
    	var broswer = broswer();
    	if(broswer.msie==true||broswer.safari==true||broswer.mozilla==true||broswer.chrome==true){
    		if(broswer.msie==true&&broswer.version<9){
    		   window.location.href = _path+"/xtgl/init_cxBrowser.html";
    		}
    	}else{
    		 window.location.href = _path+"/xtgl/init_cxBrowser.html";
    	}
    </script>
    <script type="text/javascript">
    var _path 				= "";
    var _systemPath 		= "";
    var _stylePath 			= "/zftal-ui-v5-1.0.2";
    var _reportPath 		= "http://210.45.128.84:80/WebReport";
    var _refreshInterval	= "10";
    var _localeKey 			= "zh_CN";
    console.log('zou')
    </script>
    <!--
    jquery.ui 需要在bootstrap之前加载，解决冲突问题
    http://blog.csdn.net/remote_roamer/article/details/14105999
    -->
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/js/jquery-ui-custom.contact-1.0.0.js?ver=29002685"></script>
    <!--Bootstrap布局框架-->
    <link rel="stylesheet" type="text/css" href="/zftal-ui-v5-1.0.2/assets/plugins/bootstrap/css/bootstrap.min.css?ver=29002685" />
    <link rel="stylesheet" type="text/css" href="/zftal-ui-v5-1.0.2/assets/css/error.css?ver=29002685" />

    <link rel="stylesheet" type="text/css" href="/zftal-ui-v5-1.0.2/assets/css/zftal-ui.css?ver=29002685" />

    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/plugins/bootstrap/js/bootstrap.min.js?ver=29002685" charset="utf-8"></script>
    <!--jQuery常用工具扩展库：基础工具,资源加载工具,元素尺寸相关工具 -->
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/js/zftal/jquery.utils.contact-min.js?ver=29002685" charset="utf-8"></script>
    <!--jQuery基础工具库：$.browser,$.cookie,$.actual等 -->
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/js/zftal/jquery.plugins.contact-min.js?ver=29002685" charset="utf-8"></script>
    <!--jQuery自定义event事件库 -->
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/js/zftal/jquery.events.contact-min.js?ver=29002685" charset="utf-8"></script>
    <!--JavaScript对象扩展库：Array,Date,Number,String -->

    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/js/zftal/jquery.extends.contact-min.js?ver=29002685" charset="utf-8"></script>

    <!--Bootbox弹窗插件-->
    <link rel="stylesheet" type="text/css" href="/zftal-ui-v5-1.0.2/assets/plugins/bootbox/css/bootbox.css?ver=29002685" />
    <script src="/zftal-ui-v5-1.0.2/assets/plugins/bootbox/bootbox.concat-min.js?ver=29002685" type="text/javascript" charset="utf-8"></script>
    <script src="/zftal-ui-v5-1.0.2/assets/plugins/bootbox/lang/zh_CN.js?ver=29002685" type="text/javascript" charset="utf-8"></script>

    <!--jQuery模拟滚动条库-->
    <link rel="stylesheet" type="text/css" href="/zftal-ui-v5-1.0.2/assets/plugins/customscrollbar/css/jquery.mCustomScrollbar.min.css?ver=29002685" />
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/plugins/customscrollbar/js/jquery.mCustomScrollbar.min.js?ver=29002685" charset="utf-8"></script>
    <!--jQuery.chosen美化插件-->
    <link rel="stylesheet" type="text/css" href="/zftal-ui-v5-1.0.2/assets/plugins/chosen/css/chosen-min.css?ver=29002685" />
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/plugins/chosen/jquery.choosen.concat-min.js?ver=29002685" charset="utf-8"></script>
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/plugins/chosen/lang/zh_CN-min.js?ver=29002685" charset="utf-8"></script>
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/js/utils/jquery.utils.pinyin.min.js?ver=29002685" charset="utf-8"></script>
    <!--[if lt IE 9]>
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/js/html5shiv.min.js?ver=29002685" charset="utf-8"></script>
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/js/respond.min.js?ver=29002685" charset="utf-8"></script>
    <![endif]-->
    <!--业务框架jQuery全局设置和通用函数库-->
    <script type="text/javascript" src="/js/jquery.zftal.contact-min.js?ver=29002685"></script>
    <!--国际化js库 -->
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/plugins/i18n/jquery.i18n-min.js?ver=29002685" charset="utf-8"></script>
    <!--全局国际化js. -->
    <script type="text/javascript" src="/js/globalweb/i18n-global_zh_CN.js?ver=29002685" charset="utf-8"></script>
    <!--业务框架前端脚本国际化库-->
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/js/zftal/lang/jquery.zftal_zh_CN-min.js?ver=29002685"></script>
    <!--密码强弱判断-->
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/js/utils/jquery.utils.strength.min.js?ver=29002685"></script>
    <!--jQuery浏览器检测 -->
    <script type="text/javascript" src="/js/globalweb/comp/xtgl/device.js?ver=29002685"></script>









    <script type="text/javascript">

    	var _path 		= "";
    	var _systemPath = "";
    	var _stylePath  = "/zftal-ui-v5-1.0.2";
    	var _reportPath = "http://210.45.128.84:80/WebReport";
    	var _localeKey 			= "zh_CN";


    	jQuery(function($){
    		$('[data-toggle*="validation"]').trigger("validation");
    		$('[data-toggle*="fixed"]').trigger("fixed");
    		$('[data-toggle*="tagTree"]').trigger("tagTree");
    		if($.fn.tooltip){
    			$('[data-toggle*="tooltip"]').tooltip({container:'body'});
    		}
    	});

    </script>
    <style type="text/css">
    	.captcha_modal{
    		width: 380px;
    		height: 330px;
    		z-index: 9999;
    		top: 150px;
    		margin: auto;
    		position: absolute;
    		box-sizing: border-box;
    		border-radius: 2px;
    		background-color: #fff;
    		box-shadow: 0 0 10px rgba(0,0,0,.3);
    		left: 40%;
    	}
    </style>
    <!-- 文件操作相关js -->
    <script type="text/javascript" src="/js/globalweb/comp/file/file.js?ver=29002685"></script>
    <!--教务系统通用业务js引用:比如学年，学期等公共的信息会放在这里-->
    <script type="text/javascript" src="/js/globalweb/comp/i18n/jwglxt-common_zh_CN.js?ver=29002685"></script>
    <!--业务模块的properties初始化-->
    <!--国际化js库 -->
    <script type="text/javascript" src="/js\globalweb\comp\i18n\N253512_zh_CN.js?ver=29002685" charset="utf-8"></script>

    <!--移动端审核-->


    	<style type="text/css">
    		.btn-quick{
    			margin-right:30px;
    			height:25px;
    			padding: 0px 10px;
    		}
    		.outer_left .glyphicon:before {
    		    margin: 14px;
    		}
    		.jxb-wyl{
    			background-color:#f400006e !important;
    		}
    	</style>

    </head>
    <body>
    <input type="hidden" id="pkey" name="pkey" value="" />
    <input type="hidden" id="kqhjs" name="kqhjs" value="0" />
    <input type="hidden" id="shyjsfbt" name="shyjsfbt" value="0" />
    <input type="hidden" id="localeKey" name="localeKey" value="zh_CN" />
    <input type="hidden" id="csrftoken" name="csrftoken" value="5352935d-76e5-4873-a829-556c771ad92e,5352935d76e54873a829556c771ad92e"/>
    <input type="hidden" id="cdTsxx" name="cdTsxx" value="-zfsplit-" />
    <input type="hidden" id="wjylSfkf" name="wjylSfkf" value="0" >
    <input type="hidden" id="dingdingbj" name="dingdingbj" value="" />
    <input type="hidden" id="pageNumber" name="pageNumber" value="15" />
    <input type="hidden" id="sfsygdgdt" name="sfsygdgdt" value="0" />
    <div id="mobile-div" style="display:none">
    			<div class="container">
    			<div class="navbar-header">
    				<button class="navbar-toggle" type="button" data-toggle="collapse" data-target=".bs-navbar-collapse">
    					<span class="sr-only"> 自主选课</span> 
    					<span class="icon-bar"></span> 
    					<span class="icon-bar"></span> 
    					<span class="icon-bar"></span>
    				</button>
    				<a href="#" id="topButton" class="navbar-brand" onclick="onClickMenu('/xsxk/zzxkyzb_cxZzxkYzbIndex.html','N253512')">
    					自主选课
    				</a>
    				<script type="text/javascript">
    					document.title="自主选课";
    				</script>
    			</div>
    		</div>
    <!-- navbar-end  -->
    	<!-- 判断是否可切换角色 -->

    </div>

    	<!-- 头部 开始 -->
    	<header class="navbar-inverse top2" id="show-head">
    		<div class="container" id="navbar_container">
    			<!-- 判断是否可切换角色 -->

    					<div class="container">
    			<div class="navbar-header">
    				<button class="navbar-toggle" type="button" data-toggle="collapse" data-target=".bs-navbar-collapse">
    					<span class="sr-only"> 自主选课</span> 
    					<span class="icon-bar"></span> 
    					<span class="icon-bar"></span> 
    					<span class="icon-bar"></span>
    				</button>
    				<a href="#" id="topButton" class="navbar-brand" onclick="onClickMenu('/xsxk/zzxkyzb_cxZzxkYzbIndex.html','N253512')">
    					自主选课
    				</a>
    				<script type="text/javascript">
    					document.title="自主选课";
    				</script>
    			</div>
    		</div>
    <!-- navbar-end  -->
    		</div>
    	</header>
    	<script>
    		if(window.self !== window.top){
    			 $('body').css({
    				"background": "#fff"
    			}) 
    			$('body').find('.navbar-inverse').hide();			
    		}
    	</script>

    	<!--头部 结束 -->
    	<div style="width: 100%; padding: 0px; margin: 0px;" id="bodyContainer">
    		<!-- requestMap中的参数为系统级别控制参数，请勿删除 -->
    		<form id="requestMap">
    			 <input type="hidden" id="sessionUserKey" value="20230307049" /> 

    			 	<input type="hidden" id="gnmkdmKey" value="N253512" />


    		</form>
    		<div class="container container-func sl_all_bg" id="yhgnPage">
    			<div id="innerContainer">
    				<!-- 放置页面显示内容 -->
    				<div class="all-mask" style="position: fixed; top: 0; left: 0; z-index: 99; background: #f7f7f7;"></div>

    	<div class="row sl_add_btn">
    	    <div id="btn-groups" class="col-sm-12">
    	    	<!-- 加载当前菜单栏目下操作   -->
    			<div class="col-sm-12 col-lg-12 col-md-12" style="border-width: 0px"><div class="btn-toolbar" role="toolbar" style="float:right;"><div class="btn-group" id="but_ancd"> </div> </div></div>
    			<!-- 加载当前菜单栏目下操作 -->
    	    </div>
    	</div>
    	<div id="searchBox"></div> 





     		<div class="col-md-12 col-sm-12 border-b"  style="padding:8px 0px;">
    			<div style="float:left;padding:10px 15px;">
    				<h5>
    				<font id="xkxn"></font> 学年 <font id="xkxq"></font> 学期<font id="txt_xklc"></font><span id="sysj"></span>
    				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>本学期选课要求</b>总学分最低&nbsp;<font color="red">0</font>

    					&nbsp;&nbsp;最高&nbsp;<font color="red">99</font>


    				&nbsp;&nbsp;&nbsp;本学期已选学分&nbsp;&nbsp;<font color="red" id="yxxfs">0</font>



    				</h5>
    			</div>
    			<div style="margin-right:20px;float:right;padding:8px 15px;">
    				<!-- <div style="float:left;margin-top:-2px;margin-right:20px;font-size:20px">【<a style="text-decoration:underline;" href="javascript:void(0)" onclick="$.showDialog(_path+'/xjyj/xsxyqk_ckXsXyxxHtmlView.html','我的修业情况',$.extend({},viewConfig,{width: ($('#yhgnPage').innerWidth()-200)+'px'}));">我的修业情况</a>】</div> -->
    				<div id="quickXk" style="float:left;"></div>
    				<div style="float:left;">
    					<p style="margin-top:4px;margin-right:5px;float:left;border:1px solid #BCE8F1;background-color:#D9EDF7;height:15px;width:30px;"></p>未选
    				</div>
    				<div style="float:left;margin-left:20px">
    					<p style="margin-top:4px;margin-right:5px;float:left;border:1px solid #BCE8F1;background-color:#fff7b2;height:15px;width:30px;"></p>重修未选
    				</div>
    				<div style="float:left;margin-left:20px">
    					<p style="margin-top:4px;margin-right:5px;float:left;border:1px solid #BCE8F1;background-color:#C1FFC1;height:15px;width:30px;"></p>已选
    				</div>
    			</div>
    		</div>

    		<input type="hidden" name="iskxk" id="iskxk" value="1"/>
    		<input type="hidden" name="jgh_id" id="jgh_id"/>
    		<input type="hidden" name="to_kch" id="to_kch" value=""/>
    		<input type="hidden" name="jzxkf" id="jzxkf" value="0"/>
    		<input type="hidden" name="xkzgmc" id="xkzgmc" value="99"/>
    		<input type="hidden" name="xkzgxf" id="xkzgxf" value="99"/>
    		<input type="hidden" name="zkcs" id="zkcs" value="14"/>
    		<input type="hidden" name="zxfs" id="zxfs" value="18.5"/>
    		<input type="hidden" name="bdzcbj" id="bdzcbj" value="2"/>
    		<input type="hidden" name="xkxnm" id="xkxnm" value="2024"/>
    		<input type="hidden" name="xkxqm" id="xkxqm" value="12"/>
    		<input type="hidden" name="xkxnmc" id="xkxnmc" value="2024-2025"/>
    		<input type="hidden" name="xkxqmc" id="xkxqmc" value="2"/>
    		<input type="hidden" name="xh_id" id="xh_id" value="20230307049"/>
    		<input type="hidden" name="xqh_id" id="xqh_id" value="2"/>
    		<input type="hidden" name="jg_id_1" id="jg_id_1" value="03"/>
    		<input type="hidden" name="zyh_id" id="zyh_id" value="8A173F62AE3F548BE055000000000001"/>
    		<input type="hidden" name="zymc" id="zymc" value="文化遗产"/>
    		<input type="hidden" name="zyfx_id" id="zyfx_id" value="wfx"/>
    		<input type="hidden" name="njdm_id" id="njdm_id" value="2023"/>
    		<input type="hidden" name="njmc" id="njmc" value="2023"/>
    		<input type="hidden" name="bh_id" id="bh_id" value="03072301"/>
    		<input type="hidden" name="xbm" id="xbm" value="1"/>
    		<input type="hidden" name="zh" id="zh" value=""/>
    		<input type="hidden" name="xslbdm" id="xslbdm" value="wlb"/>
    		<input type="hidden" name="mzm" id="mzm" value="01"/>
    		<input type="hidden" name="xz" id="xz" value="4"/>
    		<input type="hidden" name="ccdm" id="ccdm" value="3"/>
    		<input type="hidden" name="xsbj" id="xsbj" value="4294967296"/>
    		<input type="hidden" name="sjhm" id="sjhm" value="w"/>
    		<input type="hidden" name="xszxzt" id="xszxzt" value="1"/>
    		<input type="hidden" name="njdm_id_1" id="njdm_id_1" value="2023"/>
    		<input type="hidden" name="zyh_id_1" id="zyh_id_1" value="8A173F62AE3F548BE055000000000001"/>
    		<input type="hidden" name="sfxsxkbz" id="sfxsxkbz" value="0"/>
    		<input type="hidden" name="sfxskssj" id="sfxskssj" value="0"/>
    		<input type="hidden" name="wrljxbbhkg" id="wrljxbbhkg" value="0"/>
    		<input type="hidden" name="jxbzbkg" id="jxbzbkg" value="1"/>
    		<input type="hidden" name="tykpzykg" id="tykpzykg" value="0"/>
    		<input type="hidden" name="tkdxyzms" id="tkdxyzms" value="0"/>
    		<input type="hidden" name="jxbzhkg" id="jxbzhkg" value="0"/>
    		<input type="hidden" name="xxdm" id="xxdm" value="10373"/>
    		<input type="hidden" name="xkgwckg" id="xkgwckg" value="0"/>
    		<input type="hidden" name="cxkctskg" id="cxkctskg" value="0"/>
    		<input type="hidden" name="kxqxktskg" id="kxqxktskg" value="0"/>
    		<input type="hidden" name="tbtkxqxktskg" id=tbtkxqxktskg value="0"/>
    		<input type="hidden" name="xkkczdsqkg" id="xkkczdsqkg" value="1"/>
    		<input type="hidden" name="xkmcjzxskcs" id="xkmcjzxskcs" value="10"/>

    		<input type="hidden" name="xkckctkckg" id="xkckctkckg" value=""/>
    		<input type="hidden" name="xkbzsyljkg" id="xkbzsyljkg" value="0"/>
    		<input type="hidden" name="xyjskljdz" id="xyjskljdz" value="http://"/>

    		<input type="hidden" name="zzxkgjcxkg_kcz" id="zzxkgjcxkg_kcz" value="0"/>
    		<input type="hidden" name="zzxkgjcxkg_nj" id="zzxkgjcxkg_nj" value="1"/>
    		<input type="hidden" name="zzxkgjcxkg_xy" id="zzxkgjcxkg_xy" value="1"/>
    		<input type="hidden" name="zzxkgjcxkg_zy" id="zzxkgjcxkg_zy" value="1"/>
    		<input type="hidden" name="zzxkgjcxkg_kkxy" id="zzxkgjcxkg_kkxy" value="1"/>
    		<input type="hidden" name="zzxkgjcxkg_xqu" id="zzxkgjcxkg_xqu" value="0"/>
    		<input type="hidden" name="zzxkgjcxkg_yqu" id="zzxkgjcxkg_yqu" value="0"/>
    		<input type="hidden" name="zzxkgjcxkg_tjbj" id="zzxkgjcxkg_tjbj" value="0"/>
    		<input type="hidden" name="zzxkgjcxkg_kclb" id="zzxkgjcxkg_kclb" value="1"/>
    		<input type="hidden" name="zzxkgjcxkg_kcxz" id="zzxkgjcxkg_kcxz" value="1"/>
    		<input type="hidden" name="zzxkgjcxkg_jxms" id="zzxkgjcxkg_jxms" value="1"/>
    		<input type="hidden" name="zzxkgjcxkg_kcgs" id="zzxkgjcxkg_kcgs" value="1"/>
    		<input type="hidden" name="zzxkgjcxkg_skxq" id="zzxkgjcxkg_skxq" value="1"/>
    		<input type="hidden" name="zzxkgjcxkg_skjc" id="zzxkgjcxkg_skjc" value="1"/>
    		<input type="hidden" name="zzxkgjcxkg_jxb" id="zzxkgjcxkg_jxb" value="1"/>
    		<input type="hidden" name="zzxkgjcxkg_sfcx" id="zzxkgjcxkg_sfcx" value="1"/>
    		<input type="hidden" name="zzxkgjcxkg_ywyl" id="zzxkgjcxkg_ywyl" value="1"/>
    		<input type="hidden" name="zzxkgjcxkg_sksjct" id="zzxkgjcxkg_sksjct" value="0"/>
            <input type="hidden" name="xksdxjckg" id="xksdxjckg" value="0"/>
    		<input type="hidden" name="xkxskclxkg" id="xkxskclxkg" value="0"/>
    		<input type="hidden" name="mycos_sjtb_xkkg" id="mycos_sjtb_xkkg" value="0"/>

    		<input type="hidden" name="xkczbj" id="xkczbj" value="1"/>
    		<input type="hidden" name="isSlct" id="isSlct" value="0"/>
    		<input type="hidden" name="kklxdm" id="kklxdm" value=""/>
    		<input type="hidden" name="kklxmc" id="kklxmc" value=""/>
    		<input type="hidden" name="xkkz_id" id="xkkz_id" value=""/>
    		<input type="hidden" name="jxbzb" id="jxbzb" value=""/>


    			<div class="panel panel-info">
    			<!-- 开始 -->
    			<ul class="nav nav-tabs sl_nav_tabs" role="tablist" id="nav_tab">



    						<li class="active"><a id="tab_kklx_01" href="javascript:void(0)" onclick="queryCourse(this,'01','2E51BF193229509AE065000000000001','2023','8A173F62AE3F548BE055000000000001')" role="tab" data-toggle="tab">主修课程</a></li>
    						<input type="hidden" name="firstKklxdm" id="firstKklxdm" value="01"/>
    						<input type="hidden" name="firstKklxmc" id="firstKklxmc" value="主修课程"/>
    						<input type="hidden" name="firstXkkzId" id="firstXkkzId" value="2E51BF193229509AE065000000000001"/>
    						<input type="hidden" name="firstNjdmId" id="firstNjdmId" value="2023"/>
    						<input type="hidden" name="firstZyhId" id="firstZyhId" value="8A173F62AE3F548BE055000000000001"/>






    			 			<li><a id="tab_kklx_06" href="javascript:void(0)" onclick="queryCourse(this,'06','2E529F9BCF441BDFE065000000000001','2023','8A173F62AE3F548BE055000000000001')" role="tab" data-toggle="tab">板块课(大学英语4)</a></li>





    			 			<li><a id="tab_kklx_06" href="javascript:void(0)" onclick="queryCourse(this,'06','2E52CF9BD3D8235DE065000000000001','2023','8A173F62AE3F548BE055000000000001')" role="tab" data-toggle="tab">板块课(体育4)</a></li>





    			 			<li><a id="tab_kklx_09" href="javascript:void(0)" onclick="queryCourse(this,'09','2E529244AE741BD0E065000000000001','2023','8A173F62AE3F548BE055000000000001')" role="tab" data-toggle="tab">特殊课程</a></li>


    		 		<div class="pull-right" style="margin-top:4px;margin-right:30px">

    		 		</div>
    			</ul>
    			</div>



    	<div id="displayBox"></div>
    	<div id="choosedBox"></div>
    	<div id="endsign" style="display:none; text-align:center; height: 50px"><i class="red">......已到最后......</i></div><!-- （共 <font id="searchCount"></font> 条记录） -->
    	<!-- <div id="waitsign" style="display:none; text-align:center; height: 50px"><i class="red bigger-300 icon-spinner icon-spin"></i></div> -->
    	<div id="more" style="text-align:center; display:none"><font color="#2a6496" size="5">[<a href="javascript:void(0)" onclick="loadCoursesByPaged();">点此查看更多</a>]</font></div>
    	<!--jQuery.jqGrid -->
    <link rel="stylesheet" type="text/css" href="/zftal-ui-v5-1.0.2/assets/plugins/jqGrid/css/jquery.jqgrid.css?ver=29002685" />
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/plugins/jqGrid/jquery.jqgrid.src-min.js?ver=29002685" charset="utf-8"></script>
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/plugins/jqGrid/jquery.jqgrid.contact-min.js?ver=29002685" charset="utf-8"></script>
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/plugins/jqGrid/lang/zh_CN.js?ver=29002685" charset="utf-8"></script>
    <script type="text/javascript" src="/js/plugins/jqGrid4.6/jquery.jqgrid.settings.js?ver=29002685" charset="utf-8"></script>
    <script type="text/javascript" src="/js/plugins/jqGrid4.6/jquery.jqGrid-min.js?ver=29002685" charset="utf-8"></script>
    	<!--jQuery.validation -->
    <link rel="stylesheet" type="text/css" href="/zftal-ui-v5-1.0.2/assets/plugins/validation/css/jquery.validate-min.css?ver=29002685" />
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/plugins/validation/js/jquery.validate-min.js?ver=29002685" charset="utf-8"></script>
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/plugins/validation/js/jquery.validate.contact-min.js?ver=29002685" charset="utf-8"></script>
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/plugins/validation/js/jquery.validate.methods.contact-min.js?ver=29002685" charset="utf-8"></script>
    <script type="text/javascript" src="/zftal-ui-v5-1.0.2/assets/plugins/validation/lang/zh_CN-min.js?ver=29002685" charset="utf-8"></script>
    <script type="text/javascript">
    	jQuery(function($){
    		$('[data-toggle*="validation"]').trigger("validation");
    	});
    </script>

    	<link rel="stylesheet" type="text/css" href="/js/plugins/searchbox/css/jquery.searchbox-min.css?ver=29002685" />
    <script type="text/javascript" src="/js/plugins/searchbox/jquery.searchbox.contact-min.js?ver=29002685" charset="utf-8"></script>
    <script type="text/javascript" src="/js/plugins/searchbox/jquery.searchbox.contact-zh_CN.js?ver=29002685" charset="utf-8"></script>
    	<script type="text/javascript" src="/js/comp/jwglxt/xkgl/xsxk/zzxkYzb.js?ver=29002685"></script>








    			</div>
    		</div>
    	</div>
    	<!-- footer -->








    <!-- footer --> 

    <div id="footerID" class="footer"  style="background-color: " >

    	<p>版权所有&#169; Copyright 1999-2023 正方软件股份有限公司　　中国·杭州西湖区紫霞街176号 互联网创新创业园2号301&nbsp;&nbsp;&nbsp;版本V-9.0</p>
    </div>




    <script  type="text/javascript">
    	//系统中页面底部的时间随系统时间来定
    	/* var date=new Date;
    	var year=date.getFullYear();
    	var s = $("#footerID").text().indexOf('-');
    	var textNr =$("#footerID").text().substr(0,s+1)+year+$("#footerID").text().substr(s+5);
    	$("#footerID").text("");
    	$("#footerID").text(textNr); */

    </script>
    <!-- footer-end -->
    	<!-- footer-end -->
    </body>
    <script type="text/javascript">
    	jQuery(function($) {	
    		if ($("#navbar-tabs").length > 0) {
    			$("#navbar-tabs li:eq(0) a").tab('show');
    		}
    		setMinheight();
    		setCdtsxx();

    		$('#yhgnPage').resize(function(){
    			var minHeight  = $(this).data('min-height');
    			var innerHeight =  $('#innerContainer').outerHeight(true);
    			if(self != top){
    				$(this).css('min-height', "380");
    			}else{
    				$(this).css('min-height', Math.max(minHeight,innerHeight));
    			}

    		});

    		function setMinheight(){
    			//计算grid页面高度
    			var docuemntHeight = $(document).height();
    			var topHeight = $('header').height();
    			var footerHeight = $('.footer').height();
    			var containerHeight = docuemntHeight-topHeight-footerHeight-60;
    			if(self != top){
    				containerHeight = 380;
    			}
    			$('#yhgnPage').css('min-height',containerHeight).data('min-height',containerHeight);
    		}

    		//加载title名称，根据系统内置表设置，取菜单名称或者系统名称
    		$(document).attr("title",'自主选课');

    		//设置菜单提示信息
    		function setCdtsxx(){
    			if($("#cdTsxx").val()!=null&&$("#cdTsxx").val()!="-zfsplit-"){
    				var tsxx = $("#cdTsxx").val().split("-zfsplit-")[0];
    				var tsxxljdz = $("#cdTsxx").val().split("-zfsplit-")[1];
    				var tsxxHtml = "<a class='navbar-brand' "+(tsxxljdz!=""?"href='"+tsxxljdz+"' target='_blank'":"")+">"+tsxx+"</a>";
    				$(".navbar-header").prepend(tsxxHtml);
    			}
    		}

    		//绑定角色切换功能
    		$(document).off('change', '#changeRole').on('change', '#changeRole', function(e,param) {
    			var key = param?param:$(this).val();
    			$.post(_path + "/xtgl/index_changeRole.html",{jsdm:key},function(data){
    				window.location.href = window.location.href;//刷新页面
    			 });
    		});

    		//进行相应判断是否可切换角色及是否移动端的判断
    		if($("#kqhjs").val()=="1"&&device.mobile()){
    			$("#navbar_container").empty();
    			$("#navbar_container").append($("#mobile-div").html());
    			$("#mobile-div").empty();
    		}else{
    			$("#mobile-div").empty();
    		}
    	});
    </script>
    <!-- 设置元素固定位置显示插件  scrolltofixed 相应ini文件引用-->
    <!-- è®¾ç½®åç´ åºå®ä½ç½®æ¾ç¤ºæä»¶  scrolltofixed -->
    <script type="text/javascript" src="/js/plugins/scrolltofixed/jquery-scrolltofixed-min.js?ver=29002685"></script>
    <script>
    	$(document).ready(function() {
    		$("div.sl_add_btn .btn-toolbar").scrollToFixed({
    			marginTop:35,
    			zIndex:1060,
    			fixed:function(){
    				//$(this).css({"width":"auto"});
    			},
    		});
    		$("#gbox_tabGrid div.ui-jqgrid-hdiv").scrollToFixed({
    			//marginTop:3,
    			spacerClass:'hide-div'
    		});
    	});
    </script>
    <style>
    	.hide-div{
    		display:none; 
    	}
    </style>
    <!-- 软件评价 相应ini文件引用-->


    <link rel="stylesheet"  type="text/css" href="/js/plugins/tagtree/tagTree.css?ver=29002685"/>
    <script type='text/javascript' src="/js/plugins/tagtree/tagtree.js?ver=29002685"></script>
    <script type='text/javascript' src="/js/plugins/tagtree/tagtreeBusiness.js?ver=29002685"></script>

    </html>'''

    # 解析HTML
    tree = html.fromstring(html_content)

    # 假设 obj_need 支持 [] 操作符访问其属性

    # 使用 [] 操作符替代 . 操作符来访问属性
    obj_need['xkkz_id'] = tree.xpath('//input[@id="xkkz_id"]/@value')[0] if tree.xpath(
        '//input[@id="xkkz_id"]/@value') else None
    obj_need['njdm_id'] = tree.xpath('//input[@id="njdm_id"]/@value')[0] if tree.xpath(
        '//input[@id="njdm_id"]/@value') else None
    obj_need['zyh_id'] = tree.xpath('//input[@id="zyh_id"]/@value')[0] if tree.xpath(
        '//input[@id="zyh_id"]/@value') else None
    obj_need['kklxdm'] = tree.xpath('//input[@id="kklxdm"]/@value')[0] if tree.xpath(
        '//input[@id="kklxdm"]/@value') else None
    obj_need['xklc'] = 1  # 这个直接赋值保持不变
    obj_need['xkxnm'] = tree.xpath('//input[@id="xkxnm"]/@value')[0] if tree.xpath(
        '//input[@id="xkxnm"]/@value') else None
    obj_need['xkxqm'] = tree.xpath('//input[@id="xkxqm"]/@value')[0] if tree.xpath(
        '//input[@id="xkxqm"]/@value') else None

    obj_need['jg_id'] = tree.xpath('//input[@id="jg_id"]/@value')[0] if tree.xpath(
        '//input[@id="jg_id"]/@value') else None
    obj_need['zyfx_id'] = tree.xpath('//input[@id="zyfx_id"]/@value')[0] if tree.xpath(
        '//input[@id="zyfx_id"]/@value') else None
    obj_need['bh_id'] = tree.xpath('//input[@id="bh_id"]/@value')[0] if tree.xpath(
        '//input[@id="bh_id"]/@value') else None
    obj_need['xz'] = tree.xpath('//input[@id="xz"]/@value')[0] if tree.xpath('//input[@id="xz"]/@value') else None
    obj_need['ccdm'] = tree.xpath('//input[@id="ccdm"]/@value')[0] if tree.xpath('//input[@id="ccdm"]/@value') else None
    obj_need['xkly'] = tree.xpath('//input[@id="xkly"]/@value')[0] if tree.xpath('//input[@id="xkly"]/@value') else None
    obj_need['jcxx_id'] = ''  # 明确设置为空字符串
    obj_need['sxbj'] = int(tree.xpath('//input[@id="sxbj"]/@value')[0]) if tree.xpath(
        '//input[@id="sxbj"]/@value') else 0  # 确保转换为整数类型，如果没有该值则默认为0
    return ''
aa()
print(obj_need)

def get_xkkz_id():
    import requests

    cookies = {
        'route': 'b2d11ce13d45c150aa5f01e2aa730818',
        'JSESSIONID': '9D083F827DBA470863FEE91EEAE78825',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'http://210.45.128.80',
        'Pragma': 'no-cache',
        'Referer': 'http://210.45.128.80/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'route=b2d11ce13d45c150aa5f01e2aa730818; JSESSIONID=9D083F827DBA470863FEE91EEAE78825',
    }

    params = {
        'gnmkdm': 'N253512',
    }

    data = {
        'jg_id': obj_need['jg_id'],
        'zyh_id': obj_need['zyh_id'],
        'njdm_id': obj_need['njdm_id'],
        'zyfx_id': obj_need['zyfx_id'],
        'bh_id': obj_need['bh_id'],
        'xz': obj_need['xz'],
        'ccdm': obj_need['ccdm'],
        'xkxnm': obj_need['xkxnm'],
        'xkxqm': obj_need['xkxqm'],
        'xkly': obj_need['xkly'],
    }

    response = requests.post('http://210.45.128.80/xsxk/zzxkyzb_cxZzxkYzbChoosedDisplay.html', params=params,
                             cookies=cookies, headers=headers, data=data, verify=False)
    return response.text

def ab():
    import requests

    cookies = {
        'route': 'b2d11ce13d45c150aa5f01e2aa730818',
        'JSESSIONID': '9D083F827DBA470863FEE91EEAE78825',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'http://210.45.128.80',
        'Pragma': 'no-cache',
        'Referer': 'http://210.45.128.80/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'route=b2d11ce13d45c150aa5f01e2aa730818; JSESSIONID=9D083F827DBA470863FEE91EEAE78825',
    }

    params = {
        'gnmkdm': 'N253512',
    }

    data = {
        'jg_id': '03',
        'zyh_id': '8A173F62AE3F548BE055000000000001',
        'njdm_id': '2023',
        'zyfx_id': 'wfx',
        'bh_id': '03072301',
        'xz': '4',
        'ccdm': '3',
        'xkxnm': '2024',
        'xkxqm': '12',
        'xkly': '1',
    }
    response = requests.post('http://210.45.128.80/xsxk/zzxkyzb_cxZzxkYzbChoosedDisplay.html', params=params,
                             cookies=cookies, headers=headers, data=data, verify=False)
    print(response.text)


#获取课程标识来区别课程
#do_jxb_ids
def get__do_jxb_id():
    import requests
    cookies = {
        'route': 'b2d11ce13d45c150aa5f01e2aa730818',
        'JSESSIONID': '9D083F827DBA470863FEE91EEAE78825',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'http://210.45.128.80',
        'Pragma': 'no-cache',
        'Referer': 'http://210.45.128.80/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'route=b2d11ce13d45c150aa5f01e2aa730818; JSESSIONID=9D083F827DBA470863FEE91EEAE78825',
    }
    params = {
        'gnmkdm': 'N253512',
    }
    data = {
        'bklx_id': '7BB352435FD8291AE055000000000001',  #
        'zyh_id': '8A173F62AE3F548BE055000000000001',
        'zyfx_id': 'wfx',
        'njdm_id': '2023',
        'bh_id': '03072301',
        'xz': '4',
        'xkxnm': '2024',
        'xkxqm': '12',
        'kklxdm': '06',  #可能是固定的
        'kch_id': 'FEFE498C14E41985E055000000000001',  #
        'xkkz_id': '2E52CF9BD3D8235DE065000000000001',       #
    }

    response = requests.post('http://210.45.128.80/xsxk/zzxkyzbjk_cxJxbWithKchZzxkYzb.html', params=params,
                             cookies=cookies, headers=headers, data=data, verify=False)


    import ast

    actual_list = ast.literal_eval(response.text)
    for i in actual_list:
        teacher_name = i['jsxx']
        if '王玉' in teacher_name:
            pass
        print(i['do_jxb_id'])
        print()

#所有获取课程号的id标识符
#kch_id
def get__kch_id():
    import requests

    cookies = {
        'route': '27b76eab7509c64adb2489b5f9149598',
        'JSESSIONID': '1EA71FE6E6AA9E889443853B1D98F0AD',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'route=27b76eab7509c64adb2489b5f9149598; JSESSIONID=1EA71FE6E6AA9E889443853B1D98F0AD',
        'Origin': 'http://210.45.128.80',
        'Referer': 'http://210.45.128.80/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/11 SLBVPV/64-bit',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'gnmkdm': 'N253512',
    }

    data = {
        'jg_id': '03',
        'zyh_id': '8A173F62AE3F548BE055000000000001',
        'njdm_id': '2023',
        'zyfx_id': 'wfx',
        'bh_id': '03072301',
        'xz': '4',
        'ccdm': '3',
        'xkxnm': '2024',
        'xkxqm': '12',
        'xkly': '1',
    }

    response = requests.post('http://210.45.128.80/xsxk/zzxkyzb_cxZzxkYzbChoosedDisplay.html', params=params,
                             cookies=cookies, headers=headers, data=data, verify=False)


def post_req(do_jxb_ids,kch_id,xkkz_id,zyh_id):
    import requests
    cookies = {
        'route': 'b2d11ce13d45c150aa5f01e2aa730818',
        'JSESSIONID': '9D083F827DBA470863FEE91EEAE78825',
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'http://210.45.128.80',
        'Pragma': 'no-cache',
        'Referer': 'http://210.45.128.80/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'gnmkdm': 'N253512',
    }
    data = f'jxb_ids={do_jxb_ids}&kch_id={kch_id}&kcmc=(20230036)%E4%BD%93%E8%82%B24+-+1.0+%E5%AD%A6%E5%88%86&rwlx=3&rlkz=0&rlzlkz=1&sxbj=1&xxkbj=0&qz=0&cxbj=0&xkkz_id={xkkz_id}&njdm_id=2023&zyh_id={zyh_id}&kklxdm=06&xklc=1&xkxnm=2024&xkxqm=12&jcxx_id='

    response = requests.post('http://210.45.128.80/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html', params=params, cookies=cookies,headers=headers, data=data, verify=False)
    print(response.text)

if __name__ == '__main__':
    pass
