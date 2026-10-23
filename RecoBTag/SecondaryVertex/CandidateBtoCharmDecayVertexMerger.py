import FWCore.ParameterSet.Config as cms

def CandidateBtoCharmDecayVertexMerger(*args, **kwargs):
  mod = cms.EDProducer('CandidateBtoCharmDecayVertexMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
