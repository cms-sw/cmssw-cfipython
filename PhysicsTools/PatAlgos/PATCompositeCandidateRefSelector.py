import FWCore.ParameterSet.Config as cms

def PATCompositeCandidateRefSelector(**kwargs):
  mod = cms.EDFilter('PATCompositeCandidateRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
