import FWCore.ParameterSet.Config as cms

hcalSimulationParameters = cms.ESProducer('HcalSimParametersESModule',
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
