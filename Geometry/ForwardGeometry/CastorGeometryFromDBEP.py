import FWCore.ParameterSet.Config as cms

def CastorGeometryFromDBEP(*args, **kwargs):
  mod = cms.ESProducer('CastorGeometryFromDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
