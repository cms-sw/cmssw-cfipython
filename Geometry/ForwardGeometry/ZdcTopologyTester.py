import FWCore.ParameterSet.Config as cms

def ZdcTopologyTester(*args, **kwargs):
  mod = cms.EDAnalyzer('ZdcTopologyTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
