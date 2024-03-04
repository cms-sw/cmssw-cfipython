import FWCore.ParameterSet.Config as cms

def MuonSeedsAnalyzer(**kwargs):
  mod = cms.EDProducer('MuonSeedsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
