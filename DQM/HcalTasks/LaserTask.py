import FWCore.ParameterSet.Config as cms

def LaserTask(*args, **kwargs):
  mod = cms.EDProducer('LaserTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
