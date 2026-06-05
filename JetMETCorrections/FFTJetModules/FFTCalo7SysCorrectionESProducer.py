import FWCore.ParameterSet.Config as cms

def FFTCalo7SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTCalo7SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
