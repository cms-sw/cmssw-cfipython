import FWCore.ParameterSet.Config as cms

def RecoEcalCandidateRefSelector(*args, **kwargs):
  mod = cms.EDFilter('RecoEcalCandidateRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
