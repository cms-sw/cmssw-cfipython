import FWCore.ParameterSet.Config as cms

def EtaPtMinCandSelector(*args, **kwargs):
  mod = cms.EDFilter('EtaPtMinCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
