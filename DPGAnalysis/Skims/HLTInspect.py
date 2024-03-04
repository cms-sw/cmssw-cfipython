import FWCore.ParameterSet.Config as cms

def HLTInspect(**kwargs):
  mod = cms.EDAnalyzer('HLTInspect',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
