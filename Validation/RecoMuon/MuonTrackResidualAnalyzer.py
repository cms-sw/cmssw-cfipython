import FWCore.ParameterSet.Config as cms

def MuonTrackResidualAnalyzer(**kwargs):
  mod = cms.EDProducer('MuonTrackResidualAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
