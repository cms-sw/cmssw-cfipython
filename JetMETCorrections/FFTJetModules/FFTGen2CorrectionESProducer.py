import FWCore.ParameterSet.Config as cms

def FFTGen2CorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTGen2CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
