import FWCore.ParameterSet.Config as cms

def DTStatusFlagValidateDBRead(*args, **kwargs):
  mod = cms.EDAnalyzer('DTStatusFlagValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
