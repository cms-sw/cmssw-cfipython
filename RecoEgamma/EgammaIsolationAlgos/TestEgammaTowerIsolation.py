import FWCore.ParameterSet.Config as cms

def TestEgammaTowerIsolation(*args, **kwargs):
  mod = cms.EDAnalyzer('TestEgammaTowerIsolation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
