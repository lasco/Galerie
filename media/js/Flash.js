var parameters = window.location.search.substr(1);
var objectEmbed = '<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" id="index" width="100%" height="100%" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab">';
	objectEmbed += '<param name="movie" value="emageview.swf" />';
	objectEmbed += '<param name="quality" value="high" />';
	objectEmbed += '<param name="bgcolor" value="#11212B" />';
	objectEmbed += '<param name="allowScriptAccess" value="sameDomain" />';
	objectEmbed += '<param name="allowFullScreen" value="true" />';
	objectEmbed += '<param name="FlashVars" value="' + parameters + '" />';
	objectEmbed += '<embed src="emageview.swf" allowFullScreen="true" quality="high" bgcolor="#11212B" width="100%" height="100%" name="index" align="middle" play="true" loop="false" quality="high" allowScriptAccess="sameDomain" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" FlashVars="' + parameters + '"></embed>';
	objectEmbed += '</object>';
document.write(objectEmbed);