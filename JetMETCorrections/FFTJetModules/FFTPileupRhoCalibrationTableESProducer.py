import FWCore.ParameterSet.Config as cms

def FFTPileupRhoCalibrationTableESProducer(**kwargs):
  mod = cms.ESProducer('FFTPileupRhoCalibrationTableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
