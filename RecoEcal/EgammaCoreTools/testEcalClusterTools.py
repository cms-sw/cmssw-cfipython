import FWCore.ParameterSet.Config as cms

def testEcalClusterTools(*args, **kwargs):
  mod = cms.EDAnalyzer('testEcalClusterTools',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
