import FWCore.ParameterSet.Config as cms

def RPCGeometryESModule(*args, **kwargs):
  mod = cms.ESProducer('RPCGeometryESModule',
    fromDDD = cms.untracked.bool(True),
    fromDD4hep = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
