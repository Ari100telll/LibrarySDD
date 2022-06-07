from utils.base_decorators import singleton


@singleton
class UrlManager:
    ENDPOINTS_PARAMS = []

    def add_endpoint(
        self,
        endpoint=None,
        endpoint_name=None,
        handler=None,
        methods=("GET",),
        *args,
        **kwargs
    ):
        self.ENDPOINTS_PARAMS.append(
            (
                args,
                {
                    "endpoint": endpoint,
                    "endpoint_name": endpoint_name,
                    "handler": handler,
                    "methods": methods,
                    **kwargs,
                },
            )
        )

    def setup_endpoints(self, app):
        for endpoint_params in self.ENDPOINTS_PARAMS:
            args, kwargs = endpoint_params
            app.add_endpoint(*args, **kwargs)
