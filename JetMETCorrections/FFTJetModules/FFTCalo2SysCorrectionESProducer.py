import FWCore.ParameterSet.Config as cms

def FFTCalo2SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTCalo2SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
