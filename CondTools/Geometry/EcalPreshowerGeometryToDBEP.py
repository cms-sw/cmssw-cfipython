import FWCore.ParameterSet.Config as cms

def EcalPreshowerGeometryToDBEP(*args, **kwargs):
  mod = cms.ESProducer('EcalPreshowerGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
