import FWCore.ParameterSet.Config as cms

def CloseComponentsMergerESProducer5D(**kwargs):
  mod = cms.ESProducer('CloseComponentsMergerESProducer5D',
    ComponentName = cms.required.string,
    MaxComponents = cms.required.int32,
    DistanceMeasure = cms.required.string,
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
