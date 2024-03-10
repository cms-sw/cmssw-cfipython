import FWCore.ParameterSet.Config as cms

mkFitIterationConfigESProducer = cms.ESProducer('MkFitIterationConfigESProducer',
  ComponentName = cms.string(''),
  config = cms.FileInPath(),
  minPt = cms.double(0),
  maxClusterSize = cms.uint32(8),
  appendToDataLabel = cms.string('')
)
