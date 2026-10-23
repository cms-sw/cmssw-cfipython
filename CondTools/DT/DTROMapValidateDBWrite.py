import FWCore.ParameterSet.Config as cms

def DTROMapValidateDBWrite(*args, **kwargs):
  mod = cms.EDAnalyzer('DTROMapValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
