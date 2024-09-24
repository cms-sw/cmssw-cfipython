import FWCore.ParameterSet.Config as cms

def ReducedEGProducer(*args, **kwargs):
  mod = cms.EDProducer('ReducedEGProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
