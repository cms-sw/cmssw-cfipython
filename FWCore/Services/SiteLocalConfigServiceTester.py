import FWCore.ParameterSet.Config as cms

def SiteLocalConfigServiceTester(*args, **kwargs):
  mod = cms.EDAnalyzer('SiteLocalConfigServiceTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
