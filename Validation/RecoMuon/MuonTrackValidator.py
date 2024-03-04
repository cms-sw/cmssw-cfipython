import FWCore.ParameterSet.Config as cms

def MuonTrackValidator(**kwargs):
  mod = cms.EDProducer('MuonTrackValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
