import FWCore.ParameterSet.Config as cms

def EcalPreshowerGeometryEPdd4hep(**kwargs):
  mod = cms.ESProducer('EcalPreshowerGeometryEPdd4hep',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
