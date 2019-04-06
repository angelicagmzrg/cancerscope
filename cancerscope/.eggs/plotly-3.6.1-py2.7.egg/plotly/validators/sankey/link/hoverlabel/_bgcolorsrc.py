import _plotly_utils.basevalidators


class BgcolorsrcValidator(_plotly_utils.basevalidators.SrcValidator):

    def __init__(
        self,
        plotly_name='bgcolorsrc',
        parent_name='sankey.link.hoverlabel',
        **kwargs
    ):
        super(BgcolorsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'none'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )
