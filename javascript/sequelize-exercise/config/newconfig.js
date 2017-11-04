const Sequelize = require('sequelize');
const sequelize = new Sequelize('tasks', 'postgres', 'password', {
  host: 'localhost',
  dialect: 'postgres',

  pool: {
    max: 5,
    min: 0,
    idle: 10000
  }
});
