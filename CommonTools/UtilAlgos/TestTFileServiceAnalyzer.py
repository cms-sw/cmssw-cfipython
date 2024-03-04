import FWCore.ParameterSet.Config as cms

def TestTFileServiceAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestTFileServiceAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
