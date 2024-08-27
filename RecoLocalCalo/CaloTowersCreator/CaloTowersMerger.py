import FWCore.ParameterSet.Config as cms

def CaloTowersMerger(**kwargs):
  mod = cms.EDProducer('CaloTowersMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
