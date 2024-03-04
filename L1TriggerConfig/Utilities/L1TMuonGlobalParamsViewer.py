import FWCore.ParameterSet.Config as cms

def L1TMuonGlobalParamsViewer(**kwargs):
  mod = cms.EDAnalyzer('L1TMuonGlobalParamsViewer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
