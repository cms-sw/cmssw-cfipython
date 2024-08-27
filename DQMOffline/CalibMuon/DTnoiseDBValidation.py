import FWCore.ParameterSet.Config as cms

def DTnoiseDBValidation(**kwargs):
  mod = cms.EDAnalyzer('DTnoiseDBValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
