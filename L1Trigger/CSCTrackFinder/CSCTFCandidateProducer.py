import FWCore.ParameterSet.Config as cms

def CSCTFCandidateProducer(**kwargs):
  mod = cms.EDProducer('CSCTFCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
