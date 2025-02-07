import FWCore.ParameterSet.Config as cms

def EcalBarrelGeometryFromDBEP(*args, **kwargs):
  mod = cms.ESProducer('EcalBarrelGeometryFromDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
