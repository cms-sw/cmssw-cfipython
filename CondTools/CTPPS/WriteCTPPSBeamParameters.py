import FWCore.ParameterSet.Config as cms

def WriteCTPPSBeamParameters(*args, **kwargs):
  mod = cms.EDAnalyzer('WriteCTPPSBeamParameters',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
