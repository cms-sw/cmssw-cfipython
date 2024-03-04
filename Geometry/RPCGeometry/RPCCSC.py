import FWCore.ParameterSet.Config as cms

def RPCCSC(**kwargs):
  mod = cms.EDAnalyzer('RPCCSC',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
