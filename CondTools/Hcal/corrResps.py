import FWCore.ParameterSet.Config as cms

def corrResps(*args, **kwargs):
  mod = cms.EDAnalyzer('corrResps',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
