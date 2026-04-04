import FWCore.ParameterSet.Config as cms

def GlobalTrackingGeometryESProducer(*args, **kwargs):
  mod = cms.ESProducer('GlobalTrackingGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
