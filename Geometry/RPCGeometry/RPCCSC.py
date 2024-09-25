import FWCore.ParameterSet.Config as cms

def RPCCSC(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCCSC',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
