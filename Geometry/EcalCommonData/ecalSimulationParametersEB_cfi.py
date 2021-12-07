import FWCore.ParameterSet.Config as cms

ecalSimulationParametersEB = cms.ESProducer('EcalSimParametersESModule',
  fromDD4hep = cms.bool(False),
  name = cms.string('EcalHitsEB'),
  appendToDataLabel = cms.string('')
)
