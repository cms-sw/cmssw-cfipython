import FWCore.ParameterSet.Config as cms

def SiteLocalConfigServiceTester(**kwargs):
  mod = cms.EDAnalyzer('SiteLocalConfigServiceTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
