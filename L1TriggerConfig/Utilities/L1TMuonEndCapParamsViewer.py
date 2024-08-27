import FWCore.ParameterSet.Config as cms

def L1TMuonEndCapParamsViewer(**kwargs):
  mod = cms.EDAnalyzer('L1TMuonEndCapParamsViewer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
