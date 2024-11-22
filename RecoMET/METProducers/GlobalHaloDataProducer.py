import FWCore.ParameterSet.Config as cms

def GlobalHaloDataProducer(*args, **kwargs):
  mod = cms.EDProducer('GlobalHaloDataProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
