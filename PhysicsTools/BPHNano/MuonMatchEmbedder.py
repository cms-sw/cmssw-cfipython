import FWCore.ParameterSet.Config as cms

def MuonMatchEmbedder(*args, **kwargs):
  mod = cms.EDProducer('MuonMatchEmbedder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
