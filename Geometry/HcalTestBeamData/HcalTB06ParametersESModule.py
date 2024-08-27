import FWCore.ParameterSet.Config as cms

def HcalTB06ParametersESModule(**kwargs):
  mod = cms.ESProducer('HcalTB06ParametersESModule',
    name1 = cms.string('WireChamber'),
    name2 = cms.string('HcalTB06BeamHits'),
    fromDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
