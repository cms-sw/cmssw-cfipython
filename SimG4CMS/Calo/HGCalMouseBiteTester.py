import FWCore.ParameterSet.Config as cms

def HGCalMouseBiteTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalMouseBiteTester',
    nameSense = cms.string('HGCalEESensitive'),
    waferU = cms.int32(1),
    waferV = cms.int32(9),
    numbberOfTrials = cms.int32(1000000),
    layer = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
