import FWCore.ParameterSet.Config as cms

hcalTB06BeamParameters = cms.ESProducer('HcalTB06ParametersESModule',
  name1 = cms.string('WireChamber'),
  name2 = cms.string('HcalTB06BeamHits'),
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
