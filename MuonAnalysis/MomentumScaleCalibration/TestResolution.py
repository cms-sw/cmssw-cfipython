import FWCore.ParameterSet.Config as cms

def TestResolution(**kwargs):
  mod = cms.EDAnalyzer('TestResolution',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
