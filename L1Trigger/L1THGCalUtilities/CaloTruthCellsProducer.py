import FWCore.ParameterSet.Config as cms

def CaloTruthCellsProducer(**kwargs):
  mod = cms.EDProducer('CaloTruthCellsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
