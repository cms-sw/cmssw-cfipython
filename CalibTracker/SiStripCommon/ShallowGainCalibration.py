import FWCore.ParameterSet.Config as cms

def ShallowGainCalibration(**kwargs):
  mod = cms.EDProducer('ShallowGainCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
