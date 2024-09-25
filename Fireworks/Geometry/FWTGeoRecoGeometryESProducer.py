import FWCore.ParameterSet.Config as cms

def FWTGeoRecoGeometryESProducer(*args, **kwargs):
  mod = cms.ESProducer('FWTGeoRecoGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
