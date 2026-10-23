import FWCore.ParameterSet.Config as cms

def testEcalClusterFunctions(*args, **kwargs):
  mod = cms.EDAnalyzer('testEcalClusterFunctions',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
