import FWCore.ParameterSet.Config as cms

def DTROMapValidateDBRead(*args, **kwargs):
  mod = cms.EDAnalyzer('DTROMapValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
