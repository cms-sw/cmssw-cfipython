import FWCore.ParameterSet.Config as cms

def MuonSeedsAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('MuonSeedsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
