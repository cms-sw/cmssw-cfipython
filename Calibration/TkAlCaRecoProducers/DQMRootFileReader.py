import FWCore.ParameterSet.Config as cms

def DQMRootFileReader(**kwargs):
  mod = cms.EDAnalyzer('DQMRootFileReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
