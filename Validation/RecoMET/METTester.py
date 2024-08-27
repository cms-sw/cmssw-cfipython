import FWCore.ParameterSet.Config as cms

def METTester(**kwargs):
  mod = cms.EDProducer('METTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
