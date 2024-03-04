import FWCore.ParameterSet.Config as cms

def DQMHistNormalizer(**kwargs):
  mod = cms.EDAnalyzer('DQMHistNormalizer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
