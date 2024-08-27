import FWCore.ParameterSet.Config as cms

def MuonGeometrySVGTemplate(**kwargs):
  mod = cms.EDAnalyzer('MuonGeometrySVGTemplate',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
