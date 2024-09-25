import FWCore.ParameterSet.Config as cms

def L1TdeStage2CaloLayer1(*args, **kwargs):
  mod = cms.EDProducer('L1TdeStage2CaloLayer1',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
