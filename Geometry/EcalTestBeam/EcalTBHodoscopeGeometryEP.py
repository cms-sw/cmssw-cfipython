import FWCore.ParameterSet.Config as cms

def EcalTBHodoscopeGeometryEP(**kwargs):
  mod = cms.ESProducer('EcalTBHodoscopeGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
