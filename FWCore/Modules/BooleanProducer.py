import FWCore.ParameterSet.Config as cms

def BooleanProducer(*args, **kwargs):
  mod = cms.EDProducer('BooleanProducer',
    value = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
