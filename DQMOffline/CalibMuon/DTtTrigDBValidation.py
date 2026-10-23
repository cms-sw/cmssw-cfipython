import FWCore.ParameterSet.Config as cms

def DTtTrigDBValidation(*args, **kwargs):
  mod = cms.EDProducer('DTtTrigDBValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
