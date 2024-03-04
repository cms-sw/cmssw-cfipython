import FWCore.ParameterSet.Config as cms

def CTPPSGeometryESModule(**kwargs):
  mod = cms.ESProducer('CTPPSGeometryESModule',
    verbosity = cms.untracked.uint32(1),
    buildMisalignedGeometry = cms.bool(False),
    isRun2 = cms.bool(False),
    dbTag = cms.string(''),
    compactViewTag = cms.string(''),
    fromPreprocessedDB = cms.untracked.bool(False),
    fromDD4hep = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
