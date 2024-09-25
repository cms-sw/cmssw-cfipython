import FWCore.ParameterSet.Config as cms

def EcalPreshowerGeometryEP(*args, **kwargs):
  mod = cms.ESProducer('EcalPreshowerGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
