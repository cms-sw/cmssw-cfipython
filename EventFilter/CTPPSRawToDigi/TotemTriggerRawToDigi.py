import FWCore.ParameterSet.Config as cms

def TotemTriggerRawToDigi(**kwargs):
  mod = cms.EDProducer('TotemTriggerRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
