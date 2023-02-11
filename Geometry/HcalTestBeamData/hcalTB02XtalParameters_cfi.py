import FWCore.ParameterSet.Config as cms

hcalTB02XtalParameters = cms.ESProducer('HcalTB02ParametersESModule',
  name = cms.string('EcalHitsEB'),
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
