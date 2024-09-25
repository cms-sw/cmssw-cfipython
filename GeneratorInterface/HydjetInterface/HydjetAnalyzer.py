import FWCore.ParameterSet.Config as cms

def HydjetAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HydjetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
