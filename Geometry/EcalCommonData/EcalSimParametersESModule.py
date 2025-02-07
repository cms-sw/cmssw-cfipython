import FWCore.ParameterSet.Config as cms

def EcalSimParametersESModule(*args, **kwargs):
  mod = cms.ESProducer('EcalSimParametersESModule',
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsEB'),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
