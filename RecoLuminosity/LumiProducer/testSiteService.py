import FWCore.ParameterSet.Config as cms

def testSiteService(*args, **kwargs):
  mod = cms.EDAnalyzer('testSiteService',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
