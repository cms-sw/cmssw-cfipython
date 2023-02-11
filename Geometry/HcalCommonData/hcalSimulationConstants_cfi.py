import FWCore.ParameterSet.Config as cms

hcalSimulationConstants = cms.ESProducer('HcalSimulationConstantsESModule',
  appendToDataLabel = cms.string('')
)
