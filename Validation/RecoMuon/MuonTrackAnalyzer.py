import FWCore.ParameterSet.Config as cms

def MuonTrackAnalyzer(**kwargs):
  mod = cms.EDProducer('MuonTrackAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
