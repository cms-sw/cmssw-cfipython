import FWCore.ParameterSet.Config as cms

def HGCalParameterTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalParameterTester',
    Name = cms.string('HGCalEESensitive'),
    Mode = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
