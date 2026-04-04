import FWCore.ParameterSet.Config as cms

def FFTPileupRhoCalibrationTableESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPileupRhoCalibrationTableESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
