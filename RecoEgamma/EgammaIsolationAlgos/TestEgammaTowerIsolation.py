import FWCore.ParameterSet.Config as cms

def TestEgammaTowerIsolation(**kwargs):
  mod = cms.EDAnalyzer('TestEgammaTowerIsolation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
