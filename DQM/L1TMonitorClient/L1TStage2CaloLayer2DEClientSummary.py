import FWCore.ParameterSet.Config as cms

def L1TStage2CaloLayer2DEClientSummary(**kwargs):
  mod = cms.EDProducer('L1TStage2CaloLayer2DEClientSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
