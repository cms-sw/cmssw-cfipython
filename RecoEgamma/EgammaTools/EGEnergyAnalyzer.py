import FWCore.ParameterSet.Config as cms

def EGEnergyAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EGEnergyAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
