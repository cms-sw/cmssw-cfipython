import FWCore.ParameterSet.Config as cms

def DetLayerGeometryESProducer(*args, **kwargs):
  mod = cms.ESProducer('DetLayerGeometryESProducer',
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
