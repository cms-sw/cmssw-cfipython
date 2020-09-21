import FWCore.ParameterSet.Config as cms

trackerParameters = cms.ESProducer('TrackerParametersESModule',
  fromDD4Hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
