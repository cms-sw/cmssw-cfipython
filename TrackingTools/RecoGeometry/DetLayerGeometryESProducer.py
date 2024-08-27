import FWCore.ParameterSet.Config as cms

def DetLayerGeometryESProducer(**kwargs):
  mod = cms.ESProducer('DetLayerGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
