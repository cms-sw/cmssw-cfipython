import FWCore.ParameterSet.Config as cms

def RetrieveCTPPSBeamParameters(*args, **kwargs):
  mod = cms.EDAnalyzer('RetrieveCTPPSBeamParameters',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
