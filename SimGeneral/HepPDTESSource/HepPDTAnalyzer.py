import FWCore.ParameterSet.Config as cms

def HepPDTAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HepPDTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
