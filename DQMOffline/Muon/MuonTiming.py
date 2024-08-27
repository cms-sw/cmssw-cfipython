import FWCore.ParameterSet.Config as cms

def MuonTiming(**kwargs):
  mod = cms.EDProducer('MuonTiming',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
