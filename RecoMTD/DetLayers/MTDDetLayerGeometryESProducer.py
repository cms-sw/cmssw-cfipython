import FWCore.ParameterSet.Config as cms

def MTDDetLayerGeometryESProducer(**kwargs):
  mod = cms.ESProducer('MTDDetLayerGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
