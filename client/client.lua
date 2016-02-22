-- Author:         wanghe
-- Email:          wangh@loginsight.cn
-- Author website:
--
-- File: client.lua
 -- Create Date: 2016-02-22 18:50:10
 --

local http=require("socket.http");
local base64 = require('base64')
local CLIENT_ID="QIC2k0tpZB_.yjgfC9-ks0WGDauRnmaM7F.gbzK9"
local CLIENT_SECRET="ZnFc8jL?uqnUxI6!;ZjCfhwKS@H0RtZV2=Iu;iHbMqtK5a@XcfQ3@3oD2FZh?tvahz?Qohz-Vnb2ECaNlJ4r_vwb@hXig;QNjydwAE4f5qx7L2D7BbXhZMVsdT?sNJQM"
local head_data = base64.encode(CLIENT_ID..":"..CLIENT_SECRET)
username = "wanghe"
password = "123"

local request_body = [[grant_type=password&username=wanghe&password=123]]
local response_body = {}

local res, code, response_headers = http.request{
      url = "http://192.168.200.218:8000/o/token/",
      method = "POST",
      headers =
        {
            ["Content-Type"] = "application/x-www-form-urlencoded";
            ["Content-Length"] = #request_body;
            ["Authorization"] = "Basic "..head_data;
        },
        source = ltn12.source.string(request_body),
        sink = ltn12.sink.table(response_body),
  }

  print(res)
  print(code)

  if type(response_headers) == "table" then
    for k, v in pairs(response_headers) do
      print(k, v)
    end
  end

  print("Response body:")
  if type(response_body) == "table" then
    print(table.concat(response_body))
  else
    print("Not a table:", type(response_body))
  end
