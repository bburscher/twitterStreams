resp = self.session.request('POST',
                            url,
                            data=self.body,
                            timeout=self.timeout,
                            stream=True,
                            auth=auth,
                            verify=self.verify)