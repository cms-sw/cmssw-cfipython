import FWCore.ParameterSet.Config as cms

def SiteLocalConfigServiceCatalogTester(**kwargs):
  mod = cms.EDAnalyzer('SiteLocalConfigServiceCatalogTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
