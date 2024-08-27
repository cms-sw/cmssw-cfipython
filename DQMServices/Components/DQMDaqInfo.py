import FWCore.ParameterSet.Config as cms

def DQMDaqInfo(**kwargs):
  mod = cms.EDAnalyzer('DQMDaqInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
