import FWCore.ParameterSet.Config as cms

def PFCandidateMuonUntagger(**kwargs):
  mod = cms.EDProducer('PFCandidateMuonUntagger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
