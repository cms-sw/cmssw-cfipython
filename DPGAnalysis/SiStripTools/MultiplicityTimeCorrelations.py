import FWCore.ParameterSet.Config as cms

def MultiplicityTimeCorrelations(*args, **kwargs):
  mod = cms.EDAnalyzer('MultiplicityTimeCorrelations',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
