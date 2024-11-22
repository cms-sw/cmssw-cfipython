import FWCore.ParameterSet.Config as cms

def L1TStage2CaloLayer2DEClient(*args, **kwargs):
  mod = cms.EDProducer('L1TStage2CaloLayer2DEClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
