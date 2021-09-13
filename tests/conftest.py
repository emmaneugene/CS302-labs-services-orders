import pytest

# Decorator that specifies code that should be run at the beginning of every
# test
@pytest.fixture
def client():
    from src import app

    app.app.config['TESTING'] = True

    app.db.engine.execute('DROP TABLE IF EXISTS `order`;')
    
    app.db.engine.execute('''CREATE TABLE `order` (
    `order_id` int(11) NOT NULL,
    `customer_email` varchar(64) NOT NULL,
    `status` varchar(10) NOT NULL,
    `created` datetime NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;''')

    app.db.engine.execute('''INSERT INTO `order` (`order_id`, `customer_email`, `status`, `created`) VALUES
    (5, 'cposkitt@smu.edu.sg', 'NEW', '2021-08-10 00:00:00'),
    (6, 'phris@coskitt.com', 'NEW', '2021-08-10 00:00:00');''')

    app.db.engine.execute('DROP TABLE IF EXISTS `order_item`;')

    app.db.engine.execute('''CREATE TABLE `order_item` (
    `item_id` int(11) NOT NULL,
    `order_id` int(11) NOT NULL,
    `game_id` int(11) NOT NULL,
    `quantity` int(11) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;''')

    app.db.engine.execute('''INSERT INTO `order_item` (`item_id`, `order_id`, `game_id`, `quantity`) VALUES
    (9, 5, 1, 2),
    (10, 5, 2, 1),
    (11, 6, 9, 1);''')

    return app.app.test_client()