import FWCore.ParameterSet.Config as cms

def EcalBarrelGeometryToDBEP(*args, **kwargs):
  mod = cms.ESProducer('EcalBarrelGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
