import FWCore.ParameterSet.Config as cms

def FWRecoGeometryESProducer(**kwargs):
  mod = cms.ESProducer('FWRecoGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
