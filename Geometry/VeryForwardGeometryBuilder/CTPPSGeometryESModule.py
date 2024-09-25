import FWCore.ParameterSet.Config as cms

def CTPPSGeometryESModule(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
