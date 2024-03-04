import FWCore.ParameterSet.Config as cms

def testSiteService(**kwargs):
  mod = cms.EDAnalyzer('testSiteService',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
