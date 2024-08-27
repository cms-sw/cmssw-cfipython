import FWCore.ParameterSet.Config as cms

def L2MuonCandidateProducer(**kwargs):
  mod = cms.EDProducer('L2MuonCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
