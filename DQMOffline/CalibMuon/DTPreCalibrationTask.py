import FWCore.ParameterSet.Config as cms

def DTPreCalibrationTask(**kwargs):
  mod = cms.EDProducer('DTPreCalibrationTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
