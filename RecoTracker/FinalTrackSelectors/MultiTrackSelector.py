import FWCore.ParameterSet.Config as cms

def MultiTrackSelector(**kwargs):
  mod = cms.EDProducer('MultiTrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
