import FWCore.ParameterSet.Config as cms

def HGCalMappingESSourceTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalMappingESSourceTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
