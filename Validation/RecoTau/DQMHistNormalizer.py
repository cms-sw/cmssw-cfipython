import FWCore.ParameterSet.Config as cms

def DQMHistNormalizer(*args, **kwargs):
  mod = cms.EDAnalyzer('DQMHistNormalizer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
