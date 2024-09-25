import FWCore.ParameterSet.Config as cms

def IntListProducer(*args, **kwargs):
  mod = cms.EDProducer('IntListProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
