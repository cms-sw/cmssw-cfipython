import FWCore.ParameterSet.Config as cms

hcalSimulationParameters = cms.ESProducer('HcalSimParametersESModule',
  appendToDataLabel = cms.string('')
)
