import FWCore.ParameterSet.Config as cms

def printTrackJet(*args, **kwargs):
  mod = cms.EDAnalyzer('printTrackJet',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
