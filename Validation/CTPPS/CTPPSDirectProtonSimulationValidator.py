import FWCore.ParameterSet.Config as cms

def CTPPSDirectProtonSimulationValidator(**kwargs):
  mod = cms.EDAnalyzer('CTPPSDirectProtonSimulationValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
