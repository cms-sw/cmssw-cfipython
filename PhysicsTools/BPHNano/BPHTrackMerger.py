import FWCore.ParameterSet.Config as cms

def BPHTrackMerger(*args, **kwargs):
  mod = cms.EDProducer('BPHTrackMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
