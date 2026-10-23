import FWCore.ParameterSet.Config as cms

def CompositeCandidateMatchEmbedder(*args, **kwargs):
  mod = cms.EDProducer('CompositeCandidateMatchEmbedder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
