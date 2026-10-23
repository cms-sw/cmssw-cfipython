import FWCore.ParameterSet.Config as cms

def HitReCalibrator(*args, **kwargs):
  mod = cms.EDProducer('HitReCalibrator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
