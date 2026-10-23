import FWCore.ParameterSet.Config as cms

def FFTGen1SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTGen1SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
