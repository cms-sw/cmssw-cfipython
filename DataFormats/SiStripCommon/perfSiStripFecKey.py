import FWCore.ParameterSet.Config as cms

def perfSiStripFecKey(**kwargs):
  mod = cms.EDAnalyzer('perfSiStripFecKey',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
