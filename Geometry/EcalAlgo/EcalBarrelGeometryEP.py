import FWCore.ParameterSet.Config as cms

def EcalBarrelGeometryEP(**kwargs):
  mod = cms.ESProducer('EcalBarrelGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
