import FWCore.ParameterSet.Config as cms

def RecoEcalCandidateRefSelector(**kwargs):
  mod = cms.EDFilter('RecoEcalCandidateRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
