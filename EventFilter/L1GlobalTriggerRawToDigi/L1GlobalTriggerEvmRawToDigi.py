import FWCore.ParameterSet.Config as cms

def L1GlobalTriggerEvmRawToDigi(**kwargs):
  mod = cms.EDProducer('L1GlobalTriggerEvmRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
