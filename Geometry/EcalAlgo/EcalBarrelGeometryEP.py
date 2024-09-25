import FWCore.ParameterSet.Config as cms

def EcalBarrelGeometryEP(*args, **kwargs):
  mod = cms.ESProducer('EcalBarrelGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
