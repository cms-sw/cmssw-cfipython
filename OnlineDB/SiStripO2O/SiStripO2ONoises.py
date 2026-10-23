import FWCore.ParameterSet.Config as cms

def SiStripO2ONoises(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripO2ONoises',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
