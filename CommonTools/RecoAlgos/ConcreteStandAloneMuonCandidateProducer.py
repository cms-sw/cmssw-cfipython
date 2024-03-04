import FWCore.ParameterSet.Config as cms

def ConcreteStandAloneMuonCandidateProducer(**kwargs):
  mod = cms.EDProducer('ConcreteStandAloneMuonCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
