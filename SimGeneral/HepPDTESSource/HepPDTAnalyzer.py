import FWCore.ParameterSet.Config as cms

def HepPDTAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HepPDTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
