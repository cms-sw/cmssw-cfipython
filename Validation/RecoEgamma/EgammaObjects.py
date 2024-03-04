import FWCore.ParameterSet.Config as cms

def EgammaObjects(**kwargs):
  mod = cms.EDAnalyzer('EgammaObjects',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
