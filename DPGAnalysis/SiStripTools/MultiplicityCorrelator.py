import FWCore.ParameterSet.Config as cms

def MultiplicityCorrelator(**kwargs):
  mod = cms.EDAnalyzer('MultiplicityCorrelator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
