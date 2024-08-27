import FWCore.ParameterSet.Config as cms

def EfficiencyByLabelAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EfficiencyByLabelAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
