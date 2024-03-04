import FWCore.ParameterSet.Config as cms

def L1TMuonEndCapForestWriter(**kwargs):
  mod = cms.EDAnalyzer('L1TMuonEndCapForestWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
