import FWCore.ParameterSet.Config as cms

def GEMDigiReader(**kwargs):
  mod = cms.EDAnalyzer('GEMDigiReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
