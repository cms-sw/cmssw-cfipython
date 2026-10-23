import FWCore.ParameterSet.Config as cms

def HcalDDDGeometryEP(*args, **kwargs):
  mod = cms.ESProducer('HcalDDDGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
