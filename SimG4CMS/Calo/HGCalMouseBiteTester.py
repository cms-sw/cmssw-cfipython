import FWCore.ParameterSet.Config as cms

def HGCalMouseBiteTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalMouseBiteTester',
    nameSense = cms.string('HGCalEESensitive'),
    waferU = cms.int32(1),
    waferV = cms.int32(9),
    numbberOfTrials = cms.int32(1000000),
    layer = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
