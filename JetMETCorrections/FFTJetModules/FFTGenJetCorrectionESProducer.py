import FWCore.ParameterSet.Config as cms

def FFTGenJetCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTGenJetCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
