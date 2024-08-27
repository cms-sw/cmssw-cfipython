import FWCore.ParameterSet.Config as cms

def ListGroups(**kwargs):
  mod = cms.EDAnalyzer('ListGroups',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
