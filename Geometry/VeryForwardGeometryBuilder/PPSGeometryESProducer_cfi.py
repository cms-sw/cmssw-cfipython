import FWCore.ParameterSet.Config as cms

PPSGeometryESProducer = cms.ESProducer('PPSGeometryESProducer',
  verbosity = cms.untracked.uint32(1),
  detectorTag = cms.string(''),
  appendToDataLabel = cms.string('')
)
