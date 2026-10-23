import FWCore.ParameterSet.Config as cms

def MuonGeometrySVGTemplate(*args, **kwargs):
  mod = cms.EDAnalyzer('MuonGeometrySVGTemplate',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
