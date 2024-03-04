import FWCore.ParameterSet.Config as cms

def printPartonJet(**kwargs):
  mod = cms.EDAnalyzer('printPartonJet',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
