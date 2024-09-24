import FWCore.ParameterSet.Config as cms

def Chi2ChargeMeasurementEstimatorESProducer(**kwargs):
  mod = cms.ESProducer('Chi2ChargeMeasurementEstimatorESProducer',
    MaxChi2 = cms.double(30),
    nSigma = cms.double(3),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinimalTolerance = cms.double(0.5),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    ComponentName = cms.string('Chi2Charge'),
    pTChargeCutThreshold = cms.double(-1),
    clusterChargeCut = cms.PSet(
      value = cms.double(1620)
    ),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod