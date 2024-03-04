import FWCore.ParameterSet.Config as cms

def BTagSkimMC(**kwargs):
  mod = cms.EDFilter('BTagSkimMC',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
