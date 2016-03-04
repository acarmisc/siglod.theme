# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import siglod.theme


class SiglodThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=siglod.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'siglod.theme:default')


SIGLOD_THEME_FIXTURE = SiglodThemeLayer()


SIGLOD_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SIGLOD_THEME_FIXTURE,),
    name='SiglodThemeLayer:IntegrationTesting'
)


SIGLOD_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SIGLOD_THEME_FIXTURE,),
    name='SiglodThemeLayer:FunctionalTesting'
)


SIGLOD_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SIGLOD_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='SiglodThemeLayer:AcceptanceTesting'
)
