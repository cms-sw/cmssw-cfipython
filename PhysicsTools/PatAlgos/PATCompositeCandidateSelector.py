import FWCore.ParameterSet.Config as cms

def PATCompositeCandidateSelector(**kwargs):
  mod = cms.EDFilter('PATCompositeCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
