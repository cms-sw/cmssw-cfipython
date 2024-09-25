import FWCore.ParameterSet.Config as cms

def EgammaObjects(*args, **kwargs):
  mod = cms.EDAnalyzer('EgammaObjects',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
