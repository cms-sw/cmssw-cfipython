import FWCore.ParameterSet.Config as cms

def GEMTriggerPrimitivesAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('GEMTriggerPrimitivesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
