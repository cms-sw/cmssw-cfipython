import FWCore.ParameterSet.Config as cms

def DTPreCalibrationTask(*args, **kwargs):
  mod = cms.EDProducer('DTPreCalibrationTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
