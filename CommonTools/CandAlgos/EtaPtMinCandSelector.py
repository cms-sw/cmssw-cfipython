import FWCore.ParameterSet.Config as cms

def EtaPtMinCandSelector(**kwargs):
  mod = cms.EDFilter('EtaPtMinCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
