import FWCore.ParameterSet.Config as cms

def IntDequeProducer(*args, **kwargs):
  mod = cms.EDProducer('IntDequeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
