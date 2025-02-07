import FWCore.ParameterSet.Config as cms

def CaloTowerTopologyTester(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloTowerTopologyTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
