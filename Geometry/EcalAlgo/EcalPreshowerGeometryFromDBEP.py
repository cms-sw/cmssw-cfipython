import FWCore.ParameterSet.Config as cms

def EcalPreshowerGeometryFromDBEP(*args, **kwargs):
  mod = cms.ESProducer('EcalPreshowerGeometryFromDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
