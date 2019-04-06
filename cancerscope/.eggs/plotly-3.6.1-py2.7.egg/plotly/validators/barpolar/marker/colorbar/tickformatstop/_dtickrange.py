import _plotly_utils.basevalidators


class DtickrangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self,
        plotly_name='dtickrange',
        parent_name='barpolar.marker.colorbar.tickformatstop',
        **kwargs
    ):
        super(DtickrangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'colorbars'),
            items=kwargs.pop(
                'items', [
                    {
                        'valType': 'any',
                        'editType': 'colorbars'
                    }, {
                        'valType': 'any',
                        'editType': 'colorbars'
                    }
                ]
            ),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )
