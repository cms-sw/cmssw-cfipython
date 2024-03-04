import FWCore.ParameterSet.Config as cms

def BTagSkimLeptonJet(**kwargs):
  mod = cms.EDFilter('BTagSkimLeptonJet',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
