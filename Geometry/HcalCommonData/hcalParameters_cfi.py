import FWCore.ParameterSet.Config as cms

hcalParameters = cms.ESProducer('HcalParametersESModule',
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
