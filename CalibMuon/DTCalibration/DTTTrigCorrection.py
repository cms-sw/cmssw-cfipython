import FWCore.ParameterSet.Config as cms

def DTTTrigCorrection(**kwargs):
  mod = cms.EDAnalyzer('DTTTrigCorrection',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
