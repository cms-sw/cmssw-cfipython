import FWCore.ParameterSet.Config as cms

def FFTCalo1CorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTCalo1CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
