import FWCore.ParameterSet.Config as cms

def HGCalTBParameterTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalTBParameterTester',
    name = cms.string('HGCalEESensitive'),
    mode = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
