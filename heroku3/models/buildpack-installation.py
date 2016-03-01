from . import BaseResource, BuildPack


class BuildpackInstallation(BaseResource):
    """Heroku Buildpack Insallation."""

    _map = {'buildpack': Buildpack}
    _ints = ['ordinal']
    _pks = ['ordinal']

    def __repr__(self):
        return "<buildpack-installation '{}'>".format(self.buildpack)

    def update(self, buildpacks):
        r = self._h._http_resource(
            method='PUT',
            resource=('apps', self.app.id, 'buildpack-installations'),
            data=buildpacks
            )
        )
        r.raise_for_status()
        return r.ok
