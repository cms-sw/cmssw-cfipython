import FWCore.ParameterSet.Config as cms

def examplesSiStripFecKey(*args, **kwargs):
  mod = cms.EDAnalyzer('examplesSiStripFecKey',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
