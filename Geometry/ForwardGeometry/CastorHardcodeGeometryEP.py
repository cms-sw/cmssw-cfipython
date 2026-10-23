import FWCore.ParameterSet.Config as cms

def CastorHardcodeGeometryEP(*args, **kwargs):
  mod = cms.ESProducer('CastorHardcodeGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
