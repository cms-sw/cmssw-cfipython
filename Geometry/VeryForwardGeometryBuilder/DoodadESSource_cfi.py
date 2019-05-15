import FWCore.ParameterSet.Config as cms

DoodadESSource = cms.ESProducer('CTPPSGeometryESModule',
  verbosity = cms.untracked.uint32(1),
  compactViewTag = cms.string(''),
  appendToDataLabel = cms.string('')
)
