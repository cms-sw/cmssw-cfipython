import FWCore.ParameterSet.Config as cms

def MuonGeometrySanityCheck(**kwargs):
  mod = cms.EDAnalyzer('MuonGeometrySanityCheck',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
