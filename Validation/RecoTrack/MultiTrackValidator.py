import FWCore.ParameterSet.Config as cms

def MultiTrackValidator(*args, **kwargs):
  mod = cms.EDProducer('MultiTrackValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
