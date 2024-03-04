import FWCore.ParameterSet.Config as cms

def DAFTrackProducer(**kwargs):
  mod = cms.EDProducer('DAFTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
