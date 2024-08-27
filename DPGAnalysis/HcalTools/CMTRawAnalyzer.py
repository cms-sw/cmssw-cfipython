import FWCore.ParameterSet.Config as cms

def CMTRawAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CMTRawAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
