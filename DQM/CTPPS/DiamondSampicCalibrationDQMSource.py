import FWCore.ParameterSet.Config as cms

def DiamondSampicCalibrationDQMSource(**kwargs):
  mod = cms.EDProducer('DiamondSampicCalibrationDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
