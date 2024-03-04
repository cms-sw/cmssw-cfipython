import FWCore.ParameterSet.Config as cms

def PUDumper(**kwargs):
  mod = cms.EDAnalyzer('PUDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
