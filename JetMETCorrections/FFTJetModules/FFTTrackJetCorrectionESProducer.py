import FWCore.ParameterSet.Config as cms

def FFTTrackJetCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTTrackJetCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
