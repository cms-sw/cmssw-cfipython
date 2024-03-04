import FWCore.ParameterSet.Config as cms

def EcalPreshowerGeometryEP(**kwargs):
  mod = cms.ESProducer('EcalPreshowerGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
