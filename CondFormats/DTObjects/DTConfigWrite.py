import FWCore.ParameterSet.Config as cms

def DTConfigWrite(*args, **kwargs):
  mod = cms.EDAnalyzer('DTConfigWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
