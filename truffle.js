module.exports = {
  networks: {
    development: {
      host: "localhost",
      port: 8545,
      network_id: "*" // Match any network id
    }
  },
  build: function(options, callback) {
    console.log(options['contracts_directory'])
    console.log(options)
    console.log('cool guys dont look at explosions')
    json_test = JSON.parse(options['_'][0])
    console.log(json_test.test)
    // Do something when a build is required. `options` contains these values:
    //
    // working_directory: root location of the project
    // contracts_directory: root directory of .sol files
    // destination_directory: directory where truffle expects the built assets (important for `truffle serve`)
 }
};
