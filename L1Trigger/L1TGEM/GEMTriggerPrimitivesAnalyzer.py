import FWCore.ParameterSet.Config as cms

def GEMTriggerPrimitivesAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GEMTriggerPrimitivesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
