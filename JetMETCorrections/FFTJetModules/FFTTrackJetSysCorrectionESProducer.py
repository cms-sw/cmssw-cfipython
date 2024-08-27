import FWCore.ParameterSet.Config as cms

def FFTTrackJetSysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTTrackJetSysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
