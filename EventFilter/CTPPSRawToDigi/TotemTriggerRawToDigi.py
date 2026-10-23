import FWCore.ParameterSet.Config as cms

def TotemTriggerRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('TotemTriggerRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
