import FWCore.ParameterSet.Config as cms

def DTGeometryESProducer(**kwargs):
  mod = cms.ESProducer('DTGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
