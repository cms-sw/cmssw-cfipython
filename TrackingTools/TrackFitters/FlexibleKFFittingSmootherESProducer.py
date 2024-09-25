import FWCore.ParameterSet.Config as cms

def FlexibleKFFittingSmootherESProducer(*args, **kwargs):
  mod = cms.ESProducer('FlexibleKFFittingSmootherESProducer',
    ComponentName = cms.string('FlexibleKFFittingSmoother'),
    standardFitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    looperFitter = cms.string('LooperFittingSmoother'),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
