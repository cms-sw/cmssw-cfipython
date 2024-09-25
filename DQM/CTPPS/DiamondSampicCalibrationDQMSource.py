import FWCore.ParameterSet.Config as cms

def DiamondSampicCalibrationDQMSource(*args, **kwargs):
  mod = cms.EDProducer('DiamondSampicCalibrationDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
