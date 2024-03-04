import FWCore.ParameterSet.Config as cms

def MultiplicityInvestigator(**kwargs):
  mod = cms.EDAnalyzer('MultiplicityInvestigator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
