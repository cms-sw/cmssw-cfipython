import FWCore.ParameterSet.Config as cms

def testEcalClusterSeverityAlgo(*args, **kwargs):
  mod = cms.EDAnalyzer('testEcalClusterSeverityAlgo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
