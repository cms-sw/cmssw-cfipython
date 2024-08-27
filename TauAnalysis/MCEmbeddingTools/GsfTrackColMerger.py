import FWCore.ParameterSet.Config as cms

def GsfTrackColMerger(**kwargs):
  mod = cms.EDProducer('GsfTrackColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
