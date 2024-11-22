import FWCore.ParameterSet.Config as cms

def WritePPSAssociationCuts(*args, **kwargs):
  mod = cms.EDAnalyzer('WritePPSAssociationCuts',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
