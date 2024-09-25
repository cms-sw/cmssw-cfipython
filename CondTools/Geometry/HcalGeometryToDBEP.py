import FWCore.ParameterSet.Config as cms

def HcalGeometryToDBEP(*args, **kwargs):
  mod = cms.ESProducer('HcalGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
