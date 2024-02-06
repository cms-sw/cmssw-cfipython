import FWCore.ParameterSet.Config as cms

trackerParameters = cms.ESProducer('TrackerParametersESModule',
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
