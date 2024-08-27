import FWCore.ParameterSet.Config as cms

def GsfTest(**kwargs):
  mod = cms.EDAnalyzer('GsfTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
