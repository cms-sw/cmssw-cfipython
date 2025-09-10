import FWCore.ParameterSet.Config as cms

def FFTCalo3SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTCalo3SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
