import FWCore.ParameterSet.Config as cms

def EtaPtMinPdgIdCandSelector(*args, **kwargs):
  mod = cms.EDFilter('EtaPtMinPdgIdCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
