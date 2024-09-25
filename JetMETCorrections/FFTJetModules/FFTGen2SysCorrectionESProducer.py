import FWCore.ParameterSet.Config as cms

def FFTGen2SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTGen2SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
