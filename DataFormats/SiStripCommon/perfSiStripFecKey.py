import FWCore.ParameterSet.Config as cms

def perfSiStripFecKey(*args, **kwargs):
  mod = cms.EDAnalyzer('perfSiStripFecKey',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
