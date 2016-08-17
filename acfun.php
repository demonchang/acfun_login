<?php 
$user = 'YOURACCOUNT';
$pwd = 'PASSWORD';
$url = 'http://passport.acfun.tv/login.aspx';
$path = 'cookie.log';
$postFields = 'username='.$user.'&password='.$pwd;
if(!is_file($path)){
    file_put_contents($path,'');
    $login = curl_init($url);
    curl_setopt($login,CURLOPT_HEADER,0);
    curl_setopt($login,CURLOPT_RETURNTRANSFER,1);
    curl_setopt($login,CURLOPT_POST,1);
    curl_setopt($login,CURLOPT_POSTFIELDS,$postFields);
    curl_setopt($login,CURLOPT_COOKIEJAR,$path);
    $res = curl_exec($login);
    //var_dump($res.PHP_EOL);
    curl_close($login);
}
$header = array(
            "Host" => "www.acfun.tv",
            "User-Agent" => "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0",
            "Accept" => "*/*",
            "Accept-Language" => "en-US,en;q=0.5",
            "Referer" => "http://www.acfun.tv/member/"
        );
if (is_file($path)) {
    $signin = 'http://www.acfun.tv/webapi/record/actions/signin?channel=0&date='.time()*1000;
    $sign = curl_init($signin);
    curl_setopt($sign,CURLOPT_HTTPHEADER, $header);
    curl_setopt($sign,CURLOPT_HEADER,0);
    curl_setopt($sign,CURLOPT_POST,1);
    //curl_setopt($sign,CURLOPT_POSTFIELDS,'');
    curl_setopt($sign,CURLOPT_RETURNTRANSFER,0);
    curl_setopt($sign,CURLOPT_COOKIEFILE,$path);
    $result = curl_exec($sign);
    var_dump($result);
}



 ?>