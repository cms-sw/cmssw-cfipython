import FWCore.ParameterSet.Config as cms

def DTTFParametersTester(**kwargs):
  mod = cms.EDAnalyzer('DTTFParametersTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
