import FWCore.ParameterSet.Config as cms

def CaloTowerTopologyTester(**kwargs):
  mod = cms.EDAnalyzer('CaloTowerTopologyTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
