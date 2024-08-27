import FWCore.ParameterSet.Config as cms

def HGCalSizeTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalSizeTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
