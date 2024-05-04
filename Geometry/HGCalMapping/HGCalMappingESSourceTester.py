import FWCore.ParameterSet.Config as cms

def HGCalMappingESSourceTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalMappingESSourceTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
