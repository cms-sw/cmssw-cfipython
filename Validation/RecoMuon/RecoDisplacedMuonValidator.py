import FWCore.ParameterSet.Config as cms

def RecoDisplacedMuonValidator(**kwargs):
  mod = cms.EDProducer('RecoDisplacedMuonValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
