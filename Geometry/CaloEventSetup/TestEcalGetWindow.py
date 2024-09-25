import FWCore.ParameterSet.Config as cms

def TestEcalGetWindow(*args, **kwargs):
  mod = cms.EDAnalyzer('TestEcalGetWindow',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
