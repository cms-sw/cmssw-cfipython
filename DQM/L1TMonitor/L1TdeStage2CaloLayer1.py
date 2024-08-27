import FWCore.ParameterSet.Config as cms

def L1TdeStage2CaloLayer1(**kwargs):
  mod = cms.EDProducer('L1TdeStage2CaloLayer1',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
