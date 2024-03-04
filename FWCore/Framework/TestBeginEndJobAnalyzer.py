import FWCore.ParameterSet.Config as cms

def TestBeginEndJobAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestBeginEndJobAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
