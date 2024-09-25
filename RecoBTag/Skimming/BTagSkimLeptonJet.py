import FWCore.ParameterSet.Config as cms

def BTagSkimLeptonJet(*args, **kwargs):
  mod = cms.EDFilter('BTagSkimLeptonJet',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
