import FWCore.ParameterSet.Config as cms

mtdParameters = cms.ESProducer('MTDParametersESModule',
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
