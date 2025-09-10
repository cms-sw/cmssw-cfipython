import FWCore.ParameterSet.Config as cms

def LaserAlignment(*args, **kwargs):
  mod = cms.EDProducer('LaserAlignment',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
