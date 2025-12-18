import FWCore.ParameterSet.Config as cms

def FFTCaloJetCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTCaloJetCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
