import FWCore.ParameterSet.Config as cms

def HGCalTBParameterTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalTBParameterTester',
    name = cms.string('HGCalEESensitive'),
    mode = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
