import FWCore.ParameterSet.Config as cms

def L1TTestsSummary(**kwargs):
  mod = cms.EDProducer('L1TTestsSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
