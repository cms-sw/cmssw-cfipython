import FWCore.ParameterSet.Config as cms

def TkVoltageMapCreator(*args, **kwargs):
  mod = cms.EDAnalyzer('TkVoltageMapCreator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
