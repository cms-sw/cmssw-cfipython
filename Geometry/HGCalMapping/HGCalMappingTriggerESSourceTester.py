import FWCore.ParameterSet.Config as cms

def HGCalMappingTriggerESSourceTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalMappingTriggerESSourceTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
