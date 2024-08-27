import FWCore.ParameterSet.Config as cms

def RecoEcalCandidateSelector(**kwargs):
  mod = cms.EDFilter('RecoEcalCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
