import FWCore.ParameterSet.Config as cms

def TauValidation(*args, **kwargs):
  mod = cms.EDProducer('TauValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
