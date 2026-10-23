import FWCore.ParameterSet.Config as cms

def ValidateRadial(*args, **kwargs):
  mod = cms.EDAnalyzer('ValidateRadial',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
