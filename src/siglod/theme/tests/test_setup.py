# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from siglod.theme.testing import SIGLOD_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that siglod.theme is properly installed."""

    layer = SIGLOD_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if siglod.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'siglod.theme'))

    def test_browserlayer(self):
        """Test that ISiglodThemeLayer is registered."""
        from siglod.theme.interfaces import (
            ISiglodThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(ISiglodThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SIGLOD_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['siglod.theme'])

    def test_product_uninstalled(self):
        """Test if siglod.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'siglod.theme'))
