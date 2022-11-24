import FWCore.ParameterSet.Config as cms

mkFitIterationConfigESProducer = cms.ESProducer('MkFitIterationConfigESProducer',
  ComponentName = cms.required.string,
  config = cms.required.FileInPath,
  minPt = cms.double(0),
  maxClusterSize = cms.uint32(8),
  appendToDataLabel = cms.string('')
)
