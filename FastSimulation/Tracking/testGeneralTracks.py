import FWCore.ParameterSet.Config as cms

def testGeneralTracks(*args, **kwargs):
  mod = cms.EDProducer('testGeneralTracks',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
