import FWCore.ParameterSet.Config as cms

def ZJetsTest(**kwargs):
  mod = cms.EDAnalyzer('ZJetsTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
