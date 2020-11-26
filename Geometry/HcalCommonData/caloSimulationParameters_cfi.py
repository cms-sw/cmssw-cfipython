import FWCore.ParameterSet.Config as cms

caloSimulationParameters = cms.ESProducer('CaloSimParametersESModule',
  fromDD4Hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
