import FWCore.ParameterSet.Config as cms

def DTCCBConfigValidateDBRead(*args, **kwargs):
  mod = cms.EDAnalyzer('DTCCBConfigValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
