import FWCore.ParameterSet.Config as cms

def MuonDetLayerGeometryESProducer(*args, **kwargs):
  mod = cms.ESProducer('MuonDetLayerGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
