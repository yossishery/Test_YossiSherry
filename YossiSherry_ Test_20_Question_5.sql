
INSERT INTO `interview`.`YossiSherry_Test_20`
(
`gender`,
`email`,
`phone`,
`cell`,
`nat`,
`name_title`,
`name_first`,
`name_last`,
`location_street_number`,
`location_street_name`,
`location_city`,
`location_state`,
`location_country`,
`location_postcode`,
`location_coordinates_latitude`,
`location_coordinates_longitude`,
`location_timezone_offset`,
`location_timezone_description`,
`login_uuid`,
`login_username`,
`login_password`,
`login_salt`,
`login_md5`,
`login_sha1`,
`login_sha256`,
`dob_date`,
`dob_age`,
`registered_date`,
`registered_age`,
`id_name`,
`id_value`,
`picture_large`,
`picture_medium`,
`picture_thumbnail`
)

select *
from
(
select * 
from YossiSherry_test_male as m
order by  m.registered_date desc 
limit 20
 ) as TOP20_Male
 
 union all
 
select * 
from
(
select * 
from  YossiSherry_test_female as f
order by  f.registered_date desc 
limit 20
) as TOP20_Female;



select * from YossiSherry_Test_20



