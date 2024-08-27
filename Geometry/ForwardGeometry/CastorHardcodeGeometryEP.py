import FWCore.ParameterSet.Config as cms

def CastorHardcodeGeometryEP(**kwargs):
  mod = cms.ESProducer('CastorHardcodeGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
