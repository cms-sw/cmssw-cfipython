import FWCore.ParameterSet.Config as cms

def PFDisplacedVertexCandidateProducer(**kwargs):
  mod = cms.EDProducer('PFDisplacedVertexCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
