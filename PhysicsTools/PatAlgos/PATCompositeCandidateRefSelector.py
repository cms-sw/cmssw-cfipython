import FWCore.ParameterSet.Config as cms

def PATCompositeCandidateRefSelector(*args, **kwargs):
  mod = cms.EDFilter('PATCompositeCandidateRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
