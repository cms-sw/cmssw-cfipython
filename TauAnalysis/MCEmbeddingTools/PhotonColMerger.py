import FWCore.ParameterSet.Config as cms

def PhotonColMerger(*args, **kwargs):
  mod = cms.EDProducer('PhotonColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
