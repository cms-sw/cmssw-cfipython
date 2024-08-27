import FWCore.ParameterSet.Config as cms

def GlobalTrackingGeometryESProducer(**kwargs):
  mod = cms.ESProducer('GlobalTrackingGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
