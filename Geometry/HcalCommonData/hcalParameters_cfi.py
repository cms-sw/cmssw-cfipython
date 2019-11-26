import FWCore.ParameterSet.Config as cms

hcalParameters = cms.ESProducer('HcalParametersESModule',
  fromDD4Hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
