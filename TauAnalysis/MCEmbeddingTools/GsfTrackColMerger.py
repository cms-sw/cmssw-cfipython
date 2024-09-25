import FWCore.ParameterSet.Config as cms

def GsfTrackColMerger(*args, **kwargs):
  mod = cms.EDProducer('GsfTrackColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
