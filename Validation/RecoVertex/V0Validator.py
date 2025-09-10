import FWCore.ParameterSet.Config as cms

def V0Validator(*args, **kwargs):
  mod = cms.EDProducer('V0Validator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
