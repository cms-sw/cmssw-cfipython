import FWCore.ParameterSet.Config as cms

def GlobalDigisProducer(*args, **kwargs):
  mod = cms.EDProducer('GlobalDigisProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
