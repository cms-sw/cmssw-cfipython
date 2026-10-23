import FWCore.ParameterSet.Config as cms

def FFTJPTJetSysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTJPTJetSysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
