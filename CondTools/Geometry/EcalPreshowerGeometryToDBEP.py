import FWCore.ParameterSet.Config as cms

def EcalPreshowerGeometryToDBEP(**kwargs):
  mod = cms.ESProducer('EcalPreshowerGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
