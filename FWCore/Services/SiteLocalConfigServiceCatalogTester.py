import FWCore.ParameterSet.Config as cms

def SiteLocalConfigServiceCatalogTester(*args, **kwargs):
  mod = cms.EDAnalyzer('SiteLocalConfigServiceCatalogTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
