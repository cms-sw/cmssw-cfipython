import FWCore.ParameterSet.Config as cms

def DTTFMasksTester(**kwargs):
  mod = cms.EDAnalyzer('DTTFMasksTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
