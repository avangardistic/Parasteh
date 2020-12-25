const webpack = require("webpack");
const path = require("path");

module.exports = {
    mode: 'development',
    entry: [
        './static/js/app.js'
    ],
    output: {
        path: path.resolve(__dirname, "build"),
        filename: "bundle.js",
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery",
            "window.jQuery": "jquery",
        }),
    ],
    module: {
        rules: [{
            test: /bootstrap\/dist\/js\/umd\//,
            use: "imports-loader?jQuery=jquery",
        }, ],
    },
};
