import FWCore.ParameterSet.Config as cms

caloSimulationParameters = cms.ESProducer('CaloSimParametersESModule',
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
