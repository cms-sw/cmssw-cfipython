import FWCore.ParameterSet.Config as cms

CTPPSGeometryESModule = cms.ESProducer('CTPPSGeometryESModule',
  verbosity = cms.untracked.uint32(1),
  compactViewTag = cms.string(''),
  fromDD4hep = cms.untracked.bool(False),
  appendToDataLabel = cms.string('')
)
