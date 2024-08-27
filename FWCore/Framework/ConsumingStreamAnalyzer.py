import FWCore.ParameterSet.Config as cms

def ConsumingStreamAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ConsumingStreamAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
