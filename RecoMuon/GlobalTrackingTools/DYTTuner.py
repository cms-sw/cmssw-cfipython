import FWCore.ParameterSet.Config as cms

def DYTTuner(**kwargs):
  mod = cms.EDAnalyzer('DYTTuner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
