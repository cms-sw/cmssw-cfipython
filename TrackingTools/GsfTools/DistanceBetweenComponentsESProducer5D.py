import FWCore.ParameterSet.Config as cms

def DistanceBetweenComponentsESProducer5D(*args, **kwargs):
  mod = cms.ESProducer('DistanceBetweenComponentsESProducer5D',
    DistanceMeasure = cms.required.string,
    ComponentName = cms.required.string,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
