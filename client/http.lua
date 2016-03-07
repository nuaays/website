--
-- Created by IntelliJ IDEA.
-- User: ma
-- Date: 16/1/19
-- Time: 下午4:48
-- To change this template use File | Settings | File Templates.
--
-- please install luasocket and json
-- apt-get install lua-socket-dev -y
-- apt-get install lua-json -y
local http = require('socket.http')
--local json = require('cjson')
local base64 = require('base64')
local exports = {}
local CLIENT_ID="QIC2k0tpZB_.yjgfC9-ks0WGDauRnmaM7F.gbzK9"
local CLIENT_SECRET="ZnFc8jL?uqnUxI6!;ZjCfhwKS@H0RtZV2=Iu;iHbMqtK5a@XcfQ3@3oD2FZh?tvahz?Qohz-Vnb2ECaNlJ4r_vwb@hXig;QNjydwAE4f5qx7L2D7BbXhZMVsdT?sNJQM"
local head_data = base64.encode(CLIENT_ID..":"..CLIENT_SECRET)
print(head_data)
exports.auth = function(user_name, passwd)
    local request_body = {}
    local response_body = {}
    request_body.grant_type = "password"
    request_body.scope = "read"
    request_body.username = user_name
    request_body.password = passwd
    --request_body = json.encode(request_body)
    --print(request_body)
    local send_data = "grant_type='password'&username="..user_name.."&password="..passwd

    local _, code = http.request({
        --url = "http://192.168.200.218:9000/api/0/user_key",
        --url = "http://192.168.200.218:9000/api/0/user_key?username=admin@loginsight.cn&password=123",
        url = "http://192.168.200.218:8000/o/token/",
        method = "POST",
        headers = {
            --["Content-Type"] = "application/x-www-form-urlencoded";
						--["Content-Length"] = #send_data;
            ["Authorization"] = "Basic "..head_data;
        },
        source = ltn12.source.string(send_data),
        sink = ltn12.sink.table(response_body),
    })
    if code >= 200 and code < 300 then
        local response = table.concat(response_body)
        local result = json.decode(response)
        return result.access_token
    else
        print("error code = "..code)
    end
end
exports.host = function(user_key, host_name, host_type, system, distver)
    local request_body = {}
    local response_body = {}
    request_body.user_key = user_key
    request_body.host_name = host_name
    request_body.host_type = host_type
    request_body.system = system
    request_body.distver = distver
    request_body = json.encode(request_body)
    local _, code = http.request{
        --url = "/API/v1/Storage/host",
        url = "http://192.168.200.218:9000/api/0/agent/hosts",
        method = "POST",
        headers = {
            ["Content-Type"] = "application/json";
            ["Content-Length"] = #request_body;
        },
        source = ltn12.source.string(request_body);
        sink = ltn12.sink.table(response_body);
    }
    if code >= 200 and code < 300 then
        local response = table.concat(response_body)
        local resualt = json.decode(response)
        return resualt.host_key
    else
        print("error code = "..code)
    end
end
print(exports.auth("wanghe", "123"))
--print(exports.host("123", "ma", "test", "ubuntu", "V2.6.3"))
return exports
