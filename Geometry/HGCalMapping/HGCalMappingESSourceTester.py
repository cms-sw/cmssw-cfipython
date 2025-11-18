import FWCore.ParameterSet.Config as cms

def HGCalMappingESSourceTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalMappingESSourceTester',
    verbosity = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
