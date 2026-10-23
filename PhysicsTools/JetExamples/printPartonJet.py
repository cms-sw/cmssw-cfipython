import FWCore.ParameterSet.Config as cms

def printPartonJet(*args, **kwargs):
  mod = cms.EDAnalyzer('printPartonJet',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
