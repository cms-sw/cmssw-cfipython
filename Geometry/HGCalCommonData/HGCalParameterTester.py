import FWCore.ParameterSet.Config as cms

def HGCalParameterTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalParameterTester',
    Name = cms.string('HGCalEESensitive'),
    Mode = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
