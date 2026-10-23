import FWCore.ParameterSet.Config as cms

def EfficiencyByLabelAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EfficiencyByLabelAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
