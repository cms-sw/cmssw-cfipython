import FWCore.ParameterSet.Config as cms

def TotemGeometryESModule(*args, **kwargs):
  mod = cms.ESProducer('TotemGeometryESModule',
    useDDL = cms.bool(True),
    useDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
