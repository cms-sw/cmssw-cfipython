import FWCore.ParameterSet.Config as cms

CTPPSGeometryESModule = cms.ESProducer('CTPPSGeometryESModule',
  verbosity = cms.untracked.uint32(1),
  isRun2 = cms.bool(False),
  dbTag = cms.string(''),
  compactViewTag = cms.string(''),
  fromPreprocessedDB = cms.untracked.bool(False),
  fromDD4hep = cms.untracked.bool(False),
  appendToDataLabel = cms.string('')
)
