import FWCore.ParameterSet.Config as cms

def Chi2MeasurementEstimatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('Chi2MeasurementEstimatorESProducer',
    MaxChi2 = cms.double(30),
    nSigma = cms.double(3),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinimalTolerance = cms.double(0.5),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    ComponentName = cms.string('Chi2'),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
