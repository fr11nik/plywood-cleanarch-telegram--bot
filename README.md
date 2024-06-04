app -- internal logic around app 
use_case -- buisness logic  
migrations -- migration for database TODO:
domain -- whole objects that used between use_case <-> adapters <-> handler
handler -- обработчики для доступа к бизнес логики ака http-grpc-mqqt-websocket-tgbot
adapter -- внешняя среда которая не связана с программой grpc-routes_http-repos_database 
