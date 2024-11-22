import FWCore.ParameterSet.Config as cms

def PATCompositeCandidateSelector(*args, **kwargs):
  mod = cms.EDFilter('PATCompositeCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
