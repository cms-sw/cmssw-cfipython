import FWCore.ParameterSet.Config as cms

def testGeneralTracks(**kwargs):
  mod = cms.EDProducer('testGeneralTracks',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
