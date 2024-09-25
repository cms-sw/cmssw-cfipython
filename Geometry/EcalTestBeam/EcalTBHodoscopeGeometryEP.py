import FWCore.ParameterSet.Config as cms

def EcalTBHodoscopeGeometryEP(*args, **kwargs):
  mod = cms.ESProducer('EcalTBHodoscopeGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
