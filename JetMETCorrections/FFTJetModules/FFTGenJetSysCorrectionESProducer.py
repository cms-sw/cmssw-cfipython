import FWCore.ParameterSet.Config as cms

def FFTGenJetSysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTGenJetSysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
