import FWCore.ParameterSet.Config as cms

def FailingProducer(*args, **kwargs):
  mod = cms.EDProducer('FailingProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
