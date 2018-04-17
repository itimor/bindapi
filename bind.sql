INSERT INTO bind_record ( domain_id, name, type, value, ttl ) VALUES ( 1, 'www', 'A', '1.1.1.22', '600' );
INSERT INTO bind_record ( domain_id, name, type, value, ttl ) VALUES ( 1, 'bbs', 'CNAME', 'www', '600' );
INSERT INTO bind_record ( domain_id, name, type, value, ttl ) VALUES ( 1, '@', 'NS', 'ns', '60' );
INSERT INTO bind_record ( domain_id, name, type, value, ttl ) VALUES ( 1, 'ns', 'A', '1.1.1.11', '600' );