import FWCore.ParameterSet.Config as cms

def HcalTB06ParametersESModule(*args, **kwargs):
  mod = cms.ESProducer('HcalTB06ParametersESModule',
    name1 = cms.string('WireChamber'),
    name2 = cms.string('HcalTB06BeamHits'),
    fromDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
