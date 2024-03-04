import FWCore.ParameterSet.Config as cms

def CastorDbProducer(**kwargs):
  mod = cms.ESProducer('CastorDbProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
