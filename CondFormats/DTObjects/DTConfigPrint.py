import FWCore.ParameterSet.Config as cms

def DTConfigPrint(*args, **kwargs):
  mod = cms.EDAnalyzer('DTConfigPrint',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
