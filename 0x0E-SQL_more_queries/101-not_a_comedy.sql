-- The script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT `tv_shows`.`title`, SUM(`rating`) AS `rating_sum`
FROM `tv_shows`
JOIN `hbtn_0d_tvshows_rate` ON `tv_shows`.`id` = `hbtn_0d_tvshows_rate`.`tv_show_id`
GROUP BY `tv_shows`.`title`
ORDER BY `rating_sum` DESC;
