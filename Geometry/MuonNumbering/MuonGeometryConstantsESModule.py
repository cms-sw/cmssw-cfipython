import FWCore.ParameterSet.Config as cms

def MuonGeometryConstantsESModule(**kwargs):
  mod = cms.ESProducer('MuonGeometryConstantsESModule',
    fromDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
