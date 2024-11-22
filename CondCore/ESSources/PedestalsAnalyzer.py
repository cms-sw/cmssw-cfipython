import FWCore.ParameterSet.Config as cms

def PedestalsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PedestalsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
