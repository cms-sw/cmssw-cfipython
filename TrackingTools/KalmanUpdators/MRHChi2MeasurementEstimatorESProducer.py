import FWCore.ParameterSet.Config as cms

def MRHChi2MeasurementEstimatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('MRHChi2MeasurementEstimatorESProducer',
    MaxChi2 = cms.required.double,
    nSigma = cms.required.double,
    ComponentName = cms.required.string,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
