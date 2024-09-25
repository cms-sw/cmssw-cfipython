import FWCore.ParameterSet.Config as cms

def ShallowGainCalibration(*args, **kwargs):
  mod = cms.EDProducer('ShallowGainCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
