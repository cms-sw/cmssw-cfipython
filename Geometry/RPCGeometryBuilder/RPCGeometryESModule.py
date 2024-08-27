import FWCore.ParameterSet.Config as cms

def RPCGeometryESModule(**kwargs):
  mod = cms.ESProducer('RPCGeometryESModule',
    fromDDD = cms.untracked.bool(True),
    fromDD4hep = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
