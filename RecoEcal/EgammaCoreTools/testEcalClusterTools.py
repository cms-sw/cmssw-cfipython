import FWCore.ParameterSet.Config as cms

def testEcalClusterTools(**kwargs):
  mod = cms.EDAnalyzer('testEcalClusterTools',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
