import FWCore.ParameterSet.Config as cms

ppsPixelTopologyESSource = cms.ESSource('PPSPixelTopologyESSource',
  RunType = cms.string('Run3'),
  PitchSimY = cms.double(0.15),
  PitchSimX = cms.double(0.1),
  thickness = cms.double(0.23),
  noOfPixelSimX = cms.int32(160),
  noOfPixelSimY = cms.int32(104),
  noOfPixels = cms.int32(16640),
  simXWidth = cms.double(16.6),
  simYWidth = cms.double(16.2),
  deadEdgeWidth = cms.double(0.2),
  activeEdgeSigma = cms.double(0.02),
  physActiveEdgeDist = cms.double(0.15),
  appendToDataLabel = cms.string('')
)
