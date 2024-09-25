import FWCore.ParameterSet.Config as cms

def FFTCalo9SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTCalo9SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
