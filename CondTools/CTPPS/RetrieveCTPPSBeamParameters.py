import FWCore.ParameterSet.Config as cms

def RetrieveCTPPSBeamParameters(**kwargs):
  mod = cms.EDAnalyzer('RetrieveCTPPSBeamParameters',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
