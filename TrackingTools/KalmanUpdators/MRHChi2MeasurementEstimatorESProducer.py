import FWCore.ParameterSet.Config as cms

def MRHChi2MeasurementEstimatorESProducer(**kwargs):
  mod = cms.ESProducer('MRHChi2MeasurementEstimatorESProducer',
    MaxChi2 = cms.required.double,
    nSigma = cms.required.double,
    ComponentName = cms.required.string,
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
