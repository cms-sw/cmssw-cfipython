import FWCore.ParameterSet.Config as cms

def HGCalGeometryESProducer(**kwargs):
  mod = cms.ESProducer('HGCalGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
