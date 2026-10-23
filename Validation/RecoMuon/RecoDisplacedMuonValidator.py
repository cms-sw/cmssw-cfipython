import FWCore.ParameterSet.Config as cms

def RecoDisplacedMuonValidator(*args, **kwargs):
  mod = cms.EDProducer('RecoDisplacedMuonValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
