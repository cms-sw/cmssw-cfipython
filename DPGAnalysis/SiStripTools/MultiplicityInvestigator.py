import FWCore.ParameterSet.Config as cms

def MultiplicityInvestigator(*args, **kwargs):
  mod = cms.EDAnalyzer('MultiplicityInvestigator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
