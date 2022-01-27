import unittest
import pupdater


app_dir = '.'
api_url = 'https://raw.githubusercontent.com/Payroma/metadata/main/payroma-wallet-updater.json'
api_data = {
    "info": {
        "latestVersion": "2.2022-02",
        "title": "Payroma Wallet v2 released",
        "description": "The powerful version of payroma wallet is now available for you."
    },
    "accessToken": "96x8ly-jX2gAAAAAAAAAAUN49xtiieMtsPTgz1YyS9hfJ1c6v7Bn9CQVSUBe6pGq"
}


def function_name(text: str):
    print(f"[ + ] Start for: {text}")


class MyTestCase(unittest.TestCase):
    def _test_set_app_dir(self):
        function_name('set_app_dir')

        pupdater.set_app_dir(path=app_dir)

        self.assertEqual(pupdater.header.APP_DIR, app_dir)

    def _test_set_api_client(self):
        function_name('set_api_client')

        pupdater.set_api_client(api_url=api_url)

        self.assertEqual(pupdater.header.API_URL, api_url)
        self.assertEqual(pupdater.header.ACCESS_TOKEN, api_data[pupdater.Metadata.accessToken])

    def _test_latest_version(self):
        function_name('latest_version')

        pupdater.set_api_client(api_url=api_url)
        result: dict = pupdater.latest_version()

        self.assertEqual(result, api_data[pupdater.Metadata.info])

    def _test_latest_update(self):
        function_name('latest_update')

        result: dict = pupdater.latest_update()

        self.assertIsNone(result[pupdater.Metadata.latestVersion])
        self.assertIsNone(result[pupdater.Metadata.title])
        self.assertIsNone(result[pupdater.Metadata.description])

    def _test_is_updated(self):
        function_name('is_updated')

        pupdater.set_api_client(api_url=api_url)
        result: bool = pupdater.is_updated()

        self.assertFalse(result)

    def _test_download(self):
        function_name('download')

        pupdater.set_app_dir(path=app_dir)
        pupdater.set_api_client(api_url=api_url)
        download_result = pupdater.download()

        self.assertTrue(download_result)

    def _test_update(self):
        function_name('update')

        pupdater.set_app_dir(path=app_dir)
        pupdater.set_api_client(api_url=api_url)
        update_result = pupdater.update()

        self.assertTrue(update_result)


if __name__ == '__main__':
    unittest.main()
