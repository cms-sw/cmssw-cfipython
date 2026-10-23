import FWCore.ParameterSet.Config as cms

def FFTCalo4CorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTCalo4CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
