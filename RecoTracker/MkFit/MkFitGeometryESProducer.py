import FWCore.ParameterSet.Config as cms

def MkFitGeometryESProducer(**kwargs):
  mod = cms.ESProducer('MkFitGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
