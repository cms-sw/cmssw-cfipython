import FWCore.ParameterSet.Config as cms

def WriteVHDL(**kwargs):
  mod = cms.EDAnalyzer('WriteVHDL',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
