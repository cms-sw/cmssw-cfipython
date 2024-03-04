import FWCore.ParameterSet.Config as cms

def examplesSiStripFecKey(**kwargs):
  mod = cms.EDAnalyzer('examplesSiStripFecKey',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
