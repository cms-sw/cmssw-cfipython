import FWCore.ParameterSet.Config as cms

def DistanceBetweenComponentsESProducer5D(**kwargs):
  mod = cms.ESProducer('DistanceBetweenComponentsESProducer5D',
    DistanceMeasure = cms.required.string,
    ComponentName = cms.required.string,
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
