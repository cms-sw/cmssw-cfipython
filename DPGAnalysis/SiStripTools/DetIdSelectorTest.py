import FWCore.ParameterSet.Config as cms

def DetIdSelectorTest(*args, **kwargs):
  mod = cms.EDAnalyzer('DetIdSelectorTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
