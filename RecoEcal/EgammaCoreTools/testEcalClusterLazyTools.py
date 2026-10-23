import FWCore.ParameterSet.Config as cms

def testEcalClusterLazyTools(*args, **kwargs):
  mod = cms.EDAnalyzer('testEcalClusterLazyTools',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
