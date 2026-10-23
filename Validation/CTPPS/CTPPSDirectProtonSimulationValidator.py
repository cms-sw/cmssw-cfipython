import FWCore.ParameterSet.Config as cms

def CTPPSDirectProtonSimulationValidator(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSDirectProtonSimulationValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
