import FWCore.ParameterSet.Config as cms

def CaloTowerMapTester(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloTowerMapTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
