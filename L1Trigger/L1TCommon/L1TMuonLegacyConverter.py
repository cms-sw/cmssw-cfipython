import FWCore.ParameterSet.Config as cms

def L1TMuonLegacyConverter(**kwargs):
  mod = cms.EDProducer('L1TMuonLegacyConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
