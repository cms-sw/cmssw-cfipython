import FWCore.ParameterSet.Config as cms

def MultiTrackValidator(**kwargs):
  mod = cms.EDProducer('MultiTrackValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
