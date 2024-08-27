import FWCore.ParameterSet.Config as cms

def ConsumingOneSharedResourceAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ConsumingOneSharedResourceAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
