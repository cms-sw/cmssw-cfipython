import FWCore.ParameterSet.Config as cms

def HcalHardcodeGeometryEP(*args, **kwargs):
  mod = cms.ESProducer('HcalHardcodeGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
