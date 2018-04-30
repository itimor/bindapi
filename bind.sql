# 插入SOA数据
INSERT INTO bind_record (`zone`, `host`, `type`, `data`, `ttl`,`mx_priority`,
`refresh`, `retry`, `expire`, `minimum`, `serial`, `resp_person`, `primary_ns`,
`data_count`) VALUES
('51niux.in', '@', 'SOA', 'ns1.51niux.in.', 10, NULL, 600, 3600, 86400,
10, 2017060801, 'root.51niux.in.', 'ns1.51niux.in.', 0);

# 插入@ NS数据
INSERT INTO bind_record (`zone`, `host`, `type`, `data`) VALUES
('51niux.in', '@', 'NS', 'ns1.51niux.in.'),
('51niux.in', '@', 'NS', 'ns2.51niux.in.');

# 插入NS A数据
INSERT INTO bind_record (`zone`, `host`, `type`, `data`) VALUES
('51niux.in', 'ns1', 'A', '192.168.1.108'),
('51niux.in', 'ns2', 'A', '192.168.1.111');

# 插入www A记录
INSERT INTO bind_record (`zone`, `host`, `type`, `data`, `ttl`, `view`) VALUES
('51niux.in', 'www', 'A', '192.168.1.111', 360, 'CNC'),
('51niux.in', 'www', 'A', '192.168.1.112', 360, 'CT'),
('51niux.in', 'www', 'A', '192.168.1.113', 360, 'TIETONG'),
('51niux.in', 'www', 'A', '192.168.1.114', 360, 'OTHERANY');

# 插入CNAME 记录
INSERT INTO bind_record (zone,host,type,DATA,view) VALUES
('51niux.in', 'blog', 'CNAME', 'www','DEFAULT');