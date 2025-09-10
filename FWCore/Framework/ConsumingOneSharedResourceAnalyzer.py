import FWCore.ParameterSet.Config as cms

def ConsumingOneSharedResourceAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ConsumingOneSharedResourceAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
