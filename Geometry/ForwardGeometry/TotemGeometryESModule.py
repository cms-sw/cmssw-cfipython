import FWCore.ParameterSet.Config as cms

def TotemGeometryESModule(**kwargs):
  mod = cms.ESProducer('TotemGeometryESModule',
    useDDL = cms.bool(True),
    useDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
