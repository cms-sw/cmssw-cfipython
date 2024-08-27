import FWCore.ParameterSet.Config as cms

def FlexibleKFFittingSmootherESProducer(**kwargs):
  mod = cms.ESProducer('FlexibleKFFittingSmootherESProducer',
    ComponentName = cms.string('FlexibleKFFittingSmoother'),
    standardFitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    looperFitter = cms.string('LooperFittingSmoother'),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
