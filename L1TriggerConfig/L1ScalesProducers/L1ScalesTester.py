import FWCore.ParameterSet.Config as cms

def L1ScalesTester(**kwargs):
  mod = cms.EDAnalyzer('L1ScalesTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
