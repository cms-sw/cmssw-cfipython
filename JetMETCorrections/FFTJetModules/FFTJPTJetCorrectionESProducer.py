import FWCore.ParameterSet.Config as cms

def FFTJPTJetCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTJPTJetCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
