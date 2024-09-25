import FWCore.ParameterSet.Config as cms

def CloseComponentsMergerESProducer5D(*args, **kwargs):
  mod = cms.ESProducer('CloseComponentsMergerESProducer5D',
    ComponentName = cms.required.string,
    MaxComponents = cms.required.int32,
    DistanceMeasure = cms.required.string,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
