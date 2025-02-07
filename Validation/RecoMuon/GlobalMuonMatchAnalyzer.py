import FWCore.ParameterSet.Config as cms

def GlobalMuonMatchAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('GlobalMuonMatchAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
