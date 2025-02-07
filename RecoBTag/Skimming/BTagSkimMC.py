import FWCore.ParameterSet.Config as cms

def BTagSkimMC(*args, **kwargs):
  mod = cms.EDFilter('BTagSkimMC',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
