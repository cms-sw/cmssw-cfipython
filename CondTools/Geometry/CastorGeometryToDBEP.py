import FWCore.ParameterSet.Config as cms

def CastorGeometryToDBEP(*args, **kwargs):
  mod = cms.ESProducer('CastorGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
