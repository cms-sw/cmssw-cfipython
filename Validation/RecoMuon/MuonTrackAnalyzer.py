import FWCore.ParameterSet.Config as cms

def MuonTrackAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('MuonTrackAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
