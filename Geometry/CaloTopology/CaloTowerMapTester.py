import FWCore.ParameterSet.Config as cms

def CaloTowerMapTester(**kwargs):
  mod = cms.EDAnalyzer('CaloTowerMapTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
