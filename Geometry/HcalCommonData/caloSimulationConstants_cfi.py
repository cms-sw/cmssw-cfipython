import FWCore.ParameterSet.Config as cms

caloSimulationConstants = cms.ESProducer('CaloSimulationConstantsESModule',
  appendToDataLabel = cms.string('')
)
