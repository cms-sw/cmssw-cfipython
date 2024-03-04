import FWCore.ParameterSet.Config as cms

def L1CaloTowerTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('L1CaloTowerTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
