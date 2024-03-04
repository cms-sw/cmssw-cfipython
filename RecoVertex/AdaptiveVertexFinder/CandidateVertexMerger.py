import FWCore.ParameterSet.Config as cms

def CandidateVertexMerger(**kwargs):
  mod = cms.EDProducer('CandidateVertexMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
