import FWCore.ParameterSet.Config as cms

def GEMPadDigiReader(**kwargs):
  mod = cms.EDAnalyzer('GEMPadDigiReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
