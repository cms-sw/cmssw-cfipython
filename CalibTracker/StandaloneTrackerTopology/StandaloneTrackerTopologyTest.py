import FWCore.ParameterSet.Config as cms

def StandaloneTrackerTopologyTest(**kwargs):
  mod = cms.EDAnalyzer('StandaloneTrackerTopologyTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
