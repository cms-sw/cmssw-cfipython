import FWCore.ParameterSet.Config as cms

def PatBJetTrackAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PatBJetTrackAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
