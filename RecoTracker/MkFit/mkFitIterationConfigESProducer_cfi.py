import FWCore.ParameterSet.Config as cms

mkFitIterationConfigESProducer = cms.ESProducer('MkFitIterationConfigESProducer',
  ComponentName = cms.required.string,
  config = cms.required.FileInPath,
  minPt = cms.double(0),
  appendToDataLabel = cms.string('')
)
