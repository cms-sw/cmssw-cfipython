import FWCore.ParameterSet.Config as cms

hcalSimulationParameters = cms.ESProducer('HcalSimParametersESModule',
  fromDD4Hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
