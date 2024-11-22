import FWCore.ParameterSet.Config as cms

def RecoEcalCandidateSelector(*args, **kwargs):
  mod = cms.EDFilter('RecoEcalCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
