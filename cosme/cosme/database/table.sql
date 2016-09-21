CREATE TABLE `product_detail` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `prc_id` int(11) NOT NULL,
      `prc_publish_date` date NOT NULL,
      `prc_child_cat_id` int(11) NOT NULL,
      `prc_price_jpy` int(11) NOT NULL,
      `prc_price_rmb` int(11) NOT NULL,
      `prc_info` varchar(1024) NOT NULL,
      `large_pic_url` varchar(128) NOT NULL,
      PRIMARY KEY (`id`),
      KEY `idx_prc_price_rmb` (`prc_price_rmb`),
      KEY `idx_prc_publish_date` (`prc_publish_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `product` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `prc_id` int(11) NOT NULL,
      `prc_bid_name` varchar(128) NOT NULL,
      `prc_name` varchar(128) NOT NULL,
      `prc_url` varchar(256) DEFAULT '',
      `prc_rank` int(11) NOT NULL,
      `prc_child_cat_id` int(11) NOT NULL,
      `pc_child_cat_name` varchar(128) DEFAULT '',
      `small_pic_url` varchar(256) DEFAULT '',

      PRIMARY KEY (`id`),
      KEY `idx_prc_rank` (`prc_rank`),
      KEY `idx_pc_child_cat_name` (`pc_child_cat_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
