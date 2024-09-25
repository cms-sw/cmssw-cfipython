import FWCore.ParameterSet.Config as cms

def HcalGeometryFromDBEP(*args, **kwargs):
  mod = cms.ESProducer('HcalGeometryFromDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
