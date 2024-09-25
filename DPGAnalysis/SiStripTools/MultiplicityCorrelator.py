import FWCore.ParameterSet.Config as cms

def MultiplicityCorrelator(*args, **kwargs):
  mod = cms.EDAnalyzer('MultiplicityCorrelator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
